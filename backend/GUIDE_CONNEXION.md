# Guide de Connexion au Dashboard

## Première Connexion

### 1. L'app est lancée

Assurez-vous que l'app court:
```bash
python app.py
```

Vous devriez voir:
```
 * Running on http://localhost:5000 (Press CTRL+C to quit)
 * Restarting with reloader
```

### 2. Aller à la page de connexion

Ouvrez votre navigateur et allez à:
```
http://localhost:5000/docs/login.html
```

### 3. Entrer vos identifiants

**Nom d'utilisateur**: Le username créé avec `python db.py admin`
**Mot de passe**: Le mot de passe entré lors de la création

Exemple:
```
Username: admin
Password: ••••••••••
```

### 4. Connectez-vous!

Cliquez sur "Se connecter"

✅ Vous êtes maintenant sur le dashboard!

---

## Récupérer les identifiants oubliés

Si vous avez oublié votre password:

```bash
# Voir tous les users
python db.py users

# Recréer un admin (vous pouvez avoir plusieurs admins)
python db.py admin
```

---

## Après la connexion - Ce que vous pouvez faire

### 📊 Dashboard (Accueil)
- Vue d'ensemble des données
- Statistiques

### 📁 Portfolios
- Ajouter/éditer/supprimer des projets
- Gérer les catégories

### 🖼️ Galerie
- Ajouter des images
- Organiser par catégories

### 📅 Événements
- Créer des événements
- Mettre à jour les dates

### 📝 Blog
- Écrire des articles
- Publier/brouillon

### 💬 Messages
- Consulter les messages reçus
- Répondre si besoin

### ⚙️ Paramètres (IMPORTANT!)
Cliquez sur "Paramètres" pour:

**Profil:**
- Changer votre nom d'utilisateur ✅
- Changer votre email ✅
- Changer votre mot de passe ✅

**Site:**
- Titre du site
- Description
- Email de contact
- Téléphone
- **Numéro WhatsApp** ✅ (Nouveau!)
- Adresse

**Réseaux sociaux:**
- URLs Facebook, Instagram, Twitter, LinkedIn

**API:**
- Configuration des clés API

---

## 🎯 À faire en premier

1. ✅ **Aller dans Paramètres > Profil**
   - Changez votre password si vous avez un password simple
   - Mettez votre vrai email

2. ✅ **Aller dans Paramètres > Site**
   - Mettez le vrai titre du site
   - Ajoutez votre description
   - **Ajoutez votre numéro WhatsApp** (+509...)
   - Mettez votre email de contact
   - Mettez votre téléphone
   - Mettez votre adresse

3. ✅ **Aller dans Paramètres > Réseaux sociaux**
   - Ajoutez vos URLs Facebook, Instagram, etc.

4. ✅ **Enregistrer** les modifications

---

## 🔐 Sécurité

- **Ne partagez jamais** votre username/password
- **Changez souvent** votre mot de passe
- **Utilisez un mot de passe fort**: Mélange de majuscules, minuscules, chiffres, symboles

Exemple bon password: `Admin@123!NextGenDev2024`

---

## 📱 Vérifier que WhatsApp marche

1. Allez à `http://localhost:5000/docs/contact.html`
2. Vous devriez voir votre numéro WhatsApp
3. Cliquez dessus = cela devrait ouvrir WhatsApp

---

## ❓ FAQ

**Q: Je vois une erreur 401 "Unauthorized"**
A: Vérifiez votre username et password. Créez un nouveau admin: `python db.py admin`

**Q: La page reste blanche**
A: Vérifiez la console (F12 > Console) pour les erreurs JavaScript

**Q: Les paramètres ne s'enregistrent pas**
A: Vérifiez que l'API répond: `curl http://localhost:5000/api/settings`

**Q: Je veux ajouter un autre admin**
A: `python db.py admin` et remplissez les infos

---

Besoin d'aide? Vérifiez les fichiers de guide complets:
- `SETUP_RAPIDE.md` - Setup rapide
- `NEON_SETUP.md` - Setup détaillé Neon
- `README_MIGRATION.md` - Résumé complet
