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

  // Backup event listener for contact form
  const contactForm = document.querySelector('#contactForm');
  if (contactForm && typeof window.sendToWhatsApp === 'function') {
    contactForm.addEventListener('submit', window.sendToWhatsApp);
  }
});
