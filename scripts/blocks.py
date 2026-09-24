# Спільні блоки сторінок, зібрані з home.html: hero, «для кого» (partners), етапи (why-acc),
# тарифи, кейси, FAQ, список (services), форма. Використовують build_services.py і build_blog.py.
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, '..', 'src', 'templates')
sys.path.insert(0, HERE)
from cases_data import CASES

CASE = {c['slug']: c for c in CASES}
home = open(os.path.join(TPL, 'home.html')).read()

def L(uk, pl):
    return f'<span data-lang-block="uk">{uk}</span><span data-lang-block="pl" hidden>{pl}</span>'

ARROW = '<span class="btn__play" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12"><path d="M7 17L17 7M17 7H8M17 7v9" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
ARROW_T = '<span class="tariff__cta-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
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

# ---------- оболонка: шапка, меню, футер, попап; без прелоадера
shell = re.sub(r'\n    /\* Preloader guards.*?\}\)\(\);\n', '\n', home, flags=re.S)
shell = shell.replace('  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>\n', '')
shell = shell.replace('  <script src="preloader.js" defer></script>\n', '')
shell = re.sub(r'  <!-- GSAP drives the preloader.*?-->\n', '', shell, flags=re.S)
a = shell.index('  <div class="preloader" id="preloader"'); b = shell.index('  <header class="header" id="header">')
shell = shell[:a] + shell[b:]
shell = shell.replace('<span class="menu__meta-item"><span class="menu__meta-dot"></span>Web Shestakov — ', '<span class="menu__meta-item"><span class="menu__meta-dot"></span>SHSTKV Digital — ')
HERO = section(shell, '    <section class="hero" id="home">')
CONTACT = section(shell, '    <section class="section" id="contact">')
FAQ = section(shell, '    <section class="section section--soft" id="faq">')
TARIFFS = section(shell, '    <section class="section" id="tariffs">')
start = shell.index('    <section class="hero" id="home">')
pe = shell.index('    <section class="section" id="partners">')
end = shell.index('</section>', pe) + len('</section>')
BEFORE, AFTER = shell[:start], shell[end:]

def nav_to_home(s):
    return re.sub(r'href="#(about|why|services|cases|budget|tariffs|faq|partners|home)"', r'href="index.html#\1"', s)

# ---------- блоки
def hero(wordmark, h1, sub, facts, anchor):
    h = HERO.replace('<div class="hero__wordmark">Web&nbsp;Shestakov<span class="hero__reg">&reg;</span></div>',
                     '<div class="hero__wordmark">' + wordmark + '</div>')
    o1 = h.index('<div class="hero__overlay">'); o2 = h.index('<!-- Bottom service shelf')
    h = h[:o1] + '''<div class="hero__overlay">
            <h1 class="hero__headline">''' + h1 + '''</h1>
            <p class="hero__headline-sub hero__headline-sub--wide">''' + sub + '''</p>
          </div>

          ''' + h[o2:]
    def card(i, f, dup):
        extra = ' shelf__card--dup" aria-hidden="true" tabindex="-1' if dup else ''
        return f'''              <a href="#{anchor}" class="shelf__card{extra}">
                <span class="shelf__thumb shelf__thumb--{i}" aria-hidden="true"></span>
                <span class="shelf__meta"><span class="shelf__num">{L(f[0], f[1])}</span><span class="shelf__name">{L(f[2], f[3])}</span></span>
              </a>
'''
    t1 = h.index('<div class="shelf__track">') + len('<div class="shelf__track">\n')
    t2 = h.index('            </div>\n          </div>\n        </div>', t1)
    return h[:t1] + ''.join(card(i + 1, f, False) for i, f in enumerate(facts)) + ''.join(card(i + 1, f, True) for i, f in enumerate(facts)) + h[t2:]

def intro(id_, title, tag, lead, pills, cards, cta):
    chips = ''.join(f'<span class="partners-chip" role="listitem">{L(u, p)}</span>' for u, p in pills)
    chips += ''.join(f'<span class="partners-chip" aria-hidden="true">{L(u, p)}</span>' for u, p in pills)
    cs = ''.join(f'''            <article class="partner-card">
              <span class="partner-card__num">(0{i})</span>
              <div class="partner-card__body">
                <h3 class="partner-card__text">{L(tu, tp)}</h3>
                <p class="partner-card__desc">{L(du, dp)}</p>
              </div>
            </article>
''' for i, (tu, tp, du, dp) in enumerate(cards, 1))
    return f'''    <section class="section" id="{id_}">
      <div class="container">
{head(title, tag)}        <div class="partners-layout">
          <div class="partners-intro reveal">
            <p class="section__lead section__lead--partners">{lead}</p>

            <div class="partners-marquee" role="list">
              <div class="partners-marquee__track">{chips}</div>
            </div>

            <button type="button" class="btn btn--dark btn--lg" data-open-popup>
              <span>{cta}</span>
              {ARROW}
            </button>
          </div>

          <div class="partners-cards reveal-group">
{cs}          </div>
        </div>
      </div>
    </section>'''

def steps_block(steps, title, tag):
    cards = ''
    for i, st in enumerate(steps, 1):
        tu, tp, du, dp, k1, k2 = st
        op = ' wa-card--open' if i == 1 else ''
        cards += f'''          <article class="wa-card{op}">
            <div class="wa-num"><span class="wa-num__label">{L('Етап', 'Etap')}</span><span class="wa-num__line"></span><span class="wa-num__idx">(0{i})</span></div>
            <div class="wa-content">
              <div class="wa-image"><img src="assets/why-{i}.webp" alt="" loading="lazy" /></div>
              <h3 class="wa-content__title">{L(tu, tp)}</h3>
              <p class="wa-content__text">{L(du, dp)}</p>
              <div class="wa-tags"><span class="wa-tag">{L(*k1)}</span><span class="wa-tag">{L(*k2)}</span></div>
            </div>
            <div class="wa-vert"><h3>{L(tu, tp)}</h3></div>
          </article>

'''
    return f'''    <section class="section" id="how">
      <div class="container">
        <div class="wa-head reveal">
          <h2 class="wa-head__title">{title}</h2>
          <span class="wa-head__divider" aria-hidden="true"></span>
          <span class="wa-head__tag"><span class="wa-head__dot" aria-hidden="true"></span><span>{tag}</span></span>
        </div>

        <div class="why-acc reveal">
{cards}        </div>
      </div>
    </section>'''

def price_html(p, small=False):
    cls = 'tariff__price tariff__price--sm' if small else 'tariff__price'
    if p.get('price'):
        return f'<span class="{cls}"><span class="plan-card__cur">€</span>{p["price"]}</span>'
    return f'<span class="{cls}">{L("Оцінка", "Wycena")}</span>'

def unit_html(p):
    if p.get('price'):
        return f'<span class="tariff__unit">{L(p["unit_uk"], p["unit_pl"])}</span>'
    return f'<span class="tariff__unit">{L("за 24 год", "w 24 h")}</span>'

def plan_card(p):
    rec = p.get('rec')
    badge = f'<span class="tariff__badge">{L(p["badge_uk"], p["badge_pl"])}</span>\n              ' if rec and p.get('badge_uk') else ''
    frm = f'<span class="tariff__unit">{L("від", "od")}</span>\n              ' if p.get('price') and p.get('from_') else ''
    feats = ''.join(f'              <li><span class="plan-check" aria-hidden="true"></span><span>{L(u, pl)}</span></li>\n' for u, pl in p['feats'])
    cta = L('Обрати тариф', 'Wybierz pakiet') if rec else L('Замовити', 'Zamów')
    return f'''          <article class="tariff{' tariff--rec' if rec else ''} reveal">
{'            <div class="tariff__stone" aria-hidden="true"></div>' + chr(10) if rec else ''}            <div class="tariff__meta">
              {badge}<span class="tariff__tag">{L(p['tag_uk'], p['tag_pl'])}</span>
            </div>
            <div class="tariff__top">
              {frm}{price_html(p)}
              {unit_html(p)}
            </div>
            <h3 class="tariff__name">{L(p['name_uk'], p['name_pl'])}</h3>
            <p class="tariff__sub">{L(p['desc_uk'], p['desc_pl'])}</p>
            <ul class="plan-card__list">
{feats}            </ul>
            <button type="button" class="tariff__cta tariff__cta--{'accent' if rec else 'dark'}" data-open-popup>
              <span>{cta}</span>
              {ARROW_T}
            </button>
          </article>
'''

def addon(p):
    frm = f'<span class="tariff__unit">{L("від", "od")}</span>\n            ' if p.get('price') and p.get('from_') else ''
    if p.get('href'):
        btn = f'''<a href="{p['href']}" class="btn btn--dark">
            <span>{L(p['cta_uk'], p['cta_pl'])}</span>
            {ARROW}
          </a>'''
    else:
        btn = f'''<button type="button" class="btn btn--dark" data-open-popup>
            <span>{L(p['cta_uk'], p['cta_pl'])}</span>
            {ARROW}
          </button>'''
    return f'''        <article class="tariff-addon reveal">
          <div class="tariff-addon__price">
            {frm}{price_html(p, True)}
            {unit_html(p)}
          </div>
          <div class="tariff-addon__body">
            <h3 class="tariff-addon__name">
              <span class="tariff-addon__dot" aria-hidden="true"></span>
              <span>{L(p['name_uk'], p['name_pl'])}</span>
              <span class="tariff__tag tariff__tag--sm">{L(p['tag_uk'], p['tag_pl'])}</span>
            </h3>
            <p class="tariff-addon__desc">{L(p['desc_uk'], p['desc_pl'])}</p>
          </div>
          {btn}
        </article>

'''

def tariffs_block(title, tag, lead, plans, addons):
    return f'''    <section class="section" id="tariffs">
      <div class="container">
{head(title, tag)}
        <p class="tariff-lead reveal">{lead}</p>

        <div class="tariffs">
{''.join(plan_card(p) for p in plans)}        </div>

{''.join(addon(a) for a in addons)}      </div>
    </section>'''

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

def cases_block(slugs):
    return '''    <section class="section" id="cases">
      <div class="container">
''' + head(L('Приклади робіт', 'Przykładowe realizacje'), L('Кейси', 'Realizacje')) + '''
        <div class="cases reveal-group">
''' + ''.join(case_card(i, CASE[s]) for i, s in enumerate(slugs, 1)) + '''        </div>
      </div>
    </section>'''

def faq_block(qa, title=None, lead=None):
    items = ''.join(f'''          <div class="faq__item">
            <button type="button" class="faq__q" aria-expanded="false"><span class="faq__qn">(0{i})</span><span>{L(qu, qp)}</span><span class="faq__icon" aria-hidden="true"></span></button>
            <div class="faq__a"><p>{L(au, ap)}</p></div>
          </div>
''' for i, (qu, qp, au, ap) in enumerate(qa, 1))
    f = FAQ
    f1 = f.index('        <div class="faq reveal-group">') + len('        <div class="faq reveal-group">\n')
    f2 = f.index('        </div>\n      </div>\n    </section>')
    f = f[:f1] + items + f[f2:]
    if title:
        f = f.replace('<h2 class="section__title" data-i18n="faq.title">Питання та відповіді</h2>', '<h2 class="section__title">' + title + '</h2>')
    if lead:
        f = f.replace('<p class="section__lead" data-i18n="faq.desc">Не знайшли відповідь?<br>Напишіть нам у Telegram — відповімо швидко.</p>', '<p class="section__lead">' + lead + '</p>')
    return f

def services_block(items, title, tag, prefix='svc-', cta=None):
    arts = ''
    for i, s in enumerate(items, 1):
        arts += f'''          <article class="service" data-img="{s['img']}">
            <span class="service__num">(0{i})</span>
            <img class="service__img" src="{s['img']}" alt="" loading="lazy" />
            <div class="service__body">
              <h3 class="service__title"><a href="{prefix}{s['key']}">{L(s['name_uk'], s['name_pl'])}</a></h3>
              <p class="service__text">{L(s['sub_uk'], s['sub_pl'])}</p>
            </div>
            <a href="{prefix}{s['key']}" class="service__cta">
              <span>{cta or L('Детальніше', 'Szczegóły')}</span>
              {ARROW}
            </a>
          </article>

'''
    return f'''    <section class="section section--services" id="services">
      <div class="container">
{head(title, tag)}
        <div class="services reveal-group">
          <span class="service-preview" aria-hidden="true"></span>
{arts}        </div>
      </div>
    </section>'''

def write(name, body):
    html = nav_to_home(BEFORE + '\n\n'.join(body) + AFTER)
    open(os.path.join(TPL, name + '.html'), 'w').write(html)

def wm(uk, pl):
    return L(uk.replace(' ', '&nbsp;'), pl.replace(' ', '&nbsp;'))

