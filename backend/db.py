#!/usr/bin/env python
"""
Script simple pour gérer la base de données
"""
import os
import sys
from app import app, db
from models import User, Portfolio, GalleryImage, Event, BlogPost, Message, SiteSettings
from werkzeug.security import generate_password_hash

def init_db():
    """Créer toutes les tables"""
    with app.app_context():
        print("Création des tables...")
        db.create_all()
        print("✓ Tables créées avec succès!")

def drop_db():
    """Supprimer toutes les tables (DANGER!)"""
    with app.app_context():
        response = input("⚠️  Cela va SUPPRIMER toutes les données. Êtes-vous certain? (oui/non): ")
        if response.lower() == 'oui':
            print("Suppression des tables...")
            db.drop_all()
            print("✓ Tables supprimées!")
        else:
            print("Annulé")

def reset_db():
    """Réinitialiser la base (supprimer + recréer)"""
    with app.app_context():
        response = input("⚠️  Cela va RÉINITIALISER la base. Êtes-vous certain? (oui/non): ")
        if response.lower() == 'oui':
            print("Suppression des tables...")
            db.drop_all()
            print("Création des tables...")
            db.create_all()
            print("✓ Base de données réinitialisée!")
        else:
            print("Annulé")

def create_admin():
    """Créer un utilisateur admin"""
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        
        if admin:
            print("✗ Un admin 'admin' existe déjà")
            return
        
        print("\n--- Création d'un compte admin ---")
        username = input("Nom d'utilisateur: ").strip()
        email = input("Email: ").strip()
        password = input("Mot de passe: ").strip()
        name = input("Nom complet: ").strip() or 'Admin'
        
        if User.query.filter_by(username=username).first():
            print("✗ Ce nom d'utilisateur existe déjà")
            return
        
        if User.query.filter_by(email=email).first():
            print("✗ Cet email existe déjà")
            return
        
        admin = User(
            username=username,
            email=email,
            name=name,
            password_hash=generate_password_hash(password),
            role='admin'
        )
        
        db.session.add(admin)
        db.session.commit()
        
        print(f"\n✓ Admin créé avec succès!")
        print(f"  Nom d'utilisateur: {username}")
        print(f"  Email: {email}")

def show_users():
    """Lister tous les utilisateurs"""
    with app.app_context():
        users = User.query.all()
        
        if not users:
            print("Aucun utilisateur trouvé")
            return
        
        print("\n--- Utilisateurs ---")
        for user in users:
            print(f"  ID: {user.id}")
            print(f"    Username: {user.username}")
            print(f"    Email: {user.email}")
            print(f"    Nom: {user.name}")
            print(f"    Rôle: {user.role}")
            print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Commandes disponibles:")
        print("  python db.py init        - Créer les tables")
        print("  python db.py drop        - Supprimer toutes les tables (DANGER!)")
        print("  python db.py reset       - Réinitialiser la base (DANGER!)")
        print("  python db.py admin       - Créer un utilisateur admin")
        print("  python db.py users       - Lister tous les utilisateurs")
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == 'init':
        init_db()
    elif command == 'drop':
        drop_db()
    elif command == 'reset':
        reset_db()
    elif command == 'admin':
        create_admin()
    elif command == 'users':
        show_users()
    else:
        print(f"Commande inconnue: {command}")
        sys.exit(1)
