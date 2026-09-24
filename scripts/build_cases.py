# Генерує сторінки кейсів src/templates/case-<slug>.html з блоків головної (home.html)
# і src/lib/cases.json для карти сайту. Запуск: python3 scripts/build_cases.py
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, '..', 'src', 'templates')
sys.path.insert(0, HERE)
from cases_data import CASES

home = open(os.path.join(TPL, 'home.html')).read()

def L(uk, pl):
    return f'<span data-lang-block="uk">{uk}</span><span data-lang-block="pl" hidden>{pl}</span>'

ARROW = '<span class="btn__play" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12"><path d="M7 17L17 7M17 7H8M17 7v9" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
ARROW_LG = '<svg viewBox="0 0 24 24" width="18" height="18"><path d="M7 17L17 7M17 7H8M17 7v9" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def head(title, tag):
    return f'''        <div class="section__head section__head--split reveal">
          <h2 class="section__title">{title}</h2>
          <span class="section__rule" aria-hidden="true"></span>
          <span class="eyebrow"><span class="eyebrow__dot eyebrow__dot--square"></span><span>{tag}</span></span>
        </div>
'''

def section(src, marker):
    a = src.index(marker)
    return src[a:src.index('</section>', a) + len('</section>')]

# ---------- спільна оболонка: шапка, меню, футер, попап без прелоадера
shell = re.sub(r'\n    /\* Preloader guards.*?\}\)\(\);\n', '\n', home, flags=re.S)
shell = shell.replace('  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>\n', '')
shell = shell.replace('  <script src="preloader.js" defer></script>\n', '')
shell = re.sub(r'  <!-- GSAP drives the preloader.*?-->\n', '', shell, flags=re.S)
a = shell.index('  <div class="preloader" id="preloader"'); b = shell.index('  <header class="header" id="header">')
shell = shell[:a] + shell[b:]
HERO = section(shell, '    <section class="hero" id="home">')
CONTACT = section(shell, '    <section class="section" id="contact">')
start = shell.index('    <section class="hero" id="home">')
pe = shell.index('    <section class="section" id="partners">')
end = shell.index('</section>', pe) + len('</section>')
BEFORE, AFTER = shell[:start], shell[end:]

def nav_to_home(s):
    return re.sub(r'href="#(about|why|services|cases|budget|tariffs|faq|partners|home)"', r'href="index.html#\1"', s)

def case_card(i, c):
    return f'''          <a class="case" href="case-{c['slug']}" aria-label="{c['name']}">
            <div class="case__media">
              <img src="{c['img']}" alt="{c['name']}" loading="lazy" width="1200" height="840" />
            </div>
            <div class="case__bar">
              <div class="case__id">
                <span class="case__num">(0{i})</span>
                <h3 class="case__name">{c['name']}</h3>
              </div>
              <span class="case__cat">{L(c['facts'][-1][2], c['facts'][-1][3])}</span>
              <span class="case__cta" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path d="M7 17L17 7M17 7H8M17 7v9" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </div>
          </a>
'''

pages = []
for idx, c in enumerate(CASES):
    # ---------- hero: той самий, що на головній
    hero = HERO.replace('<div class="hero__wordmark">Web&nbsp;Shestakov<span class="hero__reg">&reg;</span></div>',
                        '<div class="hero__wordmark">' + c['name'].replace(' ', '&nbsp;').replace('&nbsp;&&nbsp;', '&nbsp;&amp;&nbsp;') + '</div>')
    o1 = hero.index('<div class="hero__overlay">'); o2 = hero.index('<!-- Bottom service shelf')
    hero = hero[:o1] + '''<div class="hero__overlay">
            <h1 class="hero__headline">''' + L(c['h1_uk'], c['h1_pl']) + '''</h1>
            <p class="hero__headline-sub">''' + L(c['sub_uk'], c['sub_pl']) + '''</p>
          </div>

          ''' + hero[o2:]
    def fcard(i, f, dup):
        extra = ' shelf__card--dup" aria-hidden="true" tabindex="-1' if dup else ''
        return f'''              <a href="#task" class="shelf__card{extra}">
                <span class="shelf__thumb shelf__thumb--{i}" aria-hidden="true"></span>
                <span class="shelf__meta"><span class="shelf__num">{L(f[0], f[1])}</span><span class="shelf__name">{L(f[2], f[3])}</span></span>
              </a>
'''
    t1 = hero.index('<div class="shelf__track">') + len('<div class="shelf__track">\n')
    t2 = hero.index('            </div>\n          </div>\n        </div>', t1)
    hero = hero[:t1] + ''.join(fcard(i + 1, f, False) for i, f in enumerate(c['facts'])) + ''.join(fcard(i + 1, f, True) for i, f in enumerate(c['facts'])) + hero[t2:]

    # ---------- задача і рішення: сітка «Бюджетний запуск» + картка сайту
    pills = ''.join(f'<span class="budget-pill" role="listitem">{L(u, p)}</span>' for u, p in c['pills'])
    pills += ''.join(f'<span class="budget-pill" aria-hidden="true">{L(u, p)}</span>' for u, p in c['pills'])
    task = '''    <section class="section" id="task">
      <div class="container">
''' + head(L('Задача і рішення', 'Zadanie i rozwiązanie'), L('Кейс', 'Realizacja')) + '''
        <div class="budget-grid">
        <div class="budget-intro reveal">
          <p class="budget-lead">''' + L(c['task_uk'], c['task_pl']) + '''</p>
          <p class="budget-sub">''' + L(c['sol_uk'], c['sol_pl']) + '''</p>
          <div class="budget-pills" role="list">
            <div class="budget-pills__track">''' + pills + '''</div>
          </div>
          <a href="''' + c['url'] + '''" class="btn btn--dark btn--lg budget-intro__btn" target="_blank" rel="noopener">
            <span>''' + L('Відкрити сайт', 'Zobacz stronę') + '''</span>
            ''' + ARROW + '''
          </a>
        </div>
        <div class="reveal">
          <a class="bx-card" href="''' + c['url'] + '''" target="_blank" rel="noopener" aria-label="''' + c['name'] + '''">
            <div class="bx-card__media"><img src="''' + c['img'] + '''" alt="''' + c['name'] + ''' — ''' + c['h1_uk'] + '''" loading="lazy" /></div>
            <div class="bx-card__bar">
              <span class="bx-card__cat">''' + L(c['facts'][-1][2] + ' · ' + c['facts'][1][2], c['facts'][-1][3] + ' · ' + c['facts'][1][3]) + '''</span>
              <span class="bx-card__cta" aria-hidden="true">''' + ARROW_LG + '''</span>
            </div>
          </a>
        </div>
        </div>
      </div>
    </section>'''

    # ---------- що всередині: макет FAQ головної
    faq = section(shell, '    <section class="section section--soft" id="faq">')
    items = ''.join(f'''          <div class="faq__item">
            <button type="button" class="faq__q" aria-expanded="false"><span class="faq__qn">(0{i})</span><span>{L(tu, tp)}</span><span class="faq__icon" aria-hidden="true"></span></button>
            <div class="faq__a"><p>{L(du, dp)}</p></div>
          </div>
''' for i, (tu, tp, du, dp) in enumerate(c['feats'], 1))
    f1 = faq.index('        <div class="faq reveal-group">') + len('        <div class="faq reveal-group">\n')
    f2 = faq.index('        </div>\n      </div>\n    </section>')
    faq = faq[:f1] + items + faq[f2:]
    faq = faq.replace('id="faq"', 'id="inside"')
    faq = faq.replace('<span data-i18n="faq.tag">FAQ</span>', '<span>' + L('Що зробили', 'Co zrobiliśmy') + '</span>')
    faq = faq.replace('<h2 class="section__title" data-i18n="faq.title">Питання та відповіді</h2>', '<h2 class="section__title">' + L('Що всередині сайту', 'Co jest na stronie') + '</h2>')
    faq = faq.replace('<p class="section__lead" data-i18n="faq.desc">Не знайшли відповідь?<br>Напишіть нам у Telegram — відповімо швидко.</p>',
                      '<p class="section__lead">' + L('Хочете такий самий сайт для свого бізнесу?<br>Напишіть — оцінимо за 24 години.', 'Chcesz podobną stronę dla swojej firmy?<br>Napisz — wycenimy w 24 godziny.') + '</p>')

    # ---------- інші кейси: сітка кейсів головної
    others = [CASES[(idx + k) % len(CASES)] for k in (1, 2)]
    more = '''    <section class="section" id="more">
      <div class="container">
''' + head(L('Інші кейси', 'Inne realizacje'), L('Портфоліо', 'Portfolio')) + '''
        <div class="cases reveal-group">
''' + ''.join(case_card(i, o) for i, o in enumerate(others, 1)) + '''        </div>
      </div>
    </section>'''

    body = '\n\n'.join([hero, task, faq, more, CONTACT])
    html = nav_to_home(BEFORE + body + AFTER)
    open(os.path.join(TPL, f"case-{c['slug']}.html"), 'w').write(html)
    pages.append({k: c[k] for k in ('slug', 'name', 'title_uk', 'title_pl', 'desc_uk', 'desc_pl')})

json.dump(pages, open(os.path.join(HERE, '..', 'src', 'lib', 'cases.json'), 'w'), ensure_ascii=False, indent=1)
print('built', len(pages), 'case pages')
