// ========================================
// NextGen Dev - Main Script
// ========================================

// Patch de Lucide pour éviter que les icônes (ex: bottom-nav) ne disparaissent
// lors du re-rendu asynchrone des autres éléments sur la page
if (typeof lucide !== 'undefined' && !lucide.__patched) {
  const originalCreateIcons = lucide.createIcons;
  lucide.createIcons = function(options) {
    originalCreateIcons(options);
    // On retire l'attribut pour que Lucide ne tente pas de remplacer un SVG par un SVG vide au prochain appel
    document.querySelectorAll('svg[data-lucide]').forEach(el => el.removeAttribute('data-lucide'));
  };
  lucide.__patched = true;
}

document.addEventListener('DOMContentLoaded', () => {
  // Define components first
  defineNavComponent();
  defineFooterComponent();

  // Initialize Lucide icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
  
  // Initialize animations
  if (window.Animations) {
    Animations.init();
  }
  
  // Initialize auth UI
  if (window.Auth) {
    Auth.updateUI();
  }
  
  // Initialize navigations
  initBottomNav();
  initMobileMenu();
  setActiveNav();
});

// Bottom Navigation
function initBottomNav() {
  const bottomNavItems = document.querySelectorAll('.bottom-nav-item[data-page]');
  bottomNavItems.forEach(item => {
    item.addEventListener('click', () => {
      const page = item.dataset.page;
      if (page === 'menu') {
        toggleBottomMenu();
      } else {
        window.location.href = page;
      }
    });
  });
}

// Mobile Menu Overlay
function initMobileMenu() {
  const overlay = document.querySelector('.bottom-nav-overlay');
  const closeBtn = document.querySelector('.bottom-nav-menu-close');
  
  if (overlay) {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        toggleBottomMenu();
      }
    });
  }
  
  if (closeBtn) {
    closeBtn.addEventListener('click', toggleBottomMenu);
  }
}

function toggleBottomMenu() {
  const overlay = document.querySelector('.bottom-nav-overlay');
  const menu = document.querySelector('.bottom-nav-menu');
  
  if (overlay && menu) {
    overlay.classList.toggle('active');
    menu.classList.toggle('active');
  }
}

// Set active navigation based on current page
function setActiveNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  
  // Desktop nav
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
  
  // Bottom nav
  document.querySelectorAll('.bottom-nav-item[data-page]').forEach(item => {
    const page = item.dataset.page;
    if (page === currentPage || (currentPage === '' && page === 'index.html')) {
      item.classList.add('active');
    }
  });
}

function defineNavComponent() {
  const navTemplate = `
    <nav class="nav">
      <div class="nav-inner">
        <a href="index.html" class="nav-logo">NEXTGEN <span>DEV</span></a>
        <ul class="nav-links">
          <li><a href="index.html">Accueil</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="portfolio.html">Portfolio</a></li>
          <li><a href="gallery.html">Galerie</a></li>
          <li><a href="events.html">Événements</a></li>
          <li><a href="blog.html">Blog</a></li>
          <li><a href="about.html">À Propos</a></li>
        </ul>
        <a href="contact.html" class="btn btn-primary">Contact</a>
      </div>
    </nav>
    
    <!-- Bottom Navigation Mobile -->
    <nav class="bottom-nav">
      <ul class="bottom-nav-items">
        <li class="bottom-nav-item" data-page="index.html">
          <i data-lucide="home"></i>
          <span>Accueil</span>
        </li>
        <li class="bottom-nav-item" data-page="services.html">
          <i data-lucide="layers"></i>
          <span>Services</span>
        </li>
        <li class="bottom-nav-item" data-page="portfolio.html">
          <i data-lucide="briefcase"></i>
          <span>Portfolio</span>
        </li>
        <li class="bottom-nav-item" data-page="contact.html">
          <i data-lucide="mail"></i>
          <span>Contact</span>
        </li>
        <li class="bottom-nav-item" data-page="menu">
          <i data-lucide="grid-3x3"></i>
          <span>Menu+</span>
        </li>
      </ul>
    </nav>
    
    <!-- Bottom Nav Menu Overlay -->
    <div class="bottom-nav-overlay">
      <div class="bottom-nav-menu">
        <div class="bottom-nav-menu-header">
          <h3>Menu</h3>
          <div class="bottom-nav-menu-close">
            <i data-lucide="x"></i>
          </div>
        </div>
        <ul class="bottom-nav-menu-items">
          <li><a href="gallery.html" class="bottom-nav-menu-item"><i data-lucide="image"></i><span>Galerie</span></a></li>
          <li><a href="events.html" class="bottom-nav-menu-item"><i data-lucide="calendar"></i><span>Événements</span></a></li>
          <li><a href="blog.html" class="bottom-nav-menu-item"><i data-lucide="file-text"></i><span>Blog</span></a></li>
          <li><a href="about.html" class="bottom-nav-menu-item"><i data-lucide="users"></i><span>À Propos</span></a></li>
          <li><a href="dashboard/index.html" class="bottom-nav-menu-item"><i data-lucide="layout-dashboard"></i><span>Dashboard</span></a></li>
        </ul>
      </div>
    </div>
  `;
  
  // Find nav placeholder and replace
  const navPlaceholder = document.getElementById('nav-placeholder');
  if (navPlaceholder) {
    navPlaceholder.outerHTML = navTemplate;
    if (typeof lucide !== 'undefined') {
      setTimeout(() => lucide.createIcons(), 0);
    }
  }
}

function defineFooterComponent() {
  const footerTemplate = `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <div class="logo">NEXTGEN <span>DEV</span></div>
            <p>Collectif de 5 étudiants développeurs à l'Université Saint François d'Assise d'Haïti, créant des solutions digitales innovantes.</p>
            <div class="footer-social">
              <a href="#" aria-label="Facebook"><i data-lucide="facebook"></i></a>
              <a href="#" aria-label="Instagram"><i data-lucide="instagram"></i></a>
              <a href="#" aria-label="Twitter"><i data-lucide="twitter"></i></a>
              <a href="#" aria-label="LinkedIn"><i data-lucide="linkedin"></i></a>
            </div>
          </div>
          <div class="footer-links">
            <h4>Navigation</h4>
            <ul>
              <li><a href="index.html">Accueil</a></li>
              <li><a href="services.html">Services</a></li>
              <li><a href="portfolio.html">Portfolio</a></li>
              <li><a href="about.html">À Propos</a></li>
            </ul>
          </div>
          <div class="footer-links">
            <h4>Services</h4>
            <ul>
              <li><a href="services.html">Sites Internet</a></li>
              <li><a href="services.html">Apps Mobiles</a></li>
              <li><a href="services.html">Design Graphique</a></li>
              <li><a href="services.html">Photographie</a></li>
            </ul>
          </div>
          <div class="footer-links">
            <h4>Contact</h4>
            <ul>
              <li><a href="contact.html">Nous contacter</a></li>
              <li><a href="blog.html">Blog</a></li>
              <li><a href="events.html">Événements</a></li>
              <li><a href="dashboard/index.html">Admin</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2024 NextGen Dev. Tous droits réservés.</p>
          <p>Université Saint François d'Assise - Delmas 33, Haïti</p>
        </div>
      </div>
    </footer>
  `;
  
  const footerPlaceholder = document.getElementById('footer-placeholder');
  if (footerPlaceholder) {
    footerPlaceholder.outerHTML = footerTemplate;
    if (typeof lucide !== 'undefined') {
      setTimeout(() => lucide.createIcons(), 0);
    }
  }
}
