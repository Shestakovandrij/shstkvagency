# Генерує нішеві сторінки («Сайт для будівельної компанії» тощо) з блоків головної
# та src/lib/niches.json для site.mjs. Кожна ніша — файл scripts/niches/<key>.py зі змінною NICHE.
# Запуск: python3 scripts/build_niches.py
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks import *
from services_pages import PRICES

TARIFFS = [a for a in PRICES['addons'] if a.get('href') in ('svc-korporatyvnyi-sait', 'svc-internet-magazyn') or a['name_uk'] == 'Підтримка сайту']

niches = load_niches()
out = []
for n in niches:
    others = [o for o in niches if o['key'] != n['key']]
    body = [
        hero(wm(n['name_uk'], n['name_pl']), L(n['h1_uk'], n['h1_pl']), L(n['sub_uk'], n['sub_pl']), n['facts'], 'about'),
        intro('about', L(n['intro_title_uk'], n['intro_title_pl']), L(n['incl_title_uk'], n['incl_title_pl']), L(n['lead_uk'], n['lead_pl']), n['pills'], n['incl'], L('Обговорити проєкт', 'Porozmawiajmy o projekcie')),
        local_block(n),
        tariffs_block(L('Ціни', 'Cennik'), L('Тарифи', 'Pakiety'), L(PRICES['plans_lead_uk'], PRICES['plans_lead_pl']), PRICES['plans'], TARIFFS),
        cases_block(n['cases']),
        faq_block(n['faq']),
        niches_block(others, L('Інші галузі', 'Inne branże')),
        CONTACT,
    ]
    write('niche-' + n['key'], body)
    out.append({k: n[k] for k in ('key', 'path_uk', 'path_pl', 'name_uk', 'name_pl', 'h1_uk', 'h1_pl', 'title_uk', 'title_pl', 'desc_uk', 'desc_pl')} | {'price': '300'})

json.dump({'niches': out}, open(os.path.join(HERE, '..', 'src', 'lib', 'niches.json'), 'w'), ensure_ascii=False, indent=1)
print('built', len(niches), 'niches')
