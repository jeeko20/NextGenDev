# ⚡ Guide Rapide - Migration vers Neon

## Étape 1️⃣: Obtenir votre DATABASE_URL

### Sur Neon:
1. Allez à https://console.neon.tech/
2. Ouvrez votre projet
3. Cliquez sur **"Connection"**
4. Sélectionnez **"Python"** (ou psycopg2)
5. **Copiez** l'URL (ressemble à: `postgresql://user:pass@ep-xxx.neon.tech/dbname`)

## Étape 2️⃣: Créer le fichier `.env`

Dans le dossier `backend/`, créez un fichier `.env`:

```bash
DATABASE_URL=postgresql://your_user:your_password@ep-xxxx-xxxx.us-east-1.neon.tech/neondb
JWT_SECRET_KEY=votre_secret_key
```

⚠️ **Ne partagez jamais ce fichier!**

## Étape 3️⃣: Installer les dépendances

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Étape 4️⃣: Tester la connexion Neon

```bash
python test_neon.py
```

Si vous voyez ✓ "Connexion réussie", continuez!

## Étape 5️⃣: Initialiser la base de données

```bash
python db.py init
```

Cela crée toutes les tables dans Neon.

## Étape 6️⃣: Créer un admin

```bash
python db.py admin
```

Répondez aux questions:
- Username: `admin` (ou votre préférence)
- Email: `admin@example.com`
- Mot de passe: quelque chose de sécurisé
- Nom: `Administrateur`

## Étape 7️⃣: Lancer l'app

```bash
python app.py
```

Vous devriez voir:
```
 * Running on http://localhost:5000
```

## Étape 8️⃣: Accéder au dashboard

1. Allez à `http://localhost:5000/docs/login.html`
2. Entrez votre username et password
3. Boom! 🎉 Vous êtes connecté!

---

## 🆘 Problèmes?

**"database does not exist"**
→ Vérifiez que votre DATABASE_URL est correct

**"psycopg2 error"**
→ Installez: `pip install psycopg2-binary`

**"IP not allowed"**
→ Allez sur Neon > Settings > Network > Autorisez votre IP publique

**"Access denied"**
→ Vérifiez l'username et password dans DATABASE_URL

---

## 📚 Autres commandes utiles

```bash
# Voir tous les utilisateurs
python db.py users

# Réinitialiser la base (ATTENTION!)
python db.py reset

# Supprimer toutes les tables (DANGER!)
python db.py drop
```

Voilà! C'est simple comme ça 🚀
