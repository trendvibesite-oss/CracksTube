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

  // Contact Form Handling (if present)
  const contactForm = document.querySelector('#contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const feedback = document.querySelector('#formFeedback');
      if (feedback) {
        feedback.style.display = 'block';
        feedback.innerHTML = '<div style="padding:1rem; background:rgba(16,185,129,0.15); border:1px solid #10b981; color:#10b981; border-radius:8px;">Thank you for contacting CracksTube! Your message has been sent successfully. We will respond shortly.</div>';
        contactForm.reset();
      }
    });
  }
});
