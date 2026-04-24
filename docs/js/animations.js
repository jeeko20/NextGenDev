// ========================================
// NextGen Dev - Animations
// ========================================

const Animations = {
  // Page loader
  initPageLoader() {
    const loader = document.querySelector('.page-loader');
    if (!loader) return;
    
    window.addEventListener('load', () => {
      setTimeout(() => {
        loader.classList.add('hidden');
        setTimeout(() => loader.remove(), 500);
      }, 800);
    });
  },
  
  // Navigation scroll effect
  initNavScroll() {
    const nav = document.querySelector('.nav');
    if (!nav) return;
    
    window.addEventListener('scroll', () => {
      if (window.scrollY > 100) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    });
  },
  
  // Initialize Lottie animations
  initLottie() {
    const containers = document.querySelectorAll('[data-lottie]');
    containers.forEach(container => {
      const path = container.dataset.lottie;
      const loop = container.dataset.lottieLoop !== 'false';
      
      if (typeof lottie !== 'undefined' && path) {
        lottie.loadAnimation({
          container,
          renderer: 'svg',
          loop,
          autoplay: true,
          path
        });
      }
    });
  },
  
  // GSAP ScrollTrigger animations
  initScrollAnimations() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
    
    // Small delay to ensure DOM is ready
    setTimeout(() => {
      gsap.registerPlugin(ScrollTrigger);
    
    // Fade in sections
    const sections = document.querySelectorAll('[data-animate]');
    sections.forEach(section => {
      const animation = section.dataset.animate || 'fadeUp';
      
      const configs = {
        fadeUp: { y: 60 },
        fadeLeft: { x: -60 },
        fadeRight: { x: 60 },
        fadeIn: {},
        scale: { scale: 0.9 }
      };
      
      gsap.fromTo(section, 
        { opacity: 0, ...configs[animation] },
        {
          opacity: 1,
          y: 0,
          x: 0,
          scale: 1,
          duration: 0.8,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: section,
            start: 'top 80%',
            toggleActions: 'play none none none'
          }
        }
      );
    });
    
    // Stagger cards
    const grids = document.querySelectorAll('[data-stagger]');
    grids.forEach(grid => {
      const children = grid.children;
      gsap.fromTo(children, 
        { y: 40, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.6,
          stagger: 0.1,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: grid,
            start: 'top 80%'
          }
        }
      );
    });
    }, 100);
  },
  
  // Counter animation for stats
  animateCounters() {
    const counters = document.querySelectorAll('[data-counter]');
    
    counters.forEach(counter => {
      const target = parseInt(counter.dataset.counter);
      const duration = 2000;
      const step = target / (duration / 16);
      let current = 0;
      
      const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          const update = () => {
            current += step;
            if (current < target) {
              counter.textContent = Math.floor(current) + '+';
              requestAnimationFrame(update);
            } else {
              counter.textContent = target + '+';
            }
          };
          update();
          observer.disconnect();
        }
      });
      
      observer.observe(counter);
    });
  },
  
  // Smooth scroll for anchor links
  initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        // Skip empty or invalid selectors
        if (!href || href === '#' || href.startsWith('http')) return;
        
        e.preventDefault();
        try {
          const target = document.querySelector(href);
          if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        } catch (err) {
          // Invalid selector, skip
        }
      });
    });
  },
  
  // Hero animations
  initHeroAnimations() {
    if (typeof gsap === 'undefined') return;
    
    const heroLabel = document.querySelector('.hero-label');
    const heroTitle = document.querySelector('.hero-title');
    const heroSubtitle = document.querySelector('.hero-subtitle');
    const heroCta = document.querySelector('.hero-cta');
    const statsBar = document.querySelector('.stats-bar');
    
    const tl = gsap.timeline({ delay: 0.3 });
    
    if (heroLabel) {
      tl.from(heroLabel, { y: 20, opacity: 0, duration: 0.6, ease: 'power3.out' });
    }
    if (heroTitle) {
      tl.from(heroTitle, { y: 30, opacity: 0, duration: 0.8, ease: 'power3.out' }, '-=0.3');
    }
    if (heroSubtitle) {
      tl.from(heroSubtitle, { y: 20, opacity: 0, duration: 0.6, ease: 'power3.out' }, '-=0.4');
    }
    if (heroCta) {
      tl.from(heroCta, { y: 20, opacity: 0, duration: 0.6, ease: 'power3.out' }, '-=0.3');
    }
    if (statsBar) {
      tl.from(statsBar, { y: 20, opacity: 0, duration: 0.6, ease: 'power3.out' }, '-=0.3');
    }
  },
  
  // Initialize all animations
  init() {
    this.initPageLoader();
    this.initNavScroll();
    this.initLottie();
    this.initScrollAnimations();
    this.animateCounters();
    this.initSmoothScroll();
    this.initHeroAnimations();
  }
};

window.Animations = Animations;
