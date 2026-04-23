# Résumé des Étapes - Migration avec Neon

## 📋 Checklist

- [ ] Créer un 1. **Créer un projet sur Neon** (https://console.neon.tech)
- [ ] Copier la `DATABASE_URL`
- [ ] Créer le fichier `.env` dans `backend/`
- [ ] Créer l'environnement virtuel
- [ ] Installer les dépendances avec pip
- [ ] Tester la connexion avec `test_neon.py`
- [ ] Initialiser la base avec `db.py init`
- [ ] Créer un admin avec `db.py admin`
- [ ] Lancer l'app avec `python app.py`
- [ ] Vous connecter au dashboard

## 🚀 Commandes à exécuter

### 1. Configuration initiale

```bash
cd backend

# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate
# Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration Neon

```bash
# Créer le fichier .env (voir SETUP_RAPIDE.md)
# Puis tester:
python test_neon.py
```

### 3. Initialiser la base de données

```bash
# Créer toutes les tables
python db.py init

# Créer un utilisateur admin
python db.py admin
```

### 4. Lancer l'application

```bash
python app.py
```

L'application sera disponible à:
- **API**: http://localhost:5000/api
- **Login**: http://localhost:5000/docs/login.html
- **Dashboard**: http://localhost:5000/docs/dashboard/index.html

## 📁 Fichiers créés/modifiés

- ✏️ `requirements.txt` - Ajout de Flask-Migrate
- ✨ `db.py` - Gestion de la base de données (init, create admin, etc)
- ✨ `test_neon.py` - Test de connexion Neon
- ✨ `migrate.py` - Migration avec Flask-Migrate (optionnel)
- 📄 `SETUP_RAPIDE.md` - Guide rapide en français
- 📄 `NEON_SETUP.md` - Guide détaillé

## 🔐 Sécurité

Jamais ne commitez `.env` !

Vérifiez votre `.gitignore`:
```
.env
.env.local
__pycache__/
*.pyc
venv/
```

## 💡 Astuces

**Pour modifier les identifiants admin après:**
```bash
python db.py users       # Voir les utilisateurs
```

**Pour réinitialiser complètement:**
```bash
python db.py reset       # ⚠️ Supprime tout!
python db.py init        # Recréer les tables
python db.py admin       # Recréer un admin
```

**Pour voir les logs de la base:**
```
# Sur Neon: Project > Monitoring > Logs
```

---

**Besoin d'aide?** Consultez SETUP_RAPIDE.md ou NEON_SETUP.md
