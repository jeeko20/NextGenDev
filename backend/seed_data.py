import os
import sys
import json
from datetime import datetime, date

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, Portfolio, GalleryImage, Event, BlogPost, Message

def seed_data():
    with app.app_context():
        print("Insertion des données d'exemple...")
        
        # Clear existing data
        Portfolio.query.delete()
        GalleryImage.query.delete()
        Event.query.delete()
        BlogPost.query.delete()
        Message.query.delete()
        db.session.commit()
        
        # ===== PORTFOLIOS =====
        portfolios = [
            {
                'title': 'HAITI-MARKET',
                'description': 'Plateforme e-commerce complète dédiée aux produits locaux haïtiens. Intégration de paiement mobile, gestion des commandes, et tableau de bord administrateur. Un projet qui met en valeur l\'artisanat haïtien.',
                'category': 'Sites Web',
                'technologies': json.dumps(['React', 'Node.js', 'MongoDB', 'Stripe']),
                'image_url': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800',
                'project_url': 'https://haitimarket.ht'
            },
            {
                'title': 'EDUKAY',
                'description': 'Application mobile d\'e-learning conçue pour les étudiants haïtiens. Cours interactifs, quiz en temps réel, et système de suivi de progression. Disponible sur iOS et Android.',
                'category': 'Apps Mobiles',
                'technologies': json.dumps(['Flutter', 'Firebase', 'Dart']),
                'image_url': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800',
                'project_url': 'https://edukay.ht'
            },
            {
                'title': 'GESTOCK PRO',
                'description': 'Logiciel de gestion de stock professionnel pour les PME haïtiennes. Suivi des inventaires en temps réel, rapports automatisés, et alertes de réapprovisionnement.',
                'category': 'Apps Desktop',
                'technologies': json.dumps(['Python', 'Tkinter', 'SQLite', 'Pandas']),
                'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
                'project_url': '#'
            },
            {
                'title': 'Brand ID Studio',
                'description': 'Création d\'identité visuelle complète pour une startup tech haïtienne. Logo, charte graphique, supports de communication, et design system pour applications.',
                'category': 'Design Graphique',
                'technologies': json.dumps(['Figma', 'Adobe Illustrator', 'Adobe Photoshop']),
                'image_url': 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800',
                'project_url': '#'
            },
            {
                'title': 'FESTIVAL KANaval 2024',
                'description': 'Couverture photographique complète du carnaval haïtien 2024. Plus de 500 photos capturées, retouche professionnelle, et livraison d\'un album numérique interactif.',
                'category': 'Photographie',
                'technologies': json.dumps(['Canon EOS R5', 'Lightroom', 'Photoshop']),
                'image_url': 'https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=800',
                'project_url': '#'
            },
            {
                'title': 'AYITI DIGITAL',
                'description': 'Site vitrine institutionnel avec animations avancées et expérience utilisateur immersive. Présentation des initiatives digitales en Haïti avec des visualisations de données interactives.',
                'category': 'Sites Web',
                'technologies': json.dumps(['HTML5', 'CSS3', 'JavaScript', 'GSAP', 'Three.js']),
                'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800',
                'project_url': 'https://ayitidigital.ht'
            }
        ]
        
        for p_data in portfolios:
            portfolio = Portfolio(**p_data)
            db.session.add(portfolio)
        
        db.session.commit()
        print(f"  {len(portfolios)} portfolios ajoutés")
        
        # ===== GALLERY IMAGES =====
        gallery_images = [
            {
                'title': 'Session brainstorming',
                'category': 'Équipe',
                'image_url': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800',
                'description': 'Séance de brainstorming pour le projet EDUKAY'
            },
            {
                'title': 'Coding night',
                'category': 'Développement',
                'image_url': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800',
                'description': 'Session de code nocturne pendant le hackathon'
            },
            {
                'title': 'Présentation projet',
                'category': 'Événements',
                'image_url': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=800',
                'description': 'Présentation du projet HAITI-MARKET aux investisseurs'
            },
            {
                'title': 'Atelier design UI/UX',
                'category': 'Workshop',
                'image_url': 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800',
                'description': 'Workshop sur les principes du design d\'interface'
            },
            {
                'title': 'Équipe NextGen Dev',
                'category': 'Équipe',
                'image_url': 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800',
                'description': 'Photo officielle de l\'équipe NextGen Dev'
            },
            {
                'title': 'Hackathon USFAS 2024',
                'category': 'Compétition',
                'image_url': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800',
                'description': 'Participation au hackathon de l\'université'
            },
            {
                'title': 'Campus USFAS',
                'category': 'Université',
                'image_url': 'https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800',
                'description': 'Le campus de l\'Université Saint François d\'Assise'
            },
            {
                'title': 'Cérémonie de remise des prix',
                'category': 'Événements',
                'image_url': 'https://images.unsplash.com/photo-1558603668-6570496b66f8?w=800',
                'description': 'Cérémonie de remise des prix du concours de programmation'
            }
        ]
        
        for g_data in gallery_images:
            image = GalleryImage(**g_data)
            db.session.add(image)
        
        db.session.commit()
        print(f"  {len(gallery_images)} images de galerie ajoutées")
        
        # ===== EVENTS =====
        events = [
            {
                'title': 'Workshop React Avancé',
                'description': 'Atelier pratique de 4 heures sur les hooks avancés, le state management avec Redux Toolkit, et les performances dans React. Ouvert à tous les niveaux intermédiaires et avancés.',
                'date': date(2024, 4, 20),
                'time': '14:00',
                'location': 'Salle Informatique USFAS, Delmas 33',
                'image_url': 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800',
                'status': 'À venir'
            },
            {
                'title': 'Hackathon NextGen 2024',
                'description': '48 heures de création intensive pour développer une solution innovante aux problématiques locales. Prix en espèces et opportunités d\'incubation pour les gagnants.',
                'date': date(2024, 5, 15),
                'time': '09:00',
                'location': 'Campus USFAS, Port-au-Prince',
                'image_url': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800',
                'status': 'À venir'
            },
            {
                'title': 'Meetup Tech Haïti',
                'description': 'Rencontre mensuelle avec des professionnels de la tech haïtienne. Échanges, networking, et présentations de projets innovants du secteur.',
                'date': date(2024, 3, 10),
                'time': '16:00',
                'location': 'Auditorium USFAS',
                'image_url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800',
                'status': 'Terminé'
            },
            {
                'title': 'Formation UI/UX Design',
                'description': 'Formation complète sur les principes du design d\'interface utilisateur. Wireframing, prototypage, tests utilisateurs, et outils modernes comme Figma.',
                'date': date(2024, 2, 5),
                'time': '10:00',
                'location': 'Labo Design USFAS',
                'image_url': 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800',
                'status': 'Terminé'
            }
        ]
        
        for e_data in events:
            event = Event(**e_data)
            db.session.add(event)
        
        db.session.commit()
        print(f"  {len(events)} événements ajoutés")
        
        # ===== BLOG POSTS =====
        blog_posts = [
            {
                'title': 'Pourquoi choisir Flutter en 2024 ?',
                'slug': 'pourquoi-choisir-flutter-2024',
                'category': 'Mobile',
                'excerpt': 'Flutter continue de dominer le développement cross-platform avec sa performance native et son écosystème croissant. Découvrez pourquoi c\'est le choix idéal pour votre prochaine application mobile.',
                'content': '''<p>Flutter, le framework de Google, a révolutionné le développement d'applications mobiles ces dernières années. En 2024, il s'affirme comme le choix privilégié pour le développement cross-platform.</p>
                
<h2>Performance native</h2>
<p>Contrairement aux autres solutions cross-platform, Flutter compile directement en code machine natif. Cela garantit des performances équivalentes aux applications développées en Swift ou Kotlin.</p>

<h2>Hot Reload ultra-rapide</h2>
<p>Le Hot Reload de Flutter permet de voir les modifications instantanément, sans perdre l'état de l'application. Un gain de temps considérable pour les développeurs.</p>

<h2>Un écosystème riche</h2>
<p>Avec des milliers de packages disponibles sur pub.dev, Flutter offre des solutions pour pratiquement tous les besoins : authentification, paiement, cartes, notifications push...</p>

<h2>Conclusion</h2>
<p>Pour votre prochain projet mobile, Flutter est sans doute le meilleur compromis entre qualité, performance et rapidité de développement.</p>''',
                'featured_image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800',
                'status': 'published'
            },
            {
                'title': 'L\'impact de la tech en Haïti',
                'slug': 'impact-tech-haiti',
                'category': 'Technologie',
                'excerpt': 'Comment les solutions digitales transforment le quotidien des Haïtiens et ouvrent de nouvelles opportunités économiques et sociales dans le pays.',
                'content': '''<p>La technologie représente une opportunité sans précédent pour Haïti. Dans un contexte où les infrastructures traditionnelles peinent à se développer, le numérique offre des solutions innovantes.</p>

<h2>L'agriculture intelligente</h2>
<p>Des applications mobiles permettent aux agriculteurs d'accéder aux prévisions météorologiques, aux prix du marché et aux conseils agronomiques en temps réel.</p>

<h2>L'éducation en ligne</h2>
<p>Les plateformes d'e-learning démocratisent l'accès à l'éducation de qualité, même dans les zones les plus reculées du pays.</p>

<h2>La finance mobile</h2>
<p>Les solutions de paiement mobile facilitent les transactions et réduisent la dépendance au cash, améliorant ainsi la sécurité et la traçabilité.</p>

<h2>Conclusion</h2>
<p>La tech en Haïti n'est pas une option de luxe, mais une nécessité pour accélérer le développement du pays.</p>''',
                'featured_image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800',
                'status': 'published'
            },
            {
                'title': 'Guide du débutant en React',
                'slug': 'guide-debutant-react',
                'category': 'Tutoriel',
                'excerpt': 'Tout ce que vous devez savoir pour commencer avec React : composants, props, state, hooks, et bonnes pratiques pour bien débuter votre parcours.',
                'content': '''<p>React est devenu incontournable dans le développement web moderne. Ce guide vous accompagne dans vos premiers pas avec cette bibliothèque.</p>

<h2>Qu'est-ce que React ?</h2>
<p>React est une bibliothèque JavaScript développée par Facebook pour construire des interfaces utilisateur. Elle se base sur le concept de composants réutilisables.</p>

<h2>Les composants</h2>
<p>Les composants sont les briques de base d'une application React. Ils peuvent être des fonctions ou des classes, et retournent du JSX qui décrit l'interface.</p>

<h2>Le state et les props</h2>
<p>Les props permettent de passer des données d'un composant parent à un composant enfant. Le state gère les données qui changent au sein d'un composant.</p>

<h2>Les Hooks</h2>
<p>Les Hooks, introduits avec React 16.8, permettent d'utiliser le state et d'autres fonctionnalités React dans les composants fonctions.</p>

<h2>Conclusion</h2>
<p>Avec ces bases, vous êtes prêts à construire vos premières applications React. Pratiquez régulièrement et n'hésitez pas à consulter la documentation officielle.</p>''',
                'featured_image': 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800',
                'status': 'published'
            },
            {
                'title': 'La photographie avec votre smartphone',
                'slug': 'photographie-smartphone',
                'category': 'Photographie',
                'excerpt': 'Capturer des photos professionnelles avec votre smartphone : techniques, applications, et astuces pour des résultats époustouflants.',
                'content': '''<p>Les smartphones d'aujourd'hui offrent des capacités photographiques impressionnantes. Voici comment en tirer le meilleur parti.</p>

<h2>Maîtriser la lumière</h2>
<p>La lumière est l'élément clé d'une bonne photo. Privilégiez la lumière naturelle, évitez le contre-jour, et utilisez l'heure dorée pour des résultats magiques.</p>

<h2>La composition</h2>
<p>Appliquez la règle des tiers, utilisez les lignes directrices, et pensez à l'équilibre visuel de votre image avant de déclencher.</p>

<h2>Les applications recommandées</h2>
<p>Lightroom Mobile, Snapseed, et VSCO sont des applications gratuites qui transforment votre smartphone en studio de retouche professionnel.</p>

<h2>Conclusion</h2>
<p>Le meilleur appareil photo est celui que vous avez toujours avec vous. Apprenez à maîtriser votre smartphone pour ne plus manquer aucun moment.</p>''',
                'featured_image': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800',
                'status': 'published'
            }
        ]
        
        for b_data in blog_posts:
            post = BlogPost(**b_data)
            db.session.add(post)
        
        db.session.commit()
        print(f"  {len(blog_posts)} articles de blog ajoutés")
        
        # ===== MESSAGES =====
        messages = [
            {
                'name': 'Jean-Pierre Michel',
                'email': 'jp.michel@example.com',
                'subject': 'Projet site vitrine',
                'message': 'Bonjour NextGen Dev, j\'aimerais créer un site vitrine pour ma boutique de vêtements à Delmas. Pouvons-nous discuter de mon projet ?',
                'status': 'unread'
            },
            {
                'name': 'Marie-Louise Joseph',
                'email': 'ml.joseph@example.com',
                'subject': 'Application mobile',
                'message': 'Je souhaiterais développer une application de livraison de repas pour Port-au-Prince. Est-ce dans vos compétences ? Merci !',
                'status': 'unread'
            },
            {
                'name': 'Patrick Lucien',
                'email': 'patrick.l@example.com',
                'subject': 'Design graphique',
                'message': 'J\'ai besoin d\'un logo et d\'une charte graphique pour mon entreprise de construction. Quels sont vos tarifs ?',
                'status': 'read'
            }
        ]
        
        for m_data in messages:
            msg = Message(**m_data)
            db.session.add(msg)
        
        db.session.commit()
        print(f"  {len(messages)} messages ajoutés")
        
        print("\nDonnées d'exemple insérées avec succès!")
        print("\nCompte admin par défaut:")
        print("  Email: admin@nextgendev.ht")
        print("  Mot de passe: admin123")

if __name__ == '__main__':
    seed_data()
