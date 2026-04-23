# Déploiement sur Render (Production)

## 🔗 Connexion Render + Neon (déjà prête!)

Votre application est déjà configurée pour fonctionner avec Neon en production sur Render.

## ✅ Configuration actuelle

- **Backend**: Render (https://nextgendev-n85n.onrender.com)
- **Base de données**: Neon PostgreSQL (déjà configurée)
- **Fallback API**: Votre app bascule automatiquement vers Render si localhost ne répond pas

Voir dans `docs/js/api.js`:
```javascript
let API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
  ? 'http://localhost:5000/api'
  : 'https://nextgendev-n85n.onrender.com/api';
```

## 🚀 Pour re-déployer après des modifications

Si vous avez fait des changements (ajout de champs, nouvelles routes, etc.):

### 1. Committez vos changements

```bash
git add .
git commit -m "describe your changes"
git push origin main
```

### 2. Render re-déploiera automatiquement

- Allez sur render.com/dashboard
- Votre app re-build et re-déploie automatiquement
- Attendez 2-3 minutes

### 3. Vérifiez que tout fonctionne

```bash
curl https://nextgendev-n85n.onrender.com/api/settings
```

## 🔐 Variables d'environnement sur Render

Votre DATABASE_URL est déjà défini dans Render:
- Environment > Environment variables
- DATABASE_URL = `postgresql://...@neon.tech/...`

## ⚠️ Important: Migrations en production

Si vous avez modifié les modèles (ajout de champs):

```bash
# Localement:
python db.py init   # Crée/met à jour les tables localement

# Sur Render:
# 1. Le déploiement va relancer l'app
# 2. Les tables se créent automatiquement du fait que app.py lance db.create_all() au démarrage
# 3. Vérifiez: curl https://nextgendev-...onrender.com/api/settings
```

## 📊 Monitoring Neon en production

Allez sur https://console.neon.tech/:
- Metrics > CPU, Memory usage
- Logs > Pour les requêtes
- Connections > Activer/désactiver pooling

## 🆘 Erreurs couantes en production

### "502 Bad Gateway"
→ Render app crashée
- Vérifiez les logs: Render > Logs
- Vérifiez DATABASE_URL: doit finir par `neondb`

### "Connection refused"
→ Neon n'est pas accessible
- Vérifiez que Render peut accéder à Neon (IP whitelisting)
- Neon > Settings > Network > Auto-whitelist

### "No space left on device"
→ Disque plein sur Render
- Render = 0.5 GB gratuit
- C'est normal, le disque est pour les logs seulement

## ✨ Optimisations recommandées

```python
# Dans app.py, remplacer debug=True par False en production:
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🔄 Pipeline de déploiement

```
Local (venv + Neon)
        ↓
    git push
        ↓
    GitHub
        ↓
    Render webhook
        ↓
    Build & Deploy (pip install -r requirements.txt)
        ↓
    Redirection: localhost → https://nextgendev-n85n.onrender.com
        ↓
    Production! 🎉
```

## 📱 Points de contact

- **API**: https://nextgendev-n85n.onrender.com/api
- **Frontend**: https://nextgendev-n85n.onrender.com/docs
- **Login**: https://nextgendev-n85n.onrender.com/docs/login.html
- **Dashboard**: https://nextgendev-n85n.onrender.com/docs/dashboard/index.html

## 🎯 Checklist déploiement

Avant de pousser en production:

- [ ] Tests locaux sur `localhost:5000` ✓
- [ ] Base de données à jour: `python db.py init` ✓
- [ ] Variables d'env dans Render ✓
- [ ] Pas de secrets dans le code (utiliser .env) ✓
- [ ] `requirements.txt` à jour: `pip freeze > requirements.txt` ✓
- [ ] `git push` depuis branche `main` ✓

Après déploiement:

- [ ] Tester l'API: `curl https://nextgendev-n85n.onrender.com/api/settings`
- [ ] Vérifier le login: https://nextgendev-n85n.onrender.com/docs/login.html
- [ ] Vérifier la page contact avec le numéro WhatsApp ✓

---

**Note**: Render ferme les apps inactives après 15 minutes. Votre app va relancer la prochaine fois que quelqu'un la visite (démarrage 30-50 secondes).

Pour empêcher ça → passer à un plan payant (gratuit = acceptable pour démo/test).
