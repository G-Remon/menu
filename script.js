// Theme Switcher
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const savedTheme = localStorage.getItem('salim-theme') || 'dark';
body.setAttribute('data-theme', savedTheme);

themeToggle.addEventListener('click', () => {
  const currentTheme = body.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  body.setAttribute('data-theme', newTheme);
  localStorage.setItem('salim-theme', newTheme);
});

// Language Switcher
const langToggle = document.getElementById('langToggle');
const html = document.documentElement;
const savedLang = localStorage.getItem('salim-lang') || 'ar';
setLanguage(savedLang);

langToggle.addEventListener('click', () => {
  const currentLang = html.getAttribute('lang');
  const newLang = currentLang === 'ar' ? 'en' : 'ar';
  setLanguage(newLang);
});

function setLanguage(lang) {
  html.setAttribute('lang', lang);
  html.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
  localStorage.setItem('salim-lang', lang);
}

// Intersection Observer optimized
const sections = document.querySelectorAll('.section');
const observer = new IntersectionObserver((entries, obs) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      obs.unobserve(entry.target); // Unobserve to save performance
    }
  });
}, { threshold: 0.05 });

sections.forEach(section => observer.observe(section));

// Active Navigation Highlight
const navItems = document.querySelectorAll('.nav-item');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= sectionTop - 150) {
      current = section.getAttribute('id');
    }
  });

  navItems.forEach(item => {
    item.classList.remove('active');
    if (item.getAttribute('href').includes(current)) {
      item.classList.add('active');
    }
  });
  
  const scrollTopBtn = document.getElementById('scrollTop');
  if (window.pageYOffset > 400) {
    scrollTopBtn.classList.add('visible');
  } else {
    scrollTopBtn.classList.remove('visible');
  }
}, { passive: true }); // Passive listener for better scroll performance

// Scroll to Top
document.getElementById('scrollTop').addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});