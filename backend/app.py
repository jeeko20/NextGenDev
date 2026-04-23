import os
import json
from datetime import datetime
from functools import wraps

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import cloudinary
import cloudinary.uploader
import cloudinary.api

from config import Config
from models import db, Portfolio, PortfolioImage, GalleryImage, Event, BlogPost, Message, User, SiteSettings

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
CORS(app, 
     resources={r"/api/*": {"origins": "*"}},
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     supports_credentials=False,
     send_wildcard=True)

# Configure Cloudinary
if Config.CLOUDINARY_CLOUD_NAME:
    cloudinary.config(
        cloud_name=Config.CLOUDINARY_CLOUD_NAME,
        api_key=Config.CLOUDINARY_API_KEY,
        api_secret=Config.CLOUDINARY_API_SECRET,
        secure=True
    )

# ============ AUTH ROUTES ============

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    name = data.get('name', 'Admin')
    
    if not username or not email or not password:
        return jsonify({'error': 'Nom d\'utilisateur, email et mot de passe requis'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Ce nom d\'utilisateur est déjà utilisé'}), 409
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Cet email est déjà utilisé'}), 409
    
    user = User(
        username=username,
        email=email,
        name=name,
        password_hash=generate_password_hash(password),
        role='admin'
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'Utilisateur créé avec succès', 'user': user.to_dict()}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Nom d\'utilisateur et mot de passe requis'}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Nom d\'utilisateur ou mot de passe incorrect'}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({
        'access_token': access_token,
        'user': user.to_dict()
    }), 200

@app.route('/api/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Utilisateur non trouvé'}), 404
    return jsonify({'user': user.to_dict()}), 200

@app.route('/api/auth/me', methods=['PUT'])
@jwt_required()
def update_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Utilisateur non trouvé'}), 404
    
    data = request.get_json()
    if 'name' in data:
        user.name = data['name']
    if 'username' in data:
        existing = User.query.filter_by(username=data['username']).first()
        if existing and existing.id != user.id:
            return jsonify({'error': 'Ce nom d\'utilisateur est déjà utilisé'}), 409
        user.username = data['username']
    if 'email' in data:
        existing = User.query.filter_by(email=data['email']).first()
        if existing and existing.id != user.id:
            return jsonify({'error': 'Cet email est déjà utilisé'}), 409
        user.email = data['email']
    if 'avatar_url' in data:
        user.avatar_url = data['avatar_url']
    if 'password' in data and data['password']:
        user.password_hash = generate_password_hash(data['password'])
    
    db.session.commit()
    return jsonify({'user': user.to_dict()}), 200

# ============ PORTFOLIO ROUTES ============

@app.route('/api/portfolios', methods=['GET'])
def get_portfolios():
    category = request.args.get('category')
    query = Portfolio.query
    if category:
        query = query.filter_by(category=category)
    portfolios = query.order_by(Portfolio.created_at.desc()).all()
    return jsonify([p.to_dict() for p in portfolios]), 200

@app.route('/api/portfolios/<int:id>', methods=['GET'])
def get_portfolio(id):
    portfolio = Portfolio.query.get_or_404(id)
    return jsonify(portfolio.to_dict()), 200

@app.route('/api/portfolios', methods=['POST'])
@jwt_required()
def create_portfolio():
    data = request.get_json()
    
    portfolio = Portfolio(
        title=data.get('title'),
        description=data.get('description'),
        category=data.get('category', 'Sites Web'),
        technologies=json.dumps(data.get('technologies', [])),
        image_url=data.get('image_url'),
        project_url=data.get('project_url')
    )
    
    db.session.add(portfolio)
    db.session.commit()
    return jsonify(portfolio.to_dict()), 201

@app.route('/api/portfolios/<int:id>', methods=['PUT'])
@jwt_required()
def update_portfolio(id):
    portfolio = Portfolio.query.get_or_404(id)
    data = request.get_json()
    
    portfolio.title = data.get('title', portfolio.title)
    portfolio.description = data.get('description', portfolio.description)
    portfolio.category = data.get('category', portfolio.category)
    if 'technologies' in data:
        portfolio.technologies = json.dumps(data['technologies'])
    portfolio.image_url = data.get('image_url', portfolio.image_url)
    portfolio.project_url = data.get('project_url', portfolio.project_url)
    portfolio.updated_at = datetime.utcnow()
    
    db.session.commit()
    return jsonify(portfolio.to_dict()), 200

@app.route('/api/portfolios/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_portfolio(id):
    portfolio = Portfolio.query.get_or_404(id)
    db.session.delete(portfolio)
    db.session.commit()
    return jsonify({'message': 'Portfolio supprimé avec succès'}), 200

# Portfolio Images Routes
@app.route('/api/portfolios/<int:portfolio_id>/images', methods=['GET'])
def get_portfolio_images(portfolio_id):
    images = PortfolioImage.query.filter_by(portfolio_id=portfolio_id).order_by(PortfolioImage.order).all()
    return jsonify([img.to_dict() for img in images]), 200

@app.route('/api/portfolios/<int:portfolio_id>/images', methods=['POST'])
@jwt_required()
def add_portfolio_image(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    data = request.get_json()
    
    # Get the next order number
    max_order = db.session.query(db.func.max(PortfolioImage.order)).filter_by(portfolio_id=portfolio_id).scalar() or 0
    
    image = PortfolioImage(
        portfolio_id=portfolio_id,
        image_url=data.get('image_url'),
        alt_text=data.get('alt_text'),
        order=max_order + 1
    )
    
    db.session.add(image)
    db.session.commit()
    return jsonify(image.to_dict()), 201

@app.route('/api/portfolios/<int:portfolio_id>/images/<int:image_id>', methods=['DELETE'])
@jwt_required()
def delete_portfolio_image(portfolio_id, image_id):
    image = PortfolioImage.query.filter_by(id=image_id, portfolio_id=portfolio_id).first_or_404()
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image supprimée avec succès'}), 200

@app.route('/api/portfolios/<int:portfolio_id>/images/reorder', methods=['PUT'])
@jwt_required()
def reorder_portfolio_images(portfolio_id):
    data = request.get_json()
    image_orders = data.get('image_orders', [])
    
    for order_data in image_orders:
        image = PortfolioImage.query.filter_by(id=order_data['id'], portfolio_id=portfolio_id).first()
        if image:
            image.order = order_data['order']
    
    db.session.commit()
    return jsonify({'message': 'Ordre des images mis à jour'}), 200

# ============ GALLERY ROUTES ============

@app.route('/api/gallery', methods=['GET'])
def get_gallery():
    category = request.args.get('category')
    query = GalleryImage.query
    if category:
        query = query.filter_by(category=category)
    images = query.order_by(GalleryImage.created_at.desc()).all()
    return jsonify([img.to_dict() for img in images]), 200

@app.route('/api/gallery/<int:id>', methods=['GET'])
def get_gallery_image(id):
    image = GalleryImage.query.get_or_404(id)
    return jsonify(image.to_dict()), 200

@app.route('/api/gallery', methods=['POST'])
@jwt_required()
def create_gallery_image():
    data = request.get_json()
    
    image = GalleryImage(
        title=data.get('title'),
        category=data.get('category', 'Général'),
        image_url=data.get('image_url'),
        description=data.get('description')
    )
    
    db.session.add(image)
    db.session.commit()
    return jsonify(image.to_dict()), 201

@app.route('/api/gallery/<int:id>', methods=['PUT'])
@jwt_required()
def update_gallery_image(id):
    image = GalleryImage.query.get_or_404(id)
    data = request.get_json()
    
    image.title = data.get('title', image.title)
    image.category = data.get('category', image.category)
    image.image_url = data.get('image_url', image.image_url)
    image.description = data.get('description', image.description)
    
    db.session.commit()
    return jsonify(image.to_dict()), 200

@app.route('/api/gallery/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_gallery_image(id):
    image = GalleryImage.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image supprimée avec succès'}), 200

# ============ EVENT ROUTES ============

@app.route('/api/events', methods=['GET'])
def get_events():
    status = request.args.get('status')
    query = Event.query
    if status:
        query = query.filter_by(status=status)
    events = query.order_by(Event.date.desc()).all()
    return jsonify([e.to_dict() for e in events]), 200

@app.route('/api/events/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify(event.to_dict()), 200

@app.route('/api/events', methods=['POST'])
@jwt_required()
def create_event():
    data = request.get_json()
    
    event = Event(
        title=data.get('title'),
        description=data.get('description'),
        date=datetime.strptime(data.get('date'), '%Y-%m-%d').date() if data.get('date') else datetime.now().date(),
        time=data.get('time'),
        location=data.get('location'),
        image_url=data.get('image_url'),
        status=data.get('status', 'À venir')
    )
    
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_dict()), 201

@app.route('/api/events/<int:id>', methods=['PUT'])
@jwt_required()
def update_event(id):
    event = Event.query.get_or_404(id)
    data = request.get_json()
    
    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)
    if data.get('date'):
        event.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    event.time = data.get('time', event.time)
    event.location = data.get('location', event.location)
    event.image_url = data.get('image_url', event.image_url)
    event.status = data.get('status', event.status)
    
    db.session.commit()
    return jsonify(event.to_dict()), 200

@app.route('/api/events/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Événement supprimé avec succès'}), 200

# ============ BLOG ROUTES ============

@app.route('/api/blog', methods=['GET'])
def get_blog_posts():
    status = request.args.get('status')
    category = request.args.get('category')
    query = BlogPost.query
    if status:
        query = query.filter_by(status=status)
    if category:
        query = query.filter_by(category=category)
    posts = query.order_by(BlogPost.created_at.desc()).all()
    return jsonify([p.to_dict() for p in posts]), 200

@app.route('/api/blog/<int:id>', methods=['GET'])
def get_blog_post(id):
    post = BlogPost.query.get_or_404(id)
    return jsonify(post.to_dict()), 200

@app.route('/api/blog/slug/<slug>', methods=['GET'])
def get_blog_post_by_slug(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return jsonify(post.to_dict()), 200

@app.route('/api/blog', methods=['POST'])
@jwt_required()
def create_blog_post():
    data = request.get_json()
    
    slug = data.get('slug') or data.get('title', '').lower().replace(' ', '-')
    
    post = BlogPost(
        title=data.get('title'),
        slug=slug,
        category=data.get('category'),
        excerpt=data.get('excerpt'),
        content=data.get('content'),
        featured_image=data.get('featured_image'),
        status=data.get('status', 'draft')
    )
    
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@app.route('/api/blog/<int:id>', methods=['PUT'])
@jwt_required()
def update_blog_post(id):
    post = BlogPost.query.get_or_404(id)
    data = request.get_json()
    
    post.title = data.get('title', post.title)
    if data.get('slug'):
        post.slug = data['slug']
    post.category = data.get('category', post.category)
    post.excerpt = data.get('excerpt', post.excerpt)
    post.content = data.get('content', post.content)
    post.featured_image = data.get('featured_image', post.featured_image)
    post.status = data.get('status', post.status)
    post.updated_at = datetime.utcnow()
    
    db.session.commit()
    return jsonify(post.to_dict()), 200

@app.route('/api/blog/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_blog_post(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Article supprimé avec succès'}), 200

# ============ MESSAGE ROUTES ============

@app.route('/api/messages', methods=['GET'])
@jwt_required()
def get_messages():
    status = request.args.get('status')
    query = Message.query
    if status:
        query = query.filter_by(status=status)
    messages = query.order_by(Message.created_at.desc()).all()
    return jsonify([m.to_dict() for m in messages]), 200

@app.route('/api/messages/<int:id>', methods=['GET'])
@jwt_required()
def get_message(id):
    message = Message.query.get_or_404(id)
    return jsonify(message.to_dict()), 200

@app.route('/api/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    
    if not data.get('name') or not data.get('email') or not data.get('message'):
        return jsonify({'error': 'Nom, email et message sont requis'}), 400
    
    message = Message(
        name=data.get('name'),
        email=data.get('email'),
        subject=data.get('subject', 'Contact'),
        message=data.get('message')
    )
    
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message envoyé avec succès', 'data': message.to_dict()}), 201

@app.route('/api/messages/<int:id>/read', methods=['PUT'])
@jwt_required()
def mark_message_read(id):
    message = Message.query.get_or_404(id)
    message.status = 'read'
    db.session.commit()
    return jsonify(message.to_dict()), 200

@app.route('/api/messages/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message supprimé avec succès'}), 200

# ============ UPLOAD ROUTES ============

@app.route('/api/upload', methods=['POST'])
@jwt_required()
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucun fichier fourni'}), 400
    
    file = request.files['image']
    folder = request.form.get('folder', 'nextgen-dev')
    
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400
    
    try:
        result = cloudinary.uploader.upload(file, folder=folder)
        return jsonify({
            'url': result['secure_url'],
            'public_id': result['public_id']
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload/multiple', methods=['POST'])
@jwt_required()
def upload_multiple_images():
    if 'images' not in request.files:
        return jsonify({'error': 'Aucun fichier fourni'}), 400
    
    files = request.files.getlist('images')
    folder = request.form.get('folder', 'nextgen-dev')
    uploaded = []
    
    for file in files:
        if file.filename:
            try:
                result = cloudinary.uploader.upload(file, folder=folder)
                uploaded.append({
                    'url': result['secure_url'],
                    'public_id': result['public_id']
                })
            except Exception as e:
                continue
    
    return jsonify({'uploaded': uploaded}), 200

# ============ STATS ROUTES ============

@app.route('/api/stats', methods=['GET'])
@jwt_required()
def get_stats():
    portfolio_count = Portfolio.query.count()
    gallery_count = GalleryImage.query.count()
    event_count = Event.query.count()
    blog_count = BlogPost.query.count()
    message_count = Message.query.count()
    unread_messages = Message.query.filter_by(status='unread').count()
    
    # Recent activity (last 6 months)
    from datetime import timedelta
    six_months_ago = datetime.utcnow() - timedelta(days=180)
    
    recent_portfolios = Portfolio.query.filter(Portfolio.created_at >= six_months_ago).count()
    recent_messages = Message.query.filter(Message.created_at >= six_months_ago).count()
    
    return jsonify({
        'portfolio_count': portfolio_count,
        'gallery_count': gallery_count,
        'event_count': event_count,
        'blog_count': blog_count,
        'message_count': message_count,
        'unread_messages': unread_messages,
        'recent_portfolios': recent_portfolios,
        'recent_messages': recent_messages
    }), 200

# ============ SETTINGS ROUTES ============

@app.route('/api/settings', methods=['GET'])
def get_settings():
    settings = SiteSettings.query.first()
    if not settings:
        settings = SiteSettings()
        db.session.add(settings)
        db.session.commit()
    return jsonify(settings.to_dict()), 200

@app.route('/api/settings', methods=['PUT'])
@jwt_required()
def update_settings():
    settings = SiteSettings.query.first()
    if not settings:
        settings = SiteSettings()
        db.session.add(settings)
    
    data = request.get_json()
    for key, value in data.items():
        if hasattr(settings, key):
            setattr(settings, key, value)
    
    settings.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify(settings.to_dict()), 200

# ============ ERROR HANDLERS ============

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Ressource non trouvée'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Erreur serveur interne'}), 500

# ============ MAIN ============

def create_tables():
    with app.app_context():
        # Créer les tables manquantes sans supprimer les données existantes
        db.create_all()
        
        # Create default settings if not exists
        if not SiteSettings.query.first():
            settings = SiteSettings()
            db.session.add(settings)
        
        # Create default admin user if no users exist
        if not User.query.first():
            admin = User(
                email='admin@nextgendev.ht',
                username='admin',
                name='Admin NextGen',
                password_hash=generate_password_hash('admin123'),
                role='admin'
            )
            db.session.add(admin)
        
        db.session.commit()
        print("Tables créées avec succès!")

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)
