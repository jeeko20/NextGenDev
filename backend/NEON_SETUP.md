# Guide de Configuration avec Neon PostgreSQL

## 1. Obtenez votre DATABASE_URL sur Neon

### Étapes:
1. Allez sur [https://console.neon.tech/](https://console.neon.tech/)
2. Connectez-vous ou créez un compte
3. Créez un nouveau projet (ou sélectionnez-en un)
4. Dans "Connection string", sélectionnez "Postgres" (ou "psycopg2")
5. Copiez l'URL complète (elle ressemble à):
   ```
   postgresql://user:password@ep-xxxx.xxxx.neon.tech/nextgendev
   ```

## 2. Créer le fichier .env

Dans `backend/`, créez un fichier `.env`:

```bash
# Database - Neon PostgreSQL
DATABASE_URL=postgresql://user:password@ep-xxxx.xxxx.neon.tech/nextgendev

# JWT Secret
JWT_SECRET_KEY=votre-secret-key-super-securisee

# Cloudinary (optionnel)
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5000
```

**⚠️ IMPORTANT**: Ne partagez jamais votre `.env` publiquement !

## 3. Créer l'environnement virtuel et installer les dépendances

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Initialiser les migrations

```bash
python migrate.py init
```

Cela crée un dossier `migrations/` s'il n'existe pas.

## 5. Créer une migration initiale

```bash
python migrate.py create "Initial migration"
```

## 6. Appliquer les migrations à la base de données Neon

```bash
python migrate.py upgrade
```

✓ Votre base de données est maintenant à jour !

## 7. Créer un admin utilisateur

```bash
python3 << 'EOF'
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Vérifier si un admin existe déjà
    admin = User.query.first()
    
    if not admin:
        admin = User(
            username='admin',
            email='admin@nextgendev.ht',
            name='Administrateur',
            password_hash=generate_password_hash('votre_mot_de_passe_securise'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print("✓ Admin créé: username='admin', password='votre_mot_de_passe_securise'")
    else:
        print("✓ Un admin existe déjà")
EOF
```

## 8. Tester la connexion

Lancez l'application:

```bash
python app.py
```

L'API sera disponible à:
- Local: `http://localhost:5000/api`
- Render (en production): `https://votre-app.onrender.com/api`

Testez la connexion:

```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"votre_mot_de_passe_securise"}'
```

## 9. Accès au dashboard admin

1. Ouvrez `docs/login.html` dans votre navigateur
2. Entrez:
   - Nom d'utilisateur: `admin`
   - Mot de passe: `votre_mot_de_passe_securise`
3. Vous êtes maintenant connecté au dashboard!

## Commandes de migration utiles

```bash
# Voir l'état des migrations
alembic current

# Annuler la dernière migration
python migrate.py downgrade

# Créer une migration après modification des modèles
python migrate.py create "Add new field"
python migrate.py upgrade
```

## Troubleshooting

### "database does not exist"
Neon crée automatiquement la base. Si erreur, vérifiez votre DATABASE_URL.

### "psycopg2 error"
Assurez-vous que `psycopg2-binary` est installé:
```bash
pip install psycopg2-binary
```

### Port 5000 déjà utilisé
Changez le port:
```bash
python app.py --port 5001
```

### Problèmes de connexion Neon
- Vérifiez que votre IP est autorisée (Neon > Project settings)
- Vérifiez que la DATABASE_URL est complète et correcte
- Testez la connexion: `psql "votre_database_url"`

---

**Besoin d'aide?** Consultez la [documentation Neon](https://neon.tech/docs) ou [Flask-Migrate](https://flask-migrate.readthedocs.io/)
