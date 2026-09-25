# Генерує сторінки послуг (svc-<key>), «Ціни» (prices), «Контакти» (contacts) і гео-сторінки (city-<key>)
# та src/lib/services.json для site.mjs. Тексти — services_data.py, services_pages.py, cities_data.py.
# Запуск: python3 scripts/build_services.py
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks import *
from services_data import SERVICES
from services_pages import PRICES, CONTACTS
from cities_data import CITIES

NICHES = load_niches()
NICHE_SVC = ('lending', 'sait-vizytka', 'korporatyvnyi-sait')  # послуги, на яких показуємо «Сайти для вашої галузі»

# ---------- сторінки послуг
out = []
for s in SERVICES:
    others = [o for o in SERVICES if o['key'] != s['key']]
    body = [
        hero(wm(s['name_uk'], s['name_pl']), L(s['h1_uk'], s['h1_pl']), L(s['sub_uk'], s['sub_pl']), s['facts'], 'about'),
        intro('about', L(s['intro_title_uk'], s['intro_title_pl']), L(s['incl_title_uk'], s['incl_title_pl']), L(s['lead_uk'], s['lead_pl']), s['pills'], s['incl'], L('Обговорити проєкт', 'Porozmawiajmy o projekcie')),
        steps_block(s['steps'], L('Етапи роботи', 'Etapy pracy'), L('Процес', 'Proces')),
        tariffs_block(L('Ціна', 'Cena'), L('Тарифи', 'Pakiety'), L(s['plans_lead_uk'], s['plans_lead_pl']), s['plans'], s['addons']),
        cases_block(s['cases']),
        faq_block(s['faq']),
        *([niches_block(NICHES)] if s['key'] in NICHE_SVC and NICHES else []),
        services_block(others, L('Інші послуги', 'Inne usługi'), L('Послуги', 'Usługi')),
        CONTACT,
    ]
    write('svc-' + s['key'], body)
    out.append({k: s[k] for k in ('key', 'path_uk', 'path_pl', 'name_uk', 'name_pl', 'title_uk', 'title_pl', 'desc_uk', 'desc_pl')}
               | {'price': next((p['price'] for p in s['plans'] if p.get('price')), None)})

# ---------- «Ціни»
P = PRICES
write('prices', [
    hero(wm('Ціни', 'Cennik'), L(P['h1_uk'], P['h1_pl']), L(P['sub_uk'], P['sub_pl']), P['facts'], 'tariffs'),
    tariffs_block(L('Тарифи на сайти', 'Pakiety stron'), L('Ціни', 'Cennik'), L(P['plans_lead_uk'], P['plans_lead_pl']), P['plans'], P['addons']),
    intro('about', L(P['intro_title_uk'], P['intro_title_pl']), L('Що впливає на ціну', 'Co wpływa na cenę'), L(P['lead_uk'], P['lead_pl']), P['pills'], P['factors'], L('Отримати оцінку', 'Otrzymaj wycenę')),
    faq_block(P['faq'], L('Питання про ціни', 'Pytania o ceny')),
    services_block(SERVICES, L('Усі послуги', 'Wszystkie usługi'), L('Послуги', 'Usługi')),
    *([niches_block(NICHES)] if NICHES else []),
    CONTACT,
])

# ---------- «Контакти»
C = CONTACTS
pills = ''.join(f'<span class="budget-pill" role="listitem">{L(u, p)}</span>' for u, p in C['pills'])
pills += ''.join(f'<span class="budget-pill" aria-hidden="true">{L(u, p)}</span>' for u, p in C['pills'])
who = '''    <section class="section" id="about">
      <div class="container">
''' + head(L('Як з нами зв\'язатися', 'Jak się z nami skontaktować'), L('Контакти', 'Kontakt')) + '''
        <div class="budget-grid">
        <div class="budget-intro reveal">
          <p class="budget-lead">''' + L(C['lead_uk'], C['lead_pl']) + '''</p>
          <p class="budget-sub">''' + L(C['sub2_uk'], C['sub2_pl']) + '''</p>
          <div class="budget-pills" role="list">
            <div class="budget-pills__track">''' + pills + '''</div>
          </div>
          <a href="https://t.me/Andrii_DEV9" class="btn btn--dark btn--lg budget-intro__btn" target="_blank" rel="noopener">
            <span>''' + L('Написати в Telegram', 'Napisz na Telegramie') + '''</span>
            ''' + ARROW + '''
          </a>
        </div>
        <div class="reveal">
          <a class="bx-card" href="https://t.me/Andrii_DEV9" target="_blank" rel="noopener" aria-label="Telegram Andrii Shestakov">
            <div class="bx-card__media"><img src="assets/photo.webp" alt="Andrii Shestakov — Founder &amp; CEO SHSTKV Digital" loading="lazy" style="object-position: center 38%" /></div>
            <div class="bx-card__bar">
              <span class="bx-card__cat">Andrii Shestakov · Founder &amp; CEO</span>
              <span class="bx-card__cta" aria-hidden="true">''' + ARROW_LG + '''</span>
            </div>
          </a>
        </div>
        </div>
      </div>
    </section>'''
CITY_ITEMS = [dict(key=x['key'], img=f"assets/service-{i % 5 + 1}.webp", name_uk=x['name_uk'], name_pl=x['name_pl'], sub_uk=x['sub_uk'], sub_pl=x['sub_pl'])
              for i, x in enumerate(c for c in CITIES if c['key'] != 'polshcha')]
cities_nav = services_block(CITY_ITEMS, L('Працюємо по всій Польщі', 'Pracujemy w całej Polsce'), L('Міста', 'Miasta'), 'city-')
# хаб /polshcha/ існує лише українською — посилання на нього тільки в UA-версії
cities_nav = cities_nav.replace('<div class="services reveal-group">',
    '<p class="section__lead reveal" data-lang-block="uk">Український бізнес у Польщі? Ось <a href="city-polshcha" style="text-decoration: underline; text-underline-offset: 3px">як ми робимо сайти під польський ринок</a>.</p>\n        <div class="services reveal-group">', 1)
write('contacts', [
    hero(wm('Контакти', 'Kontakt'), L(C['h1_uk'], C['h1_pl']), L(C['sub_uk'], C['sub_pl']), C['facts'], 'contact'),
    CONTACT,
    who,
    cities_nav,
    faq_block(C['faq'], L('Перед тим як написати', 'Zanim napiszesz')),
])

# ---------- гео-сторінки: хаб /polshcha/ і міста
CITY_TARIFFS = [a for a in PRICES['addons'] if a.get('href') in ('svc-korporatyvnyi-sait', 'svc-internet-magazyn') or a['name_uk'] == 'Підтримка сайту']
city_out = []
city_list = [c for c in CITIES if c['key'] != 'polshcha']
for c in CITIES:
    hub = c['key'] == 'polshcha'
    if hub:
        items = [dict(key=x['key'], img=f"assets/service-{i % 5 + 1}.webp", name_uk=x['name_uk'], name_pl=x['name_pl'], sub_uk=x['sub_uk'], sub_pl=x['sub_pl']) for i, x in enumerate(city_list)]
        tail = services_block(items, L('Міста', 'Miasta'), L('Польща', 'Polska'), 'city-')
    else:
        tail = services_block(SERVICES, L('Послуги', 'Usługi'), L('Що робимо', 'Co robimy'))
    body = [
        hero(wm(c['name_uk'], c['name_pl']), L(c['h1_uk'], c['h1_pl']), L(c['sub_uk'], c['sub_pl']), c['facts'], 'about'),
        intro('about', L(c['intro_title_uk'], c['intro_title_pl']), L(c['incl_title_uk'], c['incl_title_pl']), L(c['lead_uk'], c['lead_pl']), c['pills'], c['incl'], L('Обговорити проєкт', 'Porozmawiajmy o projekcie')),
        local_block(c),
        tariffs_block(L('Ціни', 'Cennik'), L('Тарифи', 'Pakiety'), L(PRICES['plans_lead_uk'], PRICES['plans_lead_pl']), PRICES['plans'], CITY_TARIFFS),
        cases_block(c['cases']),
        faq_block(c['faq']),
        tail,
        CONTACT,
    ]
    write('city-' + c['key'], body)
    city_out.append({k: c[k] for k in ('key', 'path_uk', 'path_pl', 'name_uk', 'name_pl', 'title_uk', 'title_pl', 'desc_uk', 'desc_pl')})

json.dump({'services': out, 'cities': city_out, 'prices': {k: P[k] for k in ('title_uk', 'title_pl', 'desc_uk', 'desc_pl')},
           'contacts': {k: C[k] for k in ('title_uk', 'title_pl', 'desc_uk', 'desc_pl')}},
          open(os.path.join(HERE, '..', 'src', 'lib', 'services.json'), 'w'), ensure_ascii=False, indent=1)
print('built', len(SERVICES), 'services + prices + contacts')
