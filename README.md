# NextGen Dev - Site Web Complet

Site vitrine et dashboard d'administration pour le groupe NextGen Dev, un collectif de 5 étudiants développeurs à l'Université Saint François d'Assise d'Haïti (Delmas 33).

## Fonctionnalités

### Site Public
- **Accueil** - Présentation du groupe avec animations Lottie, stats et aperçu des projets
- **Services** - Détail des 5 services (Web, Mobile, Desktop, Design, Photo)
- **Portfolio** - Grille de projets avec filtres par catégorie
- **Galerie** - Masonry grid avec lightbox
- **Événements** - Timeline des ateliers et hackathons
- **Blog** - Articles avec catégories et filtres
- **À Propos** - Présentation détaillée des 5 membres
- **Contact** - Formulaire de contact avec envoi de messages

### Dashboard Admin
- **Vue d'ensemble** - Statistiques et graphiques d'activité
- **Portfolios** - CRUD complet avec upload d'images (Cloudinary)
- **Galerie** - Upload et gestion des photos
- **Événements** - Gestion des événements avec statuts
- **Blog** - Création et édition d'articles
- **Messages** - Lecture et gestion des messages de contact
- **Paramètres** - Profil, site, réseaux sociaux et configuration API

## Stack Technique

### Frontend
- HTML5, CSS3, JavaScript Vanilla
- Lucide Icons
- GSAP + ScrollTrigger (animations)
- Lottie Web (animations vectorielles)
- Chart.js (graphiques dashboard)

### Backend
- Python 3.11+
- Flask (framework web)
- Flask-SQLAlchemy (ORM)
- Flask-JWT-Extended (authentification)
- Flask-CORS (cross-origin)
- PostgreSQL via Neon (base de données)
- Cloudinary (stockage d'images)

## Installation

### 1. Cloner le projet
```bash
git clone <repo-url>
cd nextgen-dev
```

### 2. Configuration du Backend

```bash
cd backend

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos clés
```

### 3. Configuration .env

```env
DATABASE_URL=postgresql://user:password@host.neon.tech/dbname?sslmode=require
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret
JWT_SECRET_KEY=votre_secret_key_super_securise
```

### 4. Initialisation de la base de données

```bash
python app.py
```

Dans un autre terminal, insérer les données d'exemple :
```bash
python seed_data.py
```

### 5. Lancement

```bash
# Backend (port 5000)
python app.py

# Frontend - ouvrir dans un navigateur
# Ouvrir frontend/index.html
# Ou utiliser Live Server dans VS Code
```

## Structure du projet

```
nextgen-dev/
├── backend/
│   ├── app.py              # Application Flask principale
│   ├── config.py           # Configuration
│   ├── models.py           # Modèles SQLAlchemy
│   ├── seed_data.py        # Données d'exemple
│   ├── requirements.txt    # Dépendances Python
│   └── .env.example        # Template de configuration
├── frontend/
│   ├── index.html          # Page d'accueil
│   ├── services.html
│   ├── portfolio.html
│   ├── gallery.html
│   ├── events.html
│   ├── blog.html
│   ├── about.html
│   ├── contact.html
│   ├── login.html
│   ├── css/
│   │   ├── styles.css      # Styles globaux
│   │   └── dashboard.css   # Styles dashboard
│   ├── js/
│   │   ├── api.js          # Client API
│   │   ├── auth.js         # Gestion auth
│   │   ├── utils.js        # Utilitaires
│   │   ├── animations.js   # Animations
│   │   └── main.js         # Script principal
│   ├── animations/         # Fichiers Lottie JSON
│   └── dashboard/          # Pages d'administration
│       ├── index.html
│       ├── portfolios.html
│       ├── gallery.html
│       ├── events.html
│       ├── blog.html
│       ├── messages.html
│       └── settings.html
└── README.md
```

## API Endpoints

### Authentification
- `POST /api/auth/login` - Connexion
- `GET /api/auth/me` - Profil utilisateur

### Portfolios
- `GET /api/portfolios` - Liste
- `POST /api/portfolios` - Créer
- `PUT /api/portfolios/<id>` - Modifier
- `DELETE /api/portfolios/<id>` - Supprimer

### Galerie
- `GET /api/gallery` - Liste
- `POST /api/gallery` - Ajouter
- `DELETE /api/gallery/<id>` - Supprimer

### Événements
- `GET /api/events` - Liste
- `POST /api/events` - Créer
- `PUT /api/events/<id>` - Modifier
- `DELETE /api/events/<id>` - Supprimer

### Blog
- `GET /api/blog` - Liste
- `POST /api/blog` - Créer
- `PUT /api/blog/<id>` - Modifier
- `DELETE /api/blog/<id>` - Supprimer

### Messages
- `GET /api/messages` - Liste (auth requis)
- `POST /api/messages` - Envoyer (public)
- `DELETE /api/messages/<id>` - Supprimer

### Upload
- `POST /api/upload` - Upload image vers Cloudinary

## Compte par défaut

- **Email** : admin@nextgendev.ht
- **Mot de passe** : admin123

## Équipe

- Duval David - Développeur Full Stack
- Durosier Witly - Développeur Mobile
- Juste Richcard - Designer UI/UX
- Ferdelus Christian - Développeur Backend
- Joker - Photographe & Graphiste

---

Université Saint François d'Assise - Delmas 33, Haïti
