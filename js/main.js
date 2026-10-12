/* ==========================================================================
   CracksTube Official - Fast Interactivity & Utility Script (Vanilla JS)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const toggleBtn = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (toggleBtn && navMenu) {
    toggleBtn.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      const isOpened = navMenu.classList.contains('open');
      toggleBtn.setAttribute('aria-expanded', isOpened);
    });
  }

  // FAQ Accordion
  const faqHeaders = document.querySelectorAll('.faq-header');
  
  faqHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const faqItem = header.parentElement;
      const isOpen = faqItem.classList.contains('active');

      // Close other open items
      document.querySelectorAll('.faq-item.active').forEach(item => {
        if (item !== faqItem) {
          item.classList.remove('active');
          item.querySelector('.faq-header').setAttribute('aria-expanded', 'false');
        }
      });

      // Toggle current item
      faqItem.classList.toggle('active');
      header.setAttribute('aria-expanded', !isOpen);
    });
  });

  // Highlight Current Page Link in Nav
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Table of Contents Smooth Scroll Link Handler
  document.addEventListener('click', (e) => {
    const link = e.target.closest('.toc-box a[href*="#"]');
    if (link) {
      const href = link.getAttribute('href');
      const hashIndex = href.indexOf('#');
      if (hashIndex !== -1) {
        const targetId = href.substring(hashIndex + 1);
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          e.preventDefault();
          targetEl.scrollIntoView({ behavior: 'smooth' });
          if (history.pushState) {
            history.pushState(null, '', '#' + targetId);
          }
        }
      }
    }
  });

  // Contact form submission handling
  const contactForm = document.querySelector('#contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const feedback = document.querySelector('#formFeedback');
      if (feedback) {
        feedback.style.display = 'block';
        feedback.innerHTML = '<div style="padding:1rem; background:rgba(2, 132, 199, 0.12); border:1px solid var(--accent-cyan); color:var(--text-main); border-radius:8px; font-weight:600;">✅ Thank you for your inquiry! Your message has been received. Our editorial team will review your submission and reply via email to your provided address.</div>';
        contactForm.reset();
      }
    });
  }
});

// Global Table of Contents Toggle Function
window.toggleToc = function(btn, e) {
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  if (!btn) return;
  const container = btn.closest('.toc-box');
  if (!container) return;
  const list = container.querySelector('.toc-list');
  if (!list) return;

  const isExpanded = container.classList.toggle('expanded');
  btn.textContent = isExpanded ? '[hide]' : '[show]';
  btn.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');

  if (isExpanded) {
    list.style.maxHeight = (list.scrollHeight + 50) + 'px';
    list.style.opacity = '1';
  } else {
    list.style.maxHeight = '0px';
    list.style.opacity = '0';
  }
};

window.toggleTocHeader = function(header, e) {
  if (e && e.target.closest('.toc-toggle-btn')) return;
  const btn = header.querySelector('.toc-toggle-btn');
  if (btn) {
    window.toggleToc(btn, e);
  }
};
