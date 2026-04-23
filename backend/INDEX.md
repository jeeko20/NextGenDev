# 📚 Index des Guides - NextGen Dev

## 🎯 Par où commencer?

### Je veux juste lancer l'app rapidement
→ Allez à [SETUP_RAPIDE.md](SETUP_RAPIDE.md) (5 minutes)

### Je veux tous les détails
→ Allez à [NEON_SETUP.md](NEON_SETUP.md) (détaillé + explanation)

### Je veux savoir comment me connecter
→ Allez à [GUIDE_CONNEXION.md](GUIDE_CONNEXION.md)

### Je veux juste les commandes principales
→ Allez à [CHEAT_SHEET.md](CHEAT_SHEET.md)

### Je veux déployer en production
→ Allez à [DEPLOYMENT_RENDER.md](DEPLOYMENT_RENDER.md)

---

## 📋 Liste complète des guides

| Guide | Durée | Pour qui? |
|-------|-------|----------|
| [SETUP_RAPIDE.md](SETUP_RAPIDE.md) | 5 min | Débutants impatients |
| [NEON_SETUP.md](NEON_SETUP.md) | 20 min | Veux comprendre les détails |
| [GUIDE_CONNEXION.md](GUIDE_CONNEXION.md) | 5 min | Veux se connecter au dashboard |
| [CHEAT_SHEET.md](CHEAT_SHEET.md) | - | Développeurs (référence) |
| [README_MIGRATION.md](README_MIGRATION.md) | 10 min | Veut aussi les migrations |
| [DEPLOYMENT_RENDER.md](DEPLOYMENT_RENDER.md) | 10 min | Production sur Render |

---

## 🚀 Flux typique

```
Installation    SETUP_RAPIDE.md
     ↓
Configuration   Créer .env (voir NEON_SETUP.md)
     ↓
Connexion       GUIDE_CONNEXION.md
     ↓
Développement   CHEAT_SHEET.md
     ↓
Déploiement     DEPLOYMENT_RENDER.md (optionnel)
```

---

## 🔑 Points essentiels

1. **DATABASE_URL**: obtenir sur https://console.neon.tech/
2. **Fichier .env**: créer dans `backend/` avec DATABASE_URL
3. **python db.py init**: créer les tables
4. **python db.py admin**: créer un utilisateur
5. **python app.py**: lancer l'app
6. **http://localhost:5000/docs/login.html**: se connecter

---

## 📁 Structure du projet

```
app/
├── backend/
│   ├── app.py                  # Application principale
│   ├── models.py               # Modèles base de données
│   ├── config.py               # Configuration
│   ├── requirements.txt        # Dépendances
│   ├── .env                    # Configuration (NE PAS COMMITTER!)
│   ├── db.py                   # Gestion base de données
│   ├── test_neon.py            # Test connexion
│   │
│   ├── SETUP_RAPIDE.md         # 👈 Commençez ici
│   ├── NEON_SETUP.md
│   ├── GUIDE_CONNEXION.md
│   ├── CHEAT_SHEET.md
│   ├── README_MIGRATION.md
│   ├── DEPLOYMENT_RENDER.md
│   └── INDEX.md                ← Vous êtes ici!
│
├── docs/
│   ├── index.html              # Accueil
│   ├── login.html              # Connexion admin
│   ├── contact.html            # Page contact (avec WhatsApp!)
│   ├── css/
│   └── dashboard/
│       ├── index.html          # Accueil dashboard
│       ├── settings.html       # Paramètres (pour modifier username/password)
│       └── ...
```

---

## 🎯 Tâches principales

- ✅ **Configurer la base de données Neon** (SETUP_RAPIDE.md)
- ✅ **Se connecter au dashboard** (GUIDE_CONNEXION.md)
- ✅ **Modifier username/password** (Paramètres > Profil)
- ✅ **Ajouter numéro WhatsApp** (Paramètres > Site)
- ⬜ Ajouter des projets
- ⬜ Ajouter des images
- ⬜ Écrire des articles
- ⬜ Déployer en production (DEPLOYMENT_RENDER.md)

---

## 🆘 En cas de problème

| Problème | Solution |
|----------|----------|
| DATABASE_URL non trouvé | Créer `.env` avec DATABASE_URL (voir SETUP_RAPIDE.md) |
| "Connection refused" | Vérifier que Neon est accessible |
| "Access denied" | Vérifier username/password dans DATABASE_URL |
| "Port 5000 occupé" | `python app.py --port 5001` |
| "Oublié le password" | `python db.py users` puis `python db.py admin` |
| "Page blanche après login" | Ouvrir F12 > Console pour voir les erreurs |

---

## 💡 Tips rapides

```bash
# Lancer l'app
python app.py

# Créer un admin
python db.py admin

# Voir les users
python db.py users

# Réinitialiser (ATTENTION!)
python db.py reset

# Tester connexion Neon
python test_neon.py

# Installer dépendances
pip install -r requirements.txt
```

---

## 🎨 Nouvelles fonctionnalités ajoutées

- ✅ **Champ `username`**: Pour se connecter au lieu de l'email
- ✅ **Champ `whatsapp_number`**: Dans les paramètres du site
- ✅ **Lien WhatsApp dynamique**: Sur la page contact
- ✅ **Modification password/email**: Dans les paramètres du profil

---

## 📞 Support

- Consultez les guides en français (.md)
- Vérifiez CHEAT_SHEET.md pour les commandes
- Testez avec `python test_neon.py`
- Regardez les logs: `python app.py`

---

**Bonne chance! 🚀**

Commencez par [SETUP_RAPIDE.md](SETUP_RAPIDE.md) si c'est votre première fois!
