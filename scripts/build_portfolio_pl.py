# Генерує польське портфоліо src/templates/portfolio-pl.html з portfolio.html:
# розмітка та класи ті самі, змінюється лише текст. Категорії карток — з I18N (case.N.meta).
# Запуск: python3 scripts/build_portfolio_pl.py (після змін у portfolio.html)
import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
TPL = os.path.join(ROOT, 'src', 'templates')

META = json.loads(subprocess.check_output(['node', '--input-type=module', '-e', '''
import { t } from "./src/lib/i18n.mjs";
const out = {};
for (let i = 1; i <= 60; i++) { const k = `case.${i}.meta`; const u = t("uk", k); if (u !== k) out[u] = t("pl", k); }
console.log(JSON.stringify(out));
'''], cwd=ROOT))

TEXT = [
    ('aria-label="Навігація"', 'aria-label="Nawigacja"'),
    ('class="nav-menu__link">Головна<', 'class="nav-menu__link">Strona główna<'),
    ('aria-current="page">Портфоліо<', 'aria-current="page">Portfolio<'),
    ('class="nav-menu__link">Послуги<', 'class="nav-menu__link">Usługi<'),
    ('class="nav-menu__link">Тарифи<', 'class="nav-menu__link">Cennik<'),
    ('class="nav-menu__link">Контакти<', 'class="nav-menu__link">Kontakt<'),
    ('>Польща · Європа<', '>Polska · Europa<'),
    ('>Політика конфіденційності<', '>Polityka prywatności<'),
    ('aria-label="Web Shestakov — на головну"', 'aria-label="Web Shestakov — strona główna"'),
    ('Портфоліо Web Shestakov — вибрані проєкти', 'Portfolio Web Shestakov — wybrane strony i sklepy internetowe'),
    ('aria-label="Категорії проєктів"', 'aria-label="Kategorie projektów"'),
    ('aria-label="Сторінки проєктів"', 'aria-label="Strony projektów"'),
    ('aria-label="Попередня сторінка"', 'aria-label="Poprzednia strona"'),
    ('aria-label="Наступна сторінка"', 'aria-label="Następna strona"'),
    ('data-filter="all">Всі сайти<', 'data-filter="all">Wszystkie strony<'),
    ('data-filter="ecom">Інтернет-магазини<', 'data-filter="ecom">Sklepy internetowe<'),
    ('data-filter="budget">Сайти від €300<', 'data-filter="budget">Strony od 300 €<'),
    ('У цій категорії поки немає проєктів.', 'W tej kategorii nie ma jeszcze projektów.'),
    ('Створюю сайти та інтернет-магазини для бізнесу і брендів: від дизайну до розробки й запуску. Фокус — швидкість, конверсія та охайний преміальний вигляд. Складні проєкти веду разом з командою Web Shestakov.',
     'Tworzę strony i sklepy internetowe dla firm i marek: od projektu graficznego po wdrożenie i start. Stawiam na szybkość, konwersję i staranny, premium wygląd. Złożone projekty prowadzę razem z zespołem Web Shestakov.'),
    ('<span>Обговорити проєкт</span>', '<span>Omówić projekt</span>'),
    ('Телефон&nbsp;', 'Telefon&nbsp;'),
    ('id="contact-title">Маєте проєкт?<', 'id="contact-title">Masz projekt?<'),
    ('<p class="contact__title">Зробимо разом</p>', '<p class="contact__title">Zróbmy to razem</p>'),
    ('aria-hidden="true">Перейти</div>', 'aria-hidden="true">Zobacz</div>'),
    ('aria-label="Закрити"', 'aria-label="Zamknij"'),
    ('>Закрити<', '>Zamknij<'),
    ('>Меню<', '>Menu<'),
    ('<span class="magnetic">На головну</span>', '<span class="magnetic">Strona główna</span>'),
    ('aria-label="Написати Andrii Shestakov у Telegram"', 'aria-label="Napisz do Andrii Shestakov na Telegramie"'),
]

s = open(os.path.join(TPL, 'portfolio.html')).read()
for a, b in TEXT:
    s = s.replace(a, b)
s = re.sub(r'((?:Лендинг|Багатосторінковий|Інтернет-магазин) • [^<]+)<', lambda m: META[m.group(1)] + '<', s)
s = s.replace(' — скриншот сайту"', ' — zrzut ekranu strony"')

left = sorted(set(m.strip() for m in re.findall(r'>([^<>]*[А-Яа-яІіЇїЄєҐґ][^<>]*)<', re.sub(r'<script.*?</script>|<!--.*?-->', '', s[s.index('<body'):], flags=re.S))))
left += re.findall(r'(?:alt|aria-label|title)="([^"]*[А-Яа-яІіЇїЄєҐґ][^"]*)"', s)
if left:
    raise SystemExit('Неперекладений текст: ' + ' | '.join(left))
open(os.path.join(TPL, 'portfolio-pl.html'), 'w').write(s)
print('built portfolio-pl.html')
