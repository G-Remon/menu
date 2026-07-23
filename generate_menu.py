import json

logo_src = 'image-removebg-preview.png'

menu_data = [
#    {
#        "id": "breakfast",
#        "title_ar": "الإفطار",
#        "title_en": "BREAKFAST",
#        "icon": "🥐",
#        "sub_sections": [
#            {
#                "title_ar": "",
#                "title_en": "",
#                "items": [
#                    {"ar": "كرواسون جبن", "en": "Cheese Croissant", "price": "65"},
#                    {"ar": "كرواسون تركي مع جبن", "en": "Turkey with Cheese Croissant", "price": "95"}
#                ]
#            }
#        ]
#    },
    {
        "id": "hot-drinks",
        "title_ar": "المشروبات الساخنة",
        "title_en": "HOT DRINKS",
        "icon": "☕",
        "sub_sections": [
            {
                "title_ar": "القهوة",
                "title_en": "Coffee",
                "items": [
                    {"ar": "أمريكانو", "en": "Americano", "price": "80"},
                    {"ar": "اسبريسو", "en": "Espresso", "price": "45"},
                    {"ar": "دبل اسبريسو", "en": "Double Espresso", "price": "75"},
                    {"ar": "كابيتشينو زعفران", "en": "Saffron Cappuccino", "price": "95"},
                    {"ar": "ثري كولور", "en": "Three Colors", "price": "70"},
                    {"ar": "لاتيه", "en": "Latte", "price": "70"},
                    {"ar": "كابيتشينو", "en": "Cappuccino", "price": "70"},
                    {"ar": "فلات وايت", "en": "Flat White", "price": "90"},
                    {"ar": "اسبانيش لاتيه", "en": "Spanish Latte", "price": "85"},
                    {"ar": "ميكاتو", "en": "Macchiato", "price": "60"},
                    {"ar": "كورتادو", "en": "Cortado", "price": "65"},
                    {"ar": "بيكولو", "en": "Piccolo", "price": "75"},
                    {"ar": "قهوة تركي", "en": "Turkish Coffee", "price": "35"},
                    {"ar": "قهوة غامق محوج", "en": "Dark Flavored Coffee", "price": "40"},
                    {"ar": "قهوة بندق", "en": "Hazelnut Coffee", "price": "50"},
                    {"ar": "نسكافيه", "en": "Nescafe", "price": "50"},
                    {"ar": "كوفي ميكس", "en": "Coffee Mix", "price": "35"}
                ]
            },
            {
                "title_ar": "مشروبات دافئة",
                "title_en": "Warm Drinks",
                "items": [
                    {"ar": "هوت شوكلت", "en": "Hot Chocolate", "price": "50"},
                    {"ar": "شاي", "en": "Tea", "price": "30"},
                    {"ar": "شاي فلفر", "en": "Flavored Tea", "price": "35"},
                    {"ar": "أعشاب صيدلية", "en": "Pharmacy Herbs", "price": "55"},
                    {"ar": "هوت سيدر", "en": "Hot Cider", "price": "50"},
                    {"ar": "سحلب", "en": "Sahlab", "price": "75"},
                    {"ar": "قرفة", "en": "Cinnamon", "price": "30"},
                    {"ar": "حلبة", "en": "Fenugreek", "price": "50"},
                    {"ar": "ليمون", "en": "Lemon", "price": "30"}
                ]
            }
        ]
    },
    {
        "id": "cold-drinks",
        "title_ar": "المشروبات الباردة",
        "title_en": "COLD DRINKS",
        "icon": "🧊",
        "sub_sections": [
            {
                "title_ar": "قهوة باردة",
                "title_en": "Cold Coffee",
                "items": [
                    {"ar": "ايس امريكانو", "en": "Ice Americano", "price": "80"},
                    {"ar": "ايس لاتيه", "en": "Ice Latte", "price": "85"},
                    {"ar": "ايس سبانيش لاتيه", "en": "Ice Spanish Latte", "price": "95"},
                    {"ar": "ايس ثري كولور", "en": "Ice Three Colors", "price": "85"},
                    {"ar": "ايس كابيتشينو", "en": "Ice Cappuccino", "price": "85"},
                    {"ar": "ايس موكا", "en": "Ice Mocha", "price": "90"},
                    {"ar": "ايس بلو لاتيه", "en": "Ice Blue Latte", "price": "90"},
                    {"ar": "فرابيه اوريو", "en": "Oreo Frappe", "price": "90"},
                    {"ar": "فرابيتشينو", "en": "Frappuccino", "price": "95"}
                ]
            },
            {
                "title_ar": "موهيتو",
                "title_en": "Mojito",
                "items": [
                    {"ar": "موهيتو كلاسيك", "en": "Classic Mojito", "price": "80"},
                    {"ar": "موهيتو بلو بيري", "en": "Blueberry Mojito", "price": "90"},
                    {"ar": "موهيتو باشون فروت", "en": "Passion Fruit Mojito", "price": "90"},
                    {"ar": "صن شاين", "en": "Sunshine", "price": "60"}
                ]
            },
            {
                "title_ar": "سكوتش",
                "title_en": "Scotch",
                "items": [
                    {"ar": "هامر هيد", "en": "Hammerhead", "price": "110"},
                    {"ar": "بلو سكاي", "en": "Blue Sky", "price": "75"},
                    {"ar": "بينا كولادا", "en": "Piña Colada", "price": "70"}
                ]
            },
            {
                "title_ar": "سوفت درينك",
                "title_en": "Soft Drinks",
                "items": [
                    {"ar": "كنز", "en": "Cans", "price": "45"},
                    {"ar": "فيروز", "en": "Fayrouz", "price": "45"},
                    {"ar": "بيريل", "en": "Birell", "price": "45"},
                    {"ar": "V. COLA", "en": "V. Cola", "price": "45"},
                    {"ar": "فيوري", "en": "Fury", "price": "45"},
                    {"ar": "تويست", "en": "Twist", "price": "45"},
                    {"ar": "ريد بول", "en": "Red Bull", "price": "90"},
                    {"ar": "مياه معدنية", "en": "Water", "price": "15"}
                ]
            }
        ]
    },
    {
        "id": "fresh-juices",
        "title_ar": "العصائر الطازجة",
        "title_en": "FRESH JUICES",
        "icon": "🍊",
        "sub_sections": [
            {
                "title_ar": "",
                "title_en": "",
                "items": [
                    {"ar": "مانجو", "en": "Mango", "price": "70"},
                    {"ar": "جوافة", "en": "Guava", "price": "70"},
                    {"ar": "فراولة", "en": "Strawberry", "price": "70"},
                    {"ar": "بطيخ", "en": "Watermelon", "price": "70"},
                    {"ar": "موز باللبن", "en": "Banana Milk", "price": "75"},
                    {"ar": "برتقال", "en": "Orange", "price": "55"},
                    {"ar": "ليمون سادة", "en": "Plain Lemon", "price": "60"},
                    {"ar": "ليمون نعناع", "en": "Lemon Mint", "price": "65"},
                    {"ar": "كنتالوب", "en": "Cantaloupe", "price": "70"},
                    {"ar": "كيوي", "en": "Kiwi", "price": "80"},
                    {"ar": "خوخ", "en": "Peach", "price": "70"},
                    {"ar": "بلح باللبن", "en": "Dates with Milk", "price": "75"},
                    {"ar": "افوكادو", "en": "Avocado", "price": "100"},
                    {"ar": "فلوريدا", "en": "Florida", "price": "85"},
                    {"ar": "اوريو", "en": "Oreo", "price": "100"},
                    {"ar": "توينكز", "en": "Twinkies", "price": "100"},
                    {"ar": "هوهوز", "en": "HoHos", "price": "100"},
                    {"ar": "زبادي فراولة", "en": "Strawberry Yogurt", "price": "85"}
                ]
            }
        ]
    },
    {
        "id": "desserts",
        "title_ar": "الحلويات",
        "title_en": "DESSERTS",
        "icon": "🍰",
        "sub_sections": [
            {
                "title_ar": "",
                "title_en": "",
                "items": [
                    {"ar": "مولتن كيك", "en": "Molten Cake", "price": "120"},
                    {"ar": "ريد فيلفيت", "en": "Red Velvet", "price": "90"},
                    # {"ar": "تيراميسو", "en": "Tiramisu", "price": "110"},
                    # {"ar": "كيك جزر", "en": "Carrot Cake", "price": "85"},
                    {"ar": "تشيز كيك", "en": "Cheesecake", "price": "100"},
                    {"ar": "وافل", "en": "Waffle", "price": "50"},
                    {"ar": "ام علي", "en": "Om Ali", "price": "60"},
                    {"ar": "ارز بلبن", "en": "Rice Pudding", "price": "50"},
                    {"ar": "طواجن شوكلت", "en": "Chocolate Pots", "price": "50"}
                ]
            }
        ]
    },
    {
        "id": "milkshakes",
        "title_ar": "ميلك شيك",
        "title_en": "MILKSHAKES",
        "icon": "🥤",
        "sub_sections": [
            {
                "title_ar": "",
                "title_en": "",
                "items": [
                    {"ar": "فانيليا / لوتس / كراميل / شوكلت", "en": "Vanilla / Lotus / Caramel / Choco", "price": "80"},
                    {"ar": "فراولة", "en": "Strawberry", "price": "85"},
                    {"ar": "بلوبيري", "en": "Blueberry", "price": "75"},
                    {"ar": "تشيز كيك", "en": "Cheesecake", "price": "110"},
                    {"ar": "توتي فروتي", "en": "Tutti Frutti", "price": "120"},
                    {"ar": "فروت سالاد", "en": "Fruit Salad", "price": "100"},
                    {"ar": "مافين كيك", "en": "Muffin Cake", "price": "85"}
                ]
            },
            {
                "title_ar": "إضافات",
                "title_en": "Additions",
                "items": [
                    {"ar": "فانيليا", "en": "Vanilla", "price": "15"},
                    {"ar": "شوكلت", "en": "Chocolate", "price": "15"},
                    {"ar": "كراميل", "en": "Caramel", "price": "15"},
                    {"ar": "لوتس", "en": "Lotus", "price": "20"},
                    {"ar": "بستاشيو", "en": "Pistachio", "price": "20"},
                    {"ar": "بندق", "en": "Hazelnut", "price": "20"},
                    {"ar": "اسبريسو", "en": "Espresso", "price": "30"}
                ]
            }
        ]
    },
    {
        "id": "shisha",
        "title_ar": "الشيشة",
        "title_en": "SHISHA",
        "icon": "💨",
        "sub_sections": [
            {
                "title_ar": "",
                "title_en": "",
                "items": [
                    {"ar": "معسل", "en": "Moassel", "price": "20"},
                    {"ar": "فواكه مكس", "en": "Fawakeh Mix", "price": "100"},
                    {"ar": "فاخر", "en": "Fakher", "price": "150"},
                    {"ar": "كريستال", "en": "Crystal", "price": "150"},
                    {"ar": "لي طبي", "en": "Lai Toby", "price": "15"}
                ]
            }
        ]
    }
]

html_sections = ""
nav_items = ""

for index, section in enumerate(menu_data):
    is_active = "active" if index == 0 else ""
    nav_items += f"""
      <a class="nav-item {is_active}" href="#{section['id']}">
        <span class="ar-only">{section['title_ar']}</span>
        <span class="en-only">{section['title_en'].title()}</span>
      </a>"""

    html_sections += f"""
    <div class="section" id="{section['id']}">
      <div class="section-header">
        <div class="section-title-ar">{section['icon']} <span class="ar-only">{section['title_ar']}</span><span class="en-only">{section['title_en']}</span></div>
      </div>
"""
    for sub in section['sub_sections']:
        sub_title_html = ""
        if sub['title_ar'] or sub['title_en']:
            sub_title_html = f"""
        <div class="sub-title">
          <span class="ar-only">{sub['title_ar']}</span>
          <span class="en-only">{sub['title_en']}</span>
        </div>"""
        
        items_html = ""
        for item in sub['items']:
            price_class = "empty" if not item['price'] else ""
            items_html += f"""
          <div class="item">
            <span class="item-name">
              <span class="ar-only">{item['ar']}</span>
              <span class="en-only">{item['en']}</span>
            </span>
            <div class="item-dots"></div>
            <span class="item-price {price_class}">{item['price']} <span class="currency"><span class="ar-only"> ج.م</span><span class="en-only"> EGP</span></span></span>
          </div>"""
            
        html_sections += f"""
      <div class="sub-section">
        {sub_title_html}
        <div class="items-grid">
          {items_html}
        </div>
      </div>
"""
    html_sections += "    </div>\n"

# ================= CSS CONTENT =================
css_content = """:root {
  --gold: #d4af37;
  --gold-light: #f9f1cc;
  --gold-dark: #aa8a29;
  --bg-dark: #0a0a0a;
  --bg-card: #141414;
  --text-main: #f5f5f5;
  --text-muted: #a0a0a0;
  --accent: #1f1f1f;
  --shadow-color: rgba(0,0,0,0.5);
  --nav-bg: rgba(10, 10, 10, 0.9);
  --item-hover: rgba(212, 175, 55, 0.08);
  --border-color: rgba(212, 175, 55, 0.15);
  --border-hover: rgba(212, 175, 55, 0.4);
  --dots-color: rgba(212, 175, 55, 0.2);
}

[data-theme="light"] {
  --gold: #b8860b;
  --gold-light: #b8860b;
  --gold-dark: #8b6508;
  --bg-dark: #f0f2f5;
  --bg-card: #ffffff;
  --text-main: #212529;
  --text-muted: #6c757d;
  --accent: #e9ecef;
  --shadow-color: rgba(0,0,0,0.06);
  --nav-bg: rgba(255, 255, 255, 0.95);
  --item-hover: rgba(184, 134, 11, 0.06);
  --border-color: rgba(184, 134, 11, 0.15);
  --border-hover: rgba(184, 134, 11, 0.4);
  --dots-color: rgba(184, 134, 11, 0.2);
}

html[lang="ar"] .en-only { display: none !important; }
html[lang="en"] .ar-only { display: none !important; }

body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-dark);
  color: var(--text-main);
  font-family: 'Cairo', sans-serif;
  overflow-x: hidden;
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
}

.bg-animated {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(circle at top left, var(--dots-color) 0%, transparent 40%),
              radial-gradient(circle at bottom right, var(--dots-color) 0%, transparent 40%);
  z-index: -1;
  pointer-events: none;
}

.controls-container {
  position: absolute;
  top: 15px;
  right: 15px;
  display: flex;
  gap: 12px;
  z-index: 1000;
}
html[dir="rtl"] .controls-container {
  right: auto;
  left: 15px;
}

.control-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--gold);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 10px var(--shadow-color);
  font-family: 'Cairo', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  padding: 0;
  -webkit-appearance: none;
  transition: border-color 0.2s;
}
.control-btn:active {
  background: var(--item-hover);
}

[data-theme="light"] .icon-sun { display: none; }
[data-theme="dark"] .icon-moon { display: none; }

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 15px 30px;
  text-align: center;
  position: relative;
}

.logo {
  width: 130px;
  height: auto;
  margin-bottom: 20px;
  filter: drop-shadow(0 0 15px rgba(212, 175, 55, 0.3));
  animation: float 4s ease-in-out infinite;
  will-change: transform;
}

[data-theme="light"] .logo {
  filter: drop-shadow(0 0 15px rgba(184, 134, 11, 0.2));
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

.title {
  font-family: 'Amiri', serif;
  font-size: 2.4rem;
  color: var(--gold);
  margin: 0 0 5px;
  text-shadow: 0 2px 10px var(--dots-color);
}

.subtitle {
  font-size: 1.1rem;
  color: var(--gold-light);
  letter-spacing: 2px;
  margin: 0;
  text-transform: uppercase;
  font-weight: 600;
}

.category-nav-wrapper {
  position: sticky;
  top: 0;
  background: var(--nav-bg);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 100;
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 5px 15px var(--shadow-color);
}

.category-nav {
  display: flex;
  overflow-x: auto;
  padding: 12px 15px;
  gap: 10px;
  max-width: 1000px;
  margin: 0 auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.category-nav::-webkit-scrollbar { display: none; }

.nav-item {
  color: var(--text-muted);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  white-space: nowrap;
  padding: 8px 18px;
  border-radius: 30px;
  border: 1px solid transparent;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}
.nav-item.active {
  color: var(--gold);
  background: var(--item-hover);
  border-color: var(--border-color);
}

.menu-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 15px;
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.section {
  scroll-margin-top: 120px;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease-out, transform 0.5s ease-out;
  will-change: opacity, transform;
}
.section.visible {
  opacity: 1;
  transform: translateY(0);
}

.section-header {
  text-align: center;
  margin-bottom: 25px;
}
.section-title-ar {
  font-family: 'Amiri', serif;
  font-size: 2rem;
  color: var(--gold);
  margin-bottom: 5px;
  text-shadow: 0 0 15px var(--dots-color);
}

.sub-section {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 25px;
  box-shadow: 0 8px 25px var(--shadow-color);
  position: relative;
  overflow: hidden;
}
.sub-section::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  opacity: 0.7;
}

.sub-title {
  font-family: 'Amiri', serif;
  font-size: 1.4rem;
  color: var(--gold-light);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.sub-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(to left, var(--dots-color), transparent);
}
html[dir="ltr"] .sub-title::after {
  background: linear-gradient(to right, var(--dots-color), transparent);
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 12px 30px;
}

.item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  border-radius: 8px;
  position: relative;
  -webkit-tap-highlight-color: transparent;
}

.item-name {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--text-main);
  z-index: 1;
}
.item-dots {
  flex: 1;
  border-bottom: 1px dashed var(--dots-color);
  margin: 0 12px;
  position: relative;
  top: -4px;
}
.item-price {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--gold);
  z-index: 1;
  text-shadow: 0 0 8px var(--dots-color);
  display: flex;
  align-items: baseline;
  gap: 3px;
}
.item-price.empty {
  display: none;
}
.currency {
  font-size: 0.75rem;
  color: var(--text-muted);
  font-weight: 600;
}

footer {
  text-align: center;
  padding: 40px 15px;
  color: var(--gold-dark);
  font-size: 0.9rem;
  border-top: 1px solid var(--border-color);
  background: var(--bg-dark);
  font-family: 'Amiri', serif;
  letter-spacing: 1px;
}

.scroll-top {
  position: fixed;
  bottom: 20px;
  left: 20px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--gold);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  z-index: 1000;
  box-shadow: 0 4px 10px var(--shadow-color);
  -webkit-appearance: none;
}
html[dir="ltr"] .scroll-top {
  left: auto;
  right: 20px;
}
.scroll-top.visible {
  opacity: 1;
  visibility: visible;
}

@media (max-width: 480px) {
  .items-grid { grid-template-columns: 1fr; }
  .title { font-size: 2rem; }
  .logo { width: 110px; }
}"""

# ================= JS CONTENT =================
js_content = """// Theme Switcher
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
});"""

# ================= HTML CONTENT =================
html_template = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>قائمة طعام - قهوة سليم أفندي | Salim Efendi Menu</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body data-theme="dark">

  <div class="bg-animated"></div>

  <div class="controls-container">
    <button id="themeToggle" class="control-btn" aria-label="Toggle Theme">
      <span class="icon-sun">☀️</span>
      <span class="icon-moon">🌙</span>
    </button>
    <button id="langToggle" class="control-btn" aria-label="Toggle Language">
      <span class="ar-only">EN</span>
      <span class="en-only">AR</span>
    </button>
  </div>

  <header class="hero">
    <img src="{logo_src}" class="logo" alt="Salim Efendi Logo">
    <h1 class="title">
      <span class="ar-only">قهوة سليم أفندي</span>
      <span class="en-only">Salim Efendi Coffee</span>
    </h1>
  </header>

  <div class="category-nav-wrapper">
    <nav class="category-nav" id="nav">
      {nav_items}
    </nav>
  </div>

  <main class="menu-container">
    {html_sections}
  </main>

  <footer>
    <p class="ar-only">✦ أسعارنا شاملة ضريبة القيمة المضافة ✦</p>
    <p class="en-only">✦ All prices include VAT ✦</p>
    <p style="font-size: 0.8rem; margin-top: 10px; opacity: 0.5;">Salim Efendi Coffee</p>
  </footer>

  <div class="scroll-top" id="scrollTop" aria-label="Top">
    ↑
  </div>

  <script src="script.js"></script>
</body>
</html>"""


# Write the files
with open('g:/MENU/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
    
with open('g:/MENU/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

with open('g:/MENU/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("HTML, CSS, and JS files have been generated successfully.")
