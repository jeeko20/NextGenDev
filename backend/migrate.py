#!/usr/bin/env python
"""
Script de migration pour Neon PostgreSQL
Usage:
  python migrate.py init   - Initialiser les migrations
  python migrate.py create - Créer une nouvelle migration
  python migrate.py upgrade - Appliquer les migrations
"""
import os
import sys
import subprocess
from flask_migrate import Migrate
from app import app, db

# Initialiser Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1]
    
    # Assurer que FLASK_APP est défini
    os.environ.setdefault('FLASK_APP', 'app.py')
    
    if command == 'init':
        print("Initialisation des migrations...")
        result = subprocess.run(['flask', '--app', 'app', 'db', 'init'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Migrations initialisées dans le dossier 'migrations/'")
        else:
            print("Erreur lors de l'initialisation:")
            print(result.stderr)
    
    elif command == 'create':
        message = sys.argv[2] if len(sys.argv) > 2 else "auto migration"
        print(f"Création d'une nouvelle migration: {message}")
        result = subprocess.run(['flask', '--app', 'app', 'db', 'migrate', '-m', message], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Nouvelle migration créée")
        else:
            print("Erreur lors de la création:")
            print(result.stderr)
    
    elif command == 'upgrade':
        print("Application des migrations...")
        result = subprocess.run(['flask', '--app', 'app', 'db', 'upgrade'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Migrations appliquées")
        else:
            print("Erreur lors de l'application:")
            print(result.stderr)
    
    else:
        print(f"Commande inconnue: {command}")
        print(__doc__)
        sys.exit(1)
