// ========================================
// NextGen Dev - Utilities
// ========================================

const Utils = {
  // Toast notifications
  toast(message, type = 'success') {
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    const icons = {
      success: '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
      error: '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
      warning: '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
    };
    
    toast.innerHTML = `${icons[type] || icons.success}<span>${message}</span>`;
    container.appendChild(toast);
    
    setTimeout(() => toast.remove(), 4000);
  },
  
  // Format date
  formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    });
  },
  
  // Format date short
  formatDateShort(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'short'
    });
  },
  
  // Truncate text
  truncate(text, length = 100) {
    if (!text || text.length <= length) return text;
    return text.substring(0, length) + '...';
  },
  
  // Create slug from text
  slugify(text) {
    return text
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9\s-]/g, '')
      .replace(/\s+/g, '-')
      .substring(0, 100);
  },
  
  // Debounce function
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  },
  
  // Show loading spinner
  showLoading(container) {
    container.innerHTML = '<div class="spinner" style="margin: 40px auto;"></div>';
  },
  
  // Show empty state
  showEmpty(container, message = 'Aucun contenu') {
    container.innerHTML = `
      <div style="text-align: center; padding: 60px 20px; color: var(--gris-texte);">
        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 16px; opacity: 0.5;"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="9" x2="15" y2="9"/><line x1="9" y1="13" x2="15" y2="13"/></svg>
        <p>${message}</p>
      </div>
    `;
  },
  
  // Generate random ID
  randomId(prefix = 'id') {
    return `${prefix}_${Math.random().toString(36).substring(2, 9)}`;
  },
  
  // Escape HTML
  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  },

  // Unified Lightbox
  Lightbox: {
    images: [],
    currentIndex: 0,
    
    init() {
      if (document.getElementById('utils-lightbox')) return;
      
      const html = `
        <div id="utils-lightbox" class="lightbox-overlay" aria-hidden="true">
          <button class="lightbox-close" id="utils-lightbox-close" aria-label="Fermer">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
          <div class="lightbox-content">
            <button class="lightbox-nav lightbox-prev" id="utils-lightbox-prev" aria-label="Précédent">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
            </button>
            <div class="lightbox-image-wrapper">
              <img src="" alt="" id="utils-lightbox-image">
            </div>
            <button class="lightbox-nav lightbox-next" id="utils-lightbox-next" aria-label="Suivant">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
          </div>
          <div class="lightbox-caption" id="utils-lightbox-caption"></div>
        </div>
      `;
      
      const div = document.createElement('div');
      div.innerHTML = html;
      document.body.appendChild(div.firstElementChild);
      
      // Events
      document.getElementById('utils-lightbox-close').onclick = () => this.close();
      document.getElementById('utils-lightbox-prev').onclick = (e) => { e.stopPropagation(); this.prev(); };
      document.getElementById('utils-lightbox-next').onclick = (e) => { e.stopPropagation(); this.next(); };
      document.getElementById('utils-lightbox').onclick = (e) => {
        if (e.target.id === 'utils-lightbox' || e.target.classList.contains('lightbox-image-wrapper')) {
          this.close();
        }
      };
      
      document.addEventListener('keydown', (e) => {
        if (!document.getElementById('utils-lightbox').classList.contains('active')) return;
        if (e.key === 'Escape') this.close();
        if (e.key === 'ArrowLeft') this.prev();
        if (e.key === 'ArrowRight') this.next();
      });
    },
    
    open(images, index = 0) {
      this.init();
      this.images = images.map(img => typeof img === 'string' ? { url: img, title: '' } : img);
      this.currentIndex = index;
      this.update();
      
      const el = document.getElementById('utils-lightbox');
      el.classList.add('active');
      el.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    },
    
    close() {
      const el = document.getElementById('utils-lightbox');
      if (el) {
        el.classList.remove('active');
        el.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    },
    
    update() {
      const img = this.images[this.currentIndex];
      const imgEl = document.getElementById('utils-lightbox-image');
      const captionEl = document.getElementById('utils-lightbox-caption');
      const prevBtn = document.getElementById('utils-lightbox-prev');
      const nextBtn = document.getElementById('utils-lightbox-next');
      
      imgEl.src = img.url || img.image_url;
      imgEl.alt = img.title || img.alt_text || 'Lightbox image';
      captionEl.textContent = (img.title || img.alt_text || '') + (this.images.length > 1 ? ` (${this.currentIndex + 1}/${this.images.length})` : '');
      
      if (this.images.length <= 1) {
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
      } else {
        prevBtn.style.display = 'flex';
        nextBtn.style.display = 'flex';
      }
    },
    
    next() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.update();
    },
    
    prev() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.update();
    }
  }
};

window.Utils = Utils;
