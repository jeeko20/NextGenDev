#!/usr/bin/env python
"""
Script pour tester la connexion à Neon PostgreSQL
"""
from app import app, db
from sqlalchemy import text, inspect
import os

def test_connection():
    """Tester la connexion à la base de données"""
    print("🔍 Test de connexion à Neon PostgreSQL...\n")
    
    # Vérifier que DATABASE_URL est configuré
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        print("✗ DATABASE_URL non trouvé dans .env")
        print("  Veuillez créer un fichier .env avec votre DATABASE_URL")
        return False
    
    print(f"📍 Database URL: {db_url[:50]}...")
    
    try:
        with app.app_context():
            # Essayer une requête simple
            result = db.session.execute(text('SELECT 1'))
            print("✓ Connexion réussie à Neon PostgreSQL!")
            
            # Vérifier les tables
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            if not tables:
                print("\n⚠️  Aucune table n'existe dans la base")
                print("  Exécutez: python db.py init")
            else:
                print(f"\n✓ Tables trouvées: {', '.join(tables)}")
            
            return True
            
    except Exception as e:
        print(f"✗ Erreur de connexion: {str(e)}")
        print("\nVérifications à faire:")
        print("  1. Vérifiez que .env contient DATABASE_URL correct")
        print("  2. Vérifiez que votre IP est autorisée sur Neon")
        print("  3. Vérifiez la syntaxe: postgresql://user:password@host/dbname")
        return False

if __name__ == '__main__':
    success = test_connection()
    exit(0 if success else 1)
