# ⚡ Cheat Sheet - Commandes Essentielles

## 🚀 Démarrage rapide (première fois)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate          # Mac/Linux
# venv\Scripts\activate            # Windows

pip install -r requirements.txt
python test_neon.py               # Vérifier connexion
python db.py init                 # Créer tables
python db.py admin                # Créer admin
python app.py                      # Lancer l'app
```

Puis ouvrez: **http://localhost:5000/docs/login.html**

---

## 📁 Gestion de la base de données

```bash
# Initialiser les tables
python db.py init

# Créer un administrateur
python db.py admin

# Voir tous les utilisateurs
python db.py users

# Réinitialiser complètement (⚠️ SUPPRIME TOUT)
python db.py reset

# Supprimer toutes les tables (⚠️ DANGER)
python db.py drop
```

---

## 🔌 Tests de connexion

```bash
# Tester la connexion Neon
python test_neon.py

# Tester l'API avec curl (depuis terminal)
curl http://localhost:5000/api/settings

# Tester la connexion (depuis terminal)
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"votre_password"}'
```

---

## 🛠️ Développement

```bash
# Lancer l'app en mode développement
python app.py

# Accéder à l'API
http://localhost:5000/api

# Accéder au login
http://localhost:5000/docs/login.html

# Accéder au dashboard
http://localhost:5000/docs/dashboard/index.html

# Accéder à la page contact
http://localhost:5000/docs/contact.html
```

---

## 📦 Dépendances

```bash
# Voir les packages installés
pip list

# Installer un nouveau package
pip install nombre-du-package

# Mettre à jour requirements.txt
pip freeze > requirements.txt

# Réinstaller tous les packages
pip install -r requirements.txt --force-reinstall
```

---

## 🆘 Troubleshooting

```bash
# Reactivate venv après redémarrage
source venv/bin/activate          # Mac/Linux
# venv\Scripts\activate            # Windows

# Port 5000 occupé? Changer le port
python app.py --port 5001

# Erreur SSL/Port 443?
# Ajouter export FLASK_ENV=development dans venv

# Problème de base de données?
python test_neon.py               # Diagnostiquer

# Besoin de logs?
python app.py --debug              # Mode debug
```

---

## 📝 Fichiers importants

```
backend/
├── .env                   # Configuration (NE PAS COMMITTER!)
├── app.py                 # Application principale
├── models.py              # Modèles de base de données
├── config.py              # Configuration Flask
├── requirements.txt       # Dépendances Python
├── db.py                  # Gestion base de données
├── test_neon.py           # Test connexion Neon
├── SETUP_RAPIDE.md        # Guide rapide
├── GUIDE_CONNEXION.md     # Comment se connecter
└── .gitignore             # Ignore .env!

docs/
├── login.html             # Page de connexion
└── dashboard/
    └── settings.html      # Paramètres admin
```

---

## ✅ Checklist avant de lancer

- [ ] Fichier `.env` créé avec DATABASE_URL
- [ ] `pip install -r requirements.txt` exécuté
- [ ] `python test_neon.py` ✓ réussi
- [ ] `python db.py init` ✓ exécuté
- [ ] `python db.py admin` ✓ admin créé
- [ ] `python app.py` ✓ app lancée
- [ ] http://localhost:5000/docs/login.html ✓ accessible
- [ ] Connexion au dashboard ✓ réussie

---

## 🎯 Prochaines étapes

1. Configurer les paramètres du site (Paramètres > Site)
2. Ajouter votre numéro WhatsApp
3. Ajouter vos réseaux sociaux
4. Ajouter des projets/portfolio
5. Ajouter des images à la galerie
6. Écrire des articles de blog

---

## 💡 Pro Tips

- Utilisez `python db.py users` pour voir les infos utilisateur
- La base de données Neon persiste en ligne, pas besoin de l'initialiser à chaque fois
- WhatsApp utilise le format international: `+509XXXXXXXX`
- L'email de contact dans les paramètres est utilisé sur la page contact
- Les tokens JWT durent 24h par défaut

---

**Besoin d'aide complète?** Consultez:
- `SETUP_RAPIDE.md` - Pour faire le setup initial
- `NEON_SETUP.md` - Pour les détails Neon
- `GUIDE_CONNEXION.md` - Pour se connecter et utiliser le dashboard
