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

  // Contact Form Handling - WhatsApp Redirection (+91 8200194578)
  const contactForm = document.querySelector('#contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.querySelector('#name')?.value.trim() || '';
      const email = document.querySelector('#email')?.value.trim() || '';
      const subject = document.querySelector('#subject')?.value.trim() || 'General Inquiry';
      const message = document.querySelector('#message')?.value.trim() || '';

      if (!name || !email || !message) {
        alert('Please fill out all required fields.');
        return;
      }

      // Format WhatsApp Message
      const waText = `*New Inquiry from CracksTube Website* 📬\n\n` +
                     `*Name:* ${name}\n` +
                     `*Email:* ${email}\n` +
                     `*Inquiry Type:* ${subject}\n\n` +
                     `*Message:* ${message}`;

      const phone = '918200194578';
      const waUrl = `https://api.whatsapp.com/send?phone=${phone}&text=${encodeURIComponent(waText)}`;

      const feedback = document.querySelector('#formFeedback');
      if (feedback) {
        feedback.style.display = 'block';
        feedback.innerHTML = '<div style="padding:1rem; background:rgba(37, 211, 102, 0.15); border:1px solid #25D366; color:#0e8838; font-weight:600; border-radius:8px; margin-bottom:1rem; display:flex; align-items:center; gap:0.5rem;"><span>✅</span> Opening WhatsApp with your inquiry details...</div>';
      }

      // Open WhatsApp link in new tab / redirect
      setTimeout(() => {
        window.open(waUrl, '_blank');
        contactForm.reset();
      }, 500);
    });
  }
});
