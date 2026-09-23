# Генерує src/templates/about.html з блоків головної (home.html). Запуск: python3 scripts/build_about.py
import re
import os
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'templates') + '/'
s=open(ROOT+'home.html').read()
def L(uk,pl): return f'<span data-lang-block="uk">{uk}</span><span data-lang-block="pl" hidden>{pl}</span>'
ARROW='<span class="btn__play" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12"><path d="M7 17L17 7M17 7H8M17 7v9" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
def head(title,tag,id_=''):
    return f'''        <div class="section__head section__head--split reveal">
          <h2 class="section__title">{title}</h2>
          <span class="section__rule" aria-hidden="true"></span>
          <span class="eyebrow"><span class="eyebrow__dot eyebrow__dot--square"></span><span>{tag}</span></span>
        </div>
'''
def cut(src,start,end_marker):
    a=src.index(start); b=src.index(end_marker,a); return a,b

# --- head: drop preloader scripts
s=re.sub(r'\n    /\* Preloader guards.*?\}\)\(\);\n','\n',s,flags=re.S)
s=s.replace('  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>\n','')
s=s.replace('  <script src="preloader.js" defer></script>\n','')
s=re.sub(r'  <!-- GSAP drives the preloader.*?-->\n','',s,flags=re.S)
a=s.index('  <div class="preloader" id="preloader"'); b=s.index('  <header class="header" id="header">')
s=s[:a]+s[b:]

# --- hero (reuse home hero, new texts)
a=s.index('    <section class="hero" id="home">'); b=s.index('</section>',a)+len('</section>')
hero=s[a:b]
hero=hero.replace('<div class="hero__wordmark">Web&nbsp;Shestakov<span class="hero__reg">&reg;</span></div>',
  '<div class="hero__wordmark">'+L('Про&nbsp;нас','O&nbsp;nas')+'<span class="hero__reg">&reg;</span></div>')
o1=hero.index('<div class="hero__overlay">'); o2=hero.index('<!-- Bottom service shelf')
hero=hero[:o1]+'''<div class="hero__overlay">
            <h1 class="hero__headline">'''+L('Web Shestakov — веб-студія у Вроцлаві','Web Shestakov — studio stron internetowych we Wrocławiu')+'''</h1>
            <p class="hero__headline-sub">'''+L('Сайти, інтернет-магазини й Telegram-боти для бізнесу в Польщі, Україні та ЄС. 12+ років досвіду.','Strony, sklepy internetowe i boty Telegram dla firm w Polsce, Ukrainie i UE. Ponad 12 lat doświadczenia.')+'''</p>
          </div>

          '''+hero[o2:]
stats=[('12+','років у веб-розробці','lat doświadczenia'),('35+','реалізованих проєктів','zrealizowanych projektów'),('6','країн клієнтів','krajów klientów'),('3–5','днів на лендінг','dni na landing page'),('24 год','максимум на відповідь','maks. czas odpowiedzi')]
def card(i,st,dup):
    n,uk,pl=st
    extra=' shelf__card--dup" aria-hidden="true" tabindex="-1' if dup else ''
    return f'''              <a href="#how" class="shelf__card{extra}">
                <span class="shelf__thumb shelf__thumb--{i}" aria-hidden="true"></span>
                <span class="shelf__meta"><span class="shelf__num">({n})</span><span class="shelf__name">{L(uk,pl)}</span></span>
              </a>
'''
t1=hero.index('<div class="shelf__track">')+len('<div class="shelf__track">\n'); t2=hero.index('            </div>\n          </div>\n        </div>',t1)
hero=hero[:t1]+''.join(card(i+1,st,False) for i,st in enumerate(stats))+''.join(card(i+1,st,True) for i,st in enumerate(stats))+hero[t2:]

# --- services (copy from home as is)
a2=s.index('    <section class="section section--services" id="services">'); services=s[a2:s.index('</section>',a2)+len('</section>')]
# --- tariffs (copy) + extra addons
a3=s.index('    <section class="section" id="tariffs">'); tariffs=s[a3:s.index('</section>',a3)+len('</section>')]
addon_tpl='''        <article class="tariff-addon reveal">
          <div class="tariff-addon__price">
            <span class="tariff__price tariff__price--sm">{price}</span>
            <span class="tariff__unit">{unit}</span>
          </div>
          <div class="tariff-addon__body">
            <h3 class="tariff-addon__name">
              <span class="tariff-addon__dot" aria-hidden="true"></span>
              <span>{name}</span>
              <span class="tariff__tag tariff__tag--sm">{tag}</span>
            </h3>
            <p class="tariff-addon__desc">{desc}</p>
          </div>
          <button type="button" class="btn btn--dark" data-open-popup>
            <span>{cta}</span>
            '''+ARROW+'''
          </button>
        </article>

'''
extra=addon_tpl.format(price='<span class="plan-card__cur">$</span>800',unit=L('/ від','/ od'),name=L('Інтернет-магазин','Sklep internetowy'),tag=L('20–30 роб. днів','20–30 dni rob.'),
  desc=L('Каталог, кошик, онлайн-оплата, доставка, CRM та інтеграції. Складні магазини й сервіси з кастомним функціоналом — 30–45+ робочих днів.','Katalog, koszyk, płatności online, dostawa, CRM i integracje. Złożone sklepy i serwisy z niestandardowymi funkcjami — 30–45+ dni roboczych.'),
  cta=L('Замовити магазин','Zamów sklep'))
extra+=addon_tpl.format(price=L('Інд.','Indyw.'),unit=L('оцінка','wycena'),name=L('Telegram-бот і складні сервіси','Bot Telegram i złożone systemy'),tag=L('оцінка за 24 год','wycena w 24 h'),
  desc=L('Точну вартість і термін рахуємо після короткого брифу — оцінку надсилаємо протягом 24 годин.','Dokładną cenę i termin liczymy po krótkim briefie — wycenę wysyłamy w ciągu 24 godzin.'),
  cta=L('Отримати оцінку','Otrzymaj wycenę'))
k=tariffs.index('        <article class="tariff-addon reveal">')
note='''        <p class="tariff-lead reveal">'''+L('Працюємо офіційно: за договором і з рахунком-фактурою (faktura). Оплата поетапна — в EUR, USD або PLN.','Działamy oficjalnie: na podstawie umowy i faktury. Płatność etapami — w EUR, USD lub PLN. Ceny nie zawierają VAT (sprzedawca zwolniony z VAT).')+'''</p>
'''
tariffs=tariffs[:k]+extra+tariffs[k:]
tariffs=tariffs.replace('<p class="tariff-lead reveal" data-i18n="tariff.lead">Фіксована вартість під ключ — без прихованих доплат. Оберіть формат, який найкраще підходить під вашу задачу</p>','<p class="tariff-lead reveal">'+L('Фіксована вартість під ключ — без прихованих доплат. Працюємо офіційно: за договором і з faktura, оплата поетапна в EUR, USD або PLN.','Stała cena pod klucz — bez ukrytych dopłat. Działamy oficjalnie: umowa i faktura, płatność etapami w EUR, USD lub PLN. Ceny bez VAT (zwolnienie z VAT).')+'</p>')

# --- who we are (budget-grid pattern from home)
pills=[('Українська','Polski'),('Polski','Українська'),('WordPress','WordPress'),('Webflow','Webflow'),('React · Next.js','React · Next.js'),('SEO','SEO')]
pl_html=''.join(f'<span class="budget-pill" role="listitem">{L(u,p)}</span>' for u,p in pills)+''.join(f'<span class="budget-pill" aria-hidden="true">{L(u,p)}</span>' for u,p in pills)
who='''    <section class="section" id="who">
      <div class="container">
'''+head(L('Хто ми','Kim jesteśmy'),L('Про нас','O nas'))+'''
        <div class="budget-grid">
        <div class="budget-intro reveal">
          <p class="budget-lead">'''+L('Я роблю сайти понад 12 років. У 2018 році переїхав до Польщі й вирішив розвивати студію саме тут — так з\'явився Web Shestakov, який працює вже понад 6 років.','Tworzę strony internetowe od ponad 12 lat. W 2018 roku przeprowadziłem się do Polski i postanowiłem rozwijać studio właśnie tutaj — tak powstał Web Shestakov, który działa już ponad 6 lat.')+'''</p>
          <p class="budget-sub">'''+L('Під кожен проєкт збираємо команду: дизайнер, графічний дизайнер, розробник і SEO-спеціаліст. Ви говорите напряму з тим, хто робить ваш сайт — без менеджерів і зіпсованого телефону. Ціна відома наперед, запуск — у погоджений строк, а після здачі сайт повністю ваш.','Do każdego projektu dobieramy zespół: projektant, grafik, programista i specjalista SEO. Rozmawiasz bezpośrednio z osobą, która robi Twoją stronę — bez pośredników i głuchego telefonu. Cenę znasz z góry, start jest w ustalonym terminie, a po oddaniu projektu strona w całości należy do Ciebie.')+'''</p>
          <div class="budget-pills" role="list">
            <div class="budget-pills__track">'''+pl_html+'''</div>
          </div>
          <a href="#contact" class="btn btn--dark btn--lg budget-intro__btn">
            <span>'''+L('Обговорити проєкт','Porozmawiajmy o projekcie')+'''</span>
            '''+ARROW+'''
          </a>
        </div>
        <div class="reveal">
          <a class="bx-card" href="https://t.me/Andrii_DEV9" target="_blank" rel="noopener" aria-label="Telegram Andrii Shestakov">
            <div class="bx-card__media"><img src="assets/photo.webp" alt="Andrii Shestakov — Founder &amp; CEO Web Shestakov" loading="lazy" style="object-position: center 38%" /></div>
            <div class="bx-card__bar">
              <span class="bx-card__cat">Andrii Shestakov · Founder &amp; CEO</span>
              <span class="bx-card__cta" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path d="M7 17L17 7M17 7H8M17 7v9" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </div>
          </a>
        </div>
        </div>
      </div>
    </section>'''

# --- how we work: why-acc with 6 steps
steps=[('Заявка і розмова','Zapytanie i rozmowa','Ви описуєте задачу, ми уточнюємо формат, функціонал, мови та інтеграції.','Opisujesz zadanie, a my doprecyzowujemy format, funkcje, języki i integracje.',('Бриф','Brief'),('Формат','Format')),
 ('Бриф і матеріали','Brief i materiały','Тексти, фото, логотип, приклади, що подобаються. Якщо структури ще немає — допоможемо її скласти.','Teksty, zdjęcia, logo, przykłady, które Ci się podobają. Jeśli nie masz struktury — pomożemy ją ułożyć.',('Контент','Treści'),('Структура','Struktura')),
 ('Структура і дизайн','Struktura i projekt','Спершу погоджуємо структуру, потім 1–2 перші блоки дизайну — і тільки тоді рухаємося далі.','Najpierw zatwierdzamy strukturę, potem 1–2 pierwsze sekcje projektu — dopiero wtedy idziemy dalej.',('UX','UX'),('Дизайн','Projekt')),
 ('Розробка','Wdrożenie','WordPress, Webflow, React, Next.js або чистий код. Підключаємо форми, CMS, калькулятори, аналітику й оплату.','WordPress, Webflow, React, Next.js albo czysty kod. Podłączamy formularze, CMS, kalkulatory, analitykę i płatności.',('CMS','CMS'),('Інтеграції','Integracje')),
 ('Перевірка і правки','Sprawdzenie i poprawki','Ви перевіряєте готовий сайт і надсилаєте правки одним списком — так швидше і без плутанини.','Sprawdzasz gotową stronę i przesyłasz poprawki jedną listą — szybciej i bez zamieszania.',('Тести','Testy'),('Правки','Poprawki')),
 ('Запуск і передача','Start i przekazanie','Підключаємо домен, хостинг і пошту, запускаємо сайт і передаємо вам усі доступи. За потреби — відеоінструкція.','Podłączamy domenę, hosting i pocztę, uruchamiamy stronę i przekazujemy Ci wszystkie dostępy. W razie potrzeby — instrukcja wideo.',('Домен','Domena'),('Доступи','Dostępy'))]
cards=''
for i,(tu,tp,du,dp,k1,k2) in enumerate(steps,1):
    op=' wa-card--open' if i==1 else ''
    cards+=f'''          <article class="wa-card{op}">
            <div class="wa-num"><span class="wa-num__label">{L('Етап','Etap')}</span><span class="wa-num__line"></span><span class="wa-num__idx">(0{i})</span></div>
            <div class="wa-content">
              <div class="wa-image"><img src="assets/why-{i}.webp" alt="" loading="lazy" /></div>
              <h3 class="wa-content__title">{L(tu,tp)}</h3>
              <p class="wa-content__text">{L(du,dp)}</p>
              <div class="wa-tags"><span class="wa-tag">{L(*k1)}</span><span class="wa-tag">{L(*k2)}</span></div>
            </div>
            <div class="wa-vert"><h3>{L(tu,tp)}</h3></div>
          </article>

'''
how='''    <section class="section" id="how">
      <div class="container">
        <div class="wa-head reveal">
          <h2 class="wa-head__title">'''+L('Як ми працюємо','Jak pracujemy')+'''</h2>
          <span class="wa-head__divider" aria-hidden="true"></span>
          <span class="wa-head__tag"><span class="wa-head__dot" aria-hidden="true"></span><span>'''+L('Процес','Proces')+'''</span></span>
        </div>

        <div class="why-acc reveal">
'''+cards+'''        </div>
      </div>
    </section>'''

# --- FAQ (about-specific)
a4=s.index('    <section class="section section--soft" id="faq">'); faq=s[a4:s.index('</section>',a4)+len('</section>')]
qa=[('Кому належить сайт після запуску?','Do kogo należy strona po starcie?','Вам. Ви отримуєте всі доступи до сайту, домену, хостингу, CMS і підключених сервісів. Домен і хостинг бажано одразу оформлювати на вас.','Do Ciebie. Otrzymujesz wszystkie dostępy do strony, domeny, hostingu, CMS i podłączonych usług. Domenę i hosting najlepiej od razu rejestrować na Ciebie.'),
 ('Як відбувається оплата?','Jak wygląda płatność?','Офіційно: за договором і з faktura. Оплата поетапна: перший платіж — перед стартом, наступний — після погодженого етапу або перед запуском. Валюта — EUR, USD або PLN.','Oficjalnie: na podstawie umowy i faktury. Płatność etapami: pierwsza wpłata przed startem, kolejna po zatwierdzonym etapie lub przed uruchomieniem. Waluta — EUR, USD lub PLN.'),
 ('Скільки триває розробка?','Ile trwa realizacja?','Лендінг — 3–5 днів, багатосторінковий сайт — 15–25 робочих днів, інтернет-магазин — 20–30 робочих днів. Термін Telegram-бота визначаємо після оцінки функціоналу.','Landing page — 3–5 dni, strona wielostronicowa — 15–25 dni roboczych, sklep internetowy — 20–30 dni roboczych. Termin bota Telegram ustalamy po wycenie funkcji.'),
 ('Чи допомагаєте з доменом, хостингом і рекламою?','Czy pomagacie z domeną, hostingiem i reklamą?','Так. Підберемо й підключимо домен, хостинг, SSL, корпоративну пошту та аналітику. Допоможемо з Google Business Profile і запуском реклами або підключимо профільного спеціаліста.','Tak. Dobierzemy i podłączymy domenę, hosting, SSL, pocztę firmową i analitykę. Pomożemy z Profilem Firmy w Google i startem reklam albo podłączymy specjalistę.'),
 ('Які проєкти ви не берете?','Jakich projektów nie realizujecie?','Коли треба скопіювати чужий сайт 1:1, стартувати без погодженого завдання, постійно змінювати затверджену структуру без перегляду бюджету або вмістити великий новий функціонал у вже погоджену фіксовану ціну.','Gdy trzeba skopiować cudzą stronę 1:1, zacząć bez uzgodnionego zakresu, ciągle zmieniać zatwierdzoną strukturę bez zmiany budżetu albo zmieścić dużą nową funkcjonalność w ustalonej, stałej cenie.'),
 ('Як швидко ви відповідаєте?','Jak szybko odpowiadacie?','Зазвичай за кілька годин у робочий час, максимум — 24 години. Працюємо з понеділка по п\'ятницю; на повідомлення ввечері чи у вихідні відповідаємо наступного робочого дня.','Zwykle w ciągu kilku godzin w godzinach pracy, najpóźniej w 24 godziny. Pracujemy od poniedziałku do piątku; na wiadomości wieczorem lub w weekend odpowiadamy następnego dnia roboczego.'),
 ('Де ви знаходитесь і якими мовами говорите?','Gdzie jesteście i w jakich językach rozmawiacie?','Студія працює у Вроцлаві (Польща), NIP 8961659922, REGON 543289997. Спілкуємося українською та польською, клієнти — у Польщі, Україні, Німеччині, Чехії, Нідерландах і США.','Studio działa we Wrocławiu, NIP 8961659922, REGON 543289997. Rozmawiamy po polsku i po ukraińsku, a klientów mamy w Polsce, Ukrainie, Niemczech, Czechach, Holandii i USA.')]
items=''.join(f'''          <div class="faq__item">
            <button type="button" class="faq__q" aria-expanded="false"><span class="faq__qn">(0{i})</span><span>{L(qu,qp)}</span><span class="faq__icon" aria-hidden="true"></span></button>
            <div class="faq__a"><p>{L(au,ap)}</p></div>
          </div>
''' for i,(qu,qp,au,ap) in enumerate(qa,1))
f1=faq.index('        <div class="faq reveal-group">')+len('        <div class="faq reveal-group">\n'); f2=faq.index('        </div>\n      </div>\n    </section>')
faq=faq[:f1]+items+faq[f2:]
faq=faq.replace('<h2 class="section__title" data-i18n="faq.title">Питання та відповіді</h2>','<h2 class="section__title">'+L('Як ми співпрацюємо','Jak współpracujemy')+'</h2>')

# --- assemble: replace hero..partners(end) with new sections + contact
a5=s.index('    <section class="section" id="contact">'); contact=s[a5:s.index('</section>',a5)+len('</section>')]
start=s.index('    <section class="hero" id="home">'); pe=s.index('    <section class="section" id="partners">'); end=s.index('</section>',pe)+len('</section>')
body='\n\n'.join([hero,who,services,how,tariffs,faq,contact])
s=s[:start]+body+s[end:]
# nav hashes -> home (except #contact and local shelf #how)
s=re.sub(r'href="#(about|why|services|cases|budget|tariffs|faq|partners|home)"',r'href="index.html#\1"',s)
open(ROOT+'about.html','w').write(s)
print('ok', len(s))
