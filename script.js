/* ==========================================================================
   Web Shestakov — script.js
   i18n (UA/PL) · scroll reveals (IntersectionObserver) · header · FAQ · popup · forms
   No external dependencies — works offline and from file://
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------ Translations ------------------------------ */
  var I18N = {
    uk: {
      "meta.title": "Web Shestakov — сайти, Telegram-боти, інтернет-магазини, SEO та айдентика",
      "meta.description": "Створюємо сучасні сайти, Telegram-боти, інтернет-магазини, SEO-рішення та айдентику для бізнесу. Допомагаємо залучати клієнтів, продавати онлайн і автоматизувати процеси.",

      "nav.about": "Про нас",
      "nav.why": "Переваги",
      "nav.services": "Послуги",
      "nav.cases": "Кейси",
      "nav.budget": "Швидкий старт",
      "nav.tariffs": "Тарифи",
      "nav.faq": "FAQ",
      "nav.partners": "Партнерам",
      "nav.contacts": "Контакти",
      "nav.menu": "Меню",
      "menu.follow": "Соцмережі",
      "menu.contact": "Контакти",
      "menu.status": "Приймаємо проєкти",

      "cta.header": "Отримати консультацію",
      "widget.text": "Заявка",

      "hero.eyebrow": "Web Shestakov — digital-агенція",
      "hero.title": "Створюємо сайти, Telegram-боти та digital-рішення, які приводять клієнтів",
      "hero.subtitle": "Розробляємо сучасні сайти, інтернет-магазини, Telegram-боти, SEO-стратегії та айдентику для бізнесів, які хочуть виглядати професійно, продавати більше та автоматизувати процеси.",
      "hero.cta1": "Обговорити проєкт",
      "hero.cta2": "Подивитися послуги",
      "hero.aside.role": "digital-агенція",
      "hero.aside.cta": "Написати",
      "hero.trust": "Команда під ваш проєкт",
      "hero.kicker": "Створюємо",
      "hero.rot.1": "сайти",
      "hero.rot.2": "Telegram-боти",
      "hero.rot.3": "інтернет-магазини",
      "hero.rot.4": "SEO",
      "hero.rot.5": "айдентику",

      "badge.sites": "Сайти під ключ",
      "badge.bots": "Telegram-боти",
      "badge.shops": "Інтернет-магазини",
      "badge.seo": "SEO",
      "badge.identity": "Айдентика",

      "why.tag": "Переваги",
      "why.title": "Чому бізнеси обирають нас",
      "why.statement": "Ми не просто створюємо сайти — ми будуємо digital, що працює на ваш бізнес.",
      "why.desc": "Ми не просто створюємо красиві сайти. Ми продумуємо структуру, дизайн, функціонал і шлях клієнта так, щоб digital-рішення працювало на ваш бізнес.",
      "why.1.t": "Комплексний підхід",
      "why.1.d": "Беремо на себе весь процес: від ідеї, структури та дизайну до запуску, SEO та підтримки.",
      "why.2.t": "Рішення під бізнес-задачі",
      "why.2.d": "Аналізуємо нішу, аудиторію та цілі проєкту, щоб створити не шаблонний продукт, а ефективний інструмент.",
      "why.3.t": "Сучасний дизайн",
      "why.3.d": "Створюємо візуал, який виглядає професійно, викликає довіру та підкреслює цінність бренду.",
      "why.4.t": "Зручність для клієнтів",
      "why.4.d": "Проєктуємо логіку так, щоб користувачам було легко знайти інформацію, залишити заявку або зробити покупку.",
      "why.5.t": "Автоматизація процесів",
      "why.5.d": "Telegram-боти допомагають скоротити ручну роботу, швидше відповідати клієнтам і обробляти заявки.",
      "why.6.t": "Підтримка після запуску",
      "why.6.d": "Допомагаємо з оновленнями, правками, консультаціями та подальшим розвитком проєкту.",
      "why.1.k1": "Повний цикл", "why.1.k2": "SEO",
      "why.2.k1": "Аналіз ніші", "why.2.k2": "Цілі бізнесу",
      "why.3.k1": "Візуал", "why.3.k2": "Довіра",
      "why.4.k1": "UX", "why.4.k2": "Заявки",
      "why.5.k1": "Telegram-боти", "why.5.k2": "Швидкість",
      "why.6.k1": "Оновлення", "why.6.k2": "Розвиток",

      "budget.tag": "Швидкий старт",
      "budget.title": "Бюджетний запуск сайту",
      "budget.desc.l1": "Бюджетні сайти під ключ — коли треба швидко запустити бізнес,",
      "budget.desc.l2": "рекламу чи візитку без великих вкладень",
      "budget.cases.hint": "обери проєкт і відкрий його вживу",
      "budget.desc.more": "Це не шаблон, а сайт з індивідуальним дизайном, продуманою структурою, адаптацією під ваш бізнес і зрозумілою подачею послуг. Ми запускаємо такі сайти за 3–5 днів, щоб ви могли швидко стартувати з рекламою, презентувати компанію та отримувати заявки",
      "budget.desc2": "Це ідеальне рішення, якщо вам потрібно швидко показати бізнес, приймати заявки та запустити рекламу без великих вкладень.",
      "budget.note": "Ми беремо на себе структуру, дизайн, верстку, адаптацію під мобільні пристрої та базову підготовку до запуску реклами.",
      "budget.cta": "Запустити сайт",
      "budget.pill.1": "Для реклами",
      "budget.pill.2": "Для старту бізнесу",
      "budget.pill.3": "Візитка",
      "budget.pill.4": "Швидкий запуск",
      "budget.pill.5": "Без великих вкладень",
      "budget.plan1.name": "Сайт під ключ",
      "budget.plan1.desc": "Лаконічна сторінка з адаптивним дизайном, базовою структурою, контактами та формою заявки.",
      "budget.plan1.f1": "Адаптивний дизайн",
      "budget.plan1.f2": "Базова структура",
      "budget.plan1.f3": "Контакти та форма заявки",
      "budget.plan1.f4": "Готовність до реклами",
      "budget.plan2.name": "Сайт з адмін-панеллю",
      "budget.plan2.tag": "Повний контроль",
      "budget.plan2.desc": "Рішення для тих, хто хоче самостійно змінювати тексти, фото, послуги або інший контент після запуску.",
      "budget.plan2.f1": "Усе з тарифу 200€",
      "budget.plan2.f2": "Адмін-панель",
      "budget.plan2.f3": "Самостійне редагування контенту",
      "budget.plan2.f4": "Керування послугами",
      "budget.plan.cta": "Обрати формат",
      "budget.plan.unit": "під ключ",
      "budget.cases.tag": "Формати",
      "budget.cases.title": "Приклади наших сайтів",
      "budget.case1.t": "TD-SOLAR",
      "budget.case1.m": "Сонячна енергетика · Німеччина",
      "budget.case2.t": "Bellissimo Home",
      "budget.case2.m": "Меблі та інтер'єри · Польща",
      "budget.case3.t": "TARIK Invest",
      "budget.case3.m": "Електромонтаж · Чехія",
      "budget.seeTariffs": "Дивитися тарифи",

      "tariff.tag": "Ціни",
      "tariff.title": "Прозорі тарифи",
      "tariff.lead": "Фіксована вартість під ключ — без прихованих доплат. Оберіть формат, який найкраще підходить під вашу задачу",
      "tariff.unit.project": "/ проєкт",
      "tariff.unit.month": "/ місяць",
      "tariff.1.tag": "Запуск за 3 дні",
      "tariff.1.name": "Старт",
      "tariff.1.desc": "Базовий формат для швидкого запуску сайту, перевірки ідеї або старту реклами без зайвих ускладнень.",
      "tariff.1.f1": "Індивідуальний дизайн",
      "tariff.1.f2": "Адаптація під мобільні пристрої",
      "tariff.1.f3": "Базова SEO-оптимізація",
      "tariff.1.f4": "Форма заявки з відправкою в Telegram",
      "tariff.1.f5": "Допомога з текстами",
      "tariff.1.f6": "30 днів підтримки після запуску",
      "tariff.1.cta": "Замовити сайт",
      "tariff.2.tag": "Запуск за 4–5 днів",
      "tariff.2.badge": "Оптимальний вибір",
      "tariff.2.name": "Про",
      "tariff.2.desc": "Розширений формат для бізнесу, якому потрібен сильніший дизайн, більше функціоналу та зручне керування сайтом після запуску.",
      "tariff.2.f1": "Усе з тарифу «Старт»",
      "tariff.2.f2": "Більш деталізований дизайн",
      "tariff.2.f3": "Анімації та мікровзаємодії",
      "tariff.2.f4": "Розширена робота з текстами",
      "tariff.2.f5": "Підключення систем аналітики",
      "tariff.2.f6": "Адмін-панель для редагування контенту",
      "tariff.2.f7": "30 днів підтримки після запуску",
      "tariff.2.cta": "Обрати тариф",
      "tariff.3.name": "Підтримка",
      "tariff.3.tag": "Щомісяця",
      "tariff.3.desc": "Технічний супровід після запуску сайту: оновлення контенту, невеликі правки, консультації та допомога з обслуговуванням.",
      "tariff.3.cta": "Додати підтримку",

      "services.tag": "Послуги",
      "services.title": "Наші послуги",
      "services.desc": "Створюємо digital-інструменти, які допомагають бізнесу залучати клієнтів, продавати онлайн і виглядати сильніше за конкурентів.",
      "service.1.t": "Розробка сайтів",
      "service.1.d": "Створюємо лендинги, корпоративні сайти та багатосторінкові сайти під ключ. Продумуємо структуру, дизайн, адаптацію під мобільні пристрої та зручність для користувачів.",
      "service.1.cta": "Замовити сайт",
      "service.2.t": "Інтернет-магазини",
      "service.2.d": "Розробляємо онлайн-магазини для продажу товарів і послуг. Налаштовуємо каталог, картки товарів, кошик, форми замовлення та базові інтеграції.",
      "service.2.cta": "Створити магазин",
      "service.3.t": "Telegram-боти",
      "service.3.d": "Створюємо Telegram-боти для автоматизації заявок, консультацій, продажів, бронювань, внутрішніх процесів і підтримки клієнтів.",
      "service.3.cta": "Замовити бота",
      "service.4.t": "SEO-просування",
      "service.4.d": "Допомагаємо сайту краще індексуватися, залучати органічний трафік і отримувати більше потенційних клієнтів із пошуку.",
      "service.4.cta": "Покращити SEO",
      "service.5.t": "Айдентика",
      "service.5.d": "Розробляємо візуальний стиль бренду, який допомагає бізнесу виглядати впізнавано, професійно та цілісно.",
      "service.5.cta": "Створити айдентику",

      "cases.tag": "Кейси",
      "cases.title": "Наші кейси",
      "cases.tab.all": "Всі",
      "cases.tab.ecom": "Інтернет-магазини",
      "cases.tab.multi": "Багатосторінкові",
      "cases.tab.landing": "Лендинги",
      "cases.desc": "Кожен проєкт ми створюємо з урахуванням задач бізнесу, аудиторії та кінцевої цілі: заявки, продажі, автоматизація або впізнаваність бренду.",
      "case.label.task": "Задача",
      "case.label.did": "Що зробили",
      "case.label.result": "Результат",
      "case.1.meta": "Інтернет-магазин • Акаунти",
      "case.2.meta": "Інтернет-магазин • Дрони",
      "case.3.meta": "Інтернет-магазин • Парфуми",
      "case.4.meta": "Інтернет-магазин • Взуття",
      "case.5.meta": "Багатосторінковий • Нерухомість",
      "case.6.meta": "Багатосторінковий • Суші",
      "case.7.meta": "Багатосторінковий • Суші",
      "case.8.meta": "Багатосторінковий • Снеки",
      "case.9.meta": "Багатосторінковий • Лазери",
      "case.10.meta": "Багатосторінковий • Сонячні панелі",
      "case.11.meta": "Багатосторінковий • Декоративні панелі",
      "case.12.meta": "Лендинг • Курси відеомонтажу",
      "case.13.meta": "Лендинг • Бухгалтерія",
      "case.1.tag": "Лендинг",
      "case.1.t": "Лендинг для послуги",
      "case.1.task": "Створити сучасний сайт для презентації послуги та збору заявок.",
      "case.1.did": "Розробили структуру, дизайн, адаптивну версію та форму заявки.",
      "case.1.result": "Бізнес отримав зрозумілий сайт, який презентує послугу та веде клієнта до заявки.",
      "case.2.tag": "Telegram-бот",
      "case.2.t": "Telegram-бот для заявок",
      "case.2.task": "Автоматизувати прийом звернень від клієнтів.",
      "case.2.did": "Створили сценарій бота, кнопки, форму збору даних і передачу заявки адміністратору.",
      "case.2.result": "Клієнти можуть швидко залишати заявки, а бізнес — обробляти їх без зайвої ручної роботи.",
      "case.3.tag": "Магазин",
      "case.3.t": "Інтернет-магазин",
      "case.3.task": "Запустити онлайн-продаж товарів.",
      "case.3.did": "Створили каталог, картки товарів, кошик, сторінку оформлення замовлення та адаптивну версію.",
      "case.3.result": "Бізнес отримав повноцінний інструмент для продажів онлайн.",

      "faq.tag": "FAQ",
      "faq.title": "Питання та відповіді",
      "faq.desc": "Не знайшли відповідь?<br>Напишіть нам у Telegram — відповімо швидко.",
      "faq.1.q": "Скільки часу займає створення сайту?",
      "faq.1.a": "Термін залежить від складності проєкту. Простий лендинг можна реалізувати швидше, а інтернет-магазин або складний сайт потребує більше часу через структуру, дизайн, функціонал та інтеграції.",
      "faq.2.q": "Чи можна замовити сайт під ключ?",
      "faq.2.a": "Так. Ми можемо взяти на себе структуру, дизайн, розробку, адаптивність, форми заявок, базову SEO-оптимізацію та запуск.",
      "faq.3.q": "Ви створюєте Telegram-боти для бізнесу?",
      "faq.3.a": "Так. Ми розробляємо ботів для заявок, консультацій, продажів, бронювань, підтримки клієнтів та автоматизації внутрішніх процесів.",
      "faq.4.q": "Чи можна зробити інтернет-магазин?",
      "faq.4.a": "Так. Ми створюємо інтернет-магазини з каталогом товарів, картками, кошиком, оформленням замовлення та адаптацією під мобільні пристрої.",
      "faq.5.q": "Чи займаєтесь SEO?",
      "faq.5.a": "Так. Ми можемо провести базову SEO-оптимізацію сайту, підготувати структуру, мета-теги, рекомендації та покращити технічну основу для пошукового просування.",
      "faq.6.q": "Чи можна замовити тільки дизайн або айдентику?",
      "faq.6.a": "Так. Ви можете замовити окремо логотип, візуальний стиль, оформлення соцмереж або повну айдентику бренду.",
      "faq.7.q": "Як почати співпрацю?",
      "faq.7.a": "Напишіть нам у Telegram або Instagram, коротко опишіть задачу, і ми запропонуємо оптимальне рішення для вашого бізнесу.",

      "contact.tag": "Контакти",
      "form.title": "Готові запустити сайт, магазин або Telegram-бот?",
      "form.desc": "Залиште заявку, і ми зв’яжемося з вами, щоб обговорити задачу, формат проєкту, терміни та можливе рішення",
      "form.name": "Ім’я",
      "form.contact": "Телефон або Telegram",
      "form.need": "Що потрібно розробити?",
      "form.comment": "Коментар до проєкту",
      "form.submit": "Надіслати заявку",
      "form.agree": "Я даю згоду на обробку персональних даних відповідно до Політики конфіденційності",
      "form.ph.name": "Ваше ім’я",
      "form.ph.contact": "+48 ... або @username",
      "form.ph.comment": "Коротко опишіть задачу",
      "form.opt.choose": "Оберіть варіант",
      "form.opt.site": "Сайт",
      "form.opt.shop": "Інтернет-магазин",
      "form.opt.bot": "Telegram-бот",
      "form.opt.seo": "SEO",
      "form.opt.identity": "Айдентика",
      "form.opt.other": "Інше",
      "form.success": "Дякуємо! Ваша заявка надіслана. Ми скоро зв’яжемося з вами.",
      "form.error": "Будь ласка, заповніть обов’язкові поля.",
      "form.err.required": "Це поле обов’язкове",
      "form.err.agree": "Потрібно підтвердити згоду",

      "partners.tag": "Партнерам",
      "partners.title": "Партнерська пропозиція",
      "partners.desc": "Ми відкриті до партнерства з маркетологами, таргетологами, SMM-спеціалістами, дизайнерами, продюсерами, бізнес-консультантами та агенціями. Якщо ваші клієнти потребують сайт, інтернет-магазин, Telegram-бот, SEO або айдентику — ви можете передати їх нам і отримати партнерську винагороду.",
      "partners.who.title": "Для кого",
      "partners.who.1": "Маркетологи",
      "partners.who.2": "SMM-спеціалісти",
      "partners.who.3": "Таргетологи",
      "partners.who.4": "Дизайнери",
      "partners.who.5": "Фрилансери",
      "partners.who.6": "Агенції",
      "partners.who.7": "Бізнес-консультанти",
      "partners.adv.title": "Переваги",
      "partners.adv.1": "Прозорі умови співпраці",
      "partners.adv.2": "Якісна реалізація проєктів",
      "partners.adv.3": "Постійний контакт по статусу роботи",
      "partners.adv.4": "Можливість довгострокової співпраці",
      "partners.adv.5": "Винагорода за переданого клієнта",
      "partners.advdesc.1": "Фіксуємо ставки й відсоток винагороди на старті — без прихованих правок і несподіванок під час роботи.",
      "partners.advdesc.2": "Ваш клієнт отримує сайт, магазин чи бот того ж рівня, що й наші власні проєкти — акуратний код, дизайн і терміни.",
      "partners.advdesc.3": "Тримаємо вас у курсі кожного етапу: узгодження, проміжні версії, запуск — ви завжди знаєте стадію проєкту.",
      "partners.advdesc.4": "Працюємо не на одну угоду: передавайте клієнтів регулярно й отримуйте винагороду з кожного нового проєкту.",
      "partners.advdesc.5": "Виплачуємо відсоток за кожного клієнта, який дійшов до оплати — прозоро і вчасно, одразу після старту проєкту.",
      "partners.cta": "Стати партнером",

      "footer.desc": "Web Shestakov — створюємо сайти, інтернет-магазини, Telegram-боти, SEO-рішення та айдентику для бізнесів, які хочуть розвиватися онлайн.",
      "footer.menu": "Меню",
      "footer.contacts": "Контакти",
      "footer.cta": "Написати в Telegram",
      "footer.big": "Обговоримо ваш проєкт?",
      "footer.copyright": "© Web Shestakov. Усі права захищені.",
      "footer.privacy": "політика конфіденційності",
      "footer.consent": "згода на обробку персональних даних",
      "footer.offer": "публічна оферта"
    },

    pl: {
      "meta.title": "Web Shestakov — strony internetowe, boty Telegram, sklepy online, SEO i identyfikacja wizualna",
      "meta.description": "Tworzymy nowoczesne strony internetowe, boty Telegram, sklepy online, rozwiązania SEO i identyfikację wizualną dla firm. Pomagamy pozyskiwać klientów, sprzedawać online i automatyzować procesy.",

      "nav.about": "O nas",
      "nav.why": "Korzyści",
      "nav.services": "Usługi",
      "nav.cases": "Case studies",
      "nav.budget": "Szybki start",
      "nav.tariffs": "Cennik",
      "nav.faq": "FAQ",
      "nav.partners": "Partnerzy",
      "nav.contacts": "Kontakt",
      "nav.menu": "Menu",
      "menu.follow": "Social",
      "menu.contact": "Kontakt",
      "menu.status": "Przyjmujemy projekty",

      "cta.header": "Uzyskać konsultację",
      "widget.text": "Zgłoszenie",

      "hero.eyebrow": "Web Shestakov — agencja digital",
      "hero.title": "Tworzymy strony internetowe, boty Telegram i rozwiązania digital, które pozyskują klientów",
      "hero.subtitle": "Projektujemy nowoczesne strony, sklepy internetowe, boty Telegram, strategie SEO oraz identyfikację wizualną dla firm, które chcą wyglądać profesjonalnie, sprzedawać więcej i automatyzować procesy.",
      "hero.cta1": "Omówić projekt",
      "hero.cta2": "Zobaczyć usługi",
      "hero.aside.role": "agencja digital",
      "hero.aside.cta": "Napisać",
      "hero.trust": "Zespół pod Twój projekt",
      "hero.kicker": "Tworzymy",
      "hero.rot.1": "strony",
      "hero.rot.2": "boty Telegram",
      "hero.rot.3": "sklepy online",
      "hero.rot.4": "SEO",
      "hero.rot.5": "identyfikację",

      "badge.sites": "Strony pod klucz",
      "badge.bots": "Boty Telegram",
      "badge.shops": "Sklepy internetowe",
      "badge.seo": "SEO",
      "badge.identity": "Identyfikacja wizualna",

      "why.tag": "Korzyści",
      "why.title": "Dlaczego firmy wybierają nas",
      "why.statement": "Nie tworzymy tylko stron — budujemy digital, który pracuje na Twój biznes.",
      "why.desc": "Nie tworzymy tylko ładnych stron. Projektujemy strukturę, design, funkcjonalność i ścieżkę klienta tak, aby rozwiązanie digital realnie wspierało Twój biznes.",
      "why.1.t": "Kompleksowe podejście",
      "why.1.d": "Bierzemy na siebie cały proces: od pomysłu, struktury i designu po wdrożenie, SEO i wsparcie.",
      "why.2.t": "Rozwiązania pod cele biznesowe",
      "why.2.d": "Analizujemy niszę, odbiorców i cele projektu, aby stworzyć skuteczne narzędzie, a nie przypadkowy szablon.",
      "why.3.t": "Nowoczesny design",
      "why.3.d": "Tworzymy wizualny styl, który wygląda profesjonalnie, buduje zaufanie i podkreśla wartość marki.",
      "why.4.t": "Wygoda dla klientów",
      "why.4.d": "Projektujemy logikę strony tak, aby użytkownik łatwo znalazł informacje, wysłał zapytanie lub dokonał zakupu.",
      "why.5.t": "Automatyzacja procesów",
      "why.5.d": "Boty Telegram pomagają ograniczyć ręczną pracę, szybciej odpowiadać klientom i obsługiwać zgłoszenia.",
      "why.6.t": "Wsparcie po uruchomieniu",
      "why.6.d": "Pomagamy przy aktualizacjach, poprawkach, konsultacjach i dalszym rozwoju projektu.",
      "why.1.k1": "Pełny cykl", "why.1.k2": "SEO",
      "why.2.k1": "Analiza niszy", "why.2.k2": "Cele biznesu",
      "why.3.k1": "Wizual", "why.3.k2": "Zaufanie",
      "why.4.k1": "UX", "why.4.k2": "Zgłoszenia",
      "why.5.k1": "Boty Telegram", "why.5.k2": "Szybkość",
      "why.6.k1": "Aktualizacje", "why.6.k2": "Rozwój",

      "budget.tag": "Szybki start",
      "budget.title": "Budżetowe uruchomienie strony",
      "budget.desc.l1": "Budżetowe strony pod klucz — gdy trzeba szybko uruchomić biznes,",
      "budget.desc.l2": "reklamę lub wizytówkę bez dużych nakładów",
      "budget.cases.hint": "wybierz projekt i otwórz go na żywo",
      "budget.desc.more": "To nie szablon, lecz strona z indywidualnym designem, przemyślaną strukturą, dopasowaniem do Twojego biznesu i czytelną prezentacją usług. Uruchamiamy takie strony w 3–5 dni, byś mógł szybko wystartować z reklamą, zaprezentować firmę i zbierać zapytania",
      "budget.desc2": "To idealne rozwiązanie, gdy trzeba szybko pokazać biznes, przyjmować zgłoszenia i uruchomić reklamę bez dużych nakładów.",
      "budget.note": "Bierzemy na siebie strukturę, projekt, kodowanie, dostosowanie do urządzeń mobilnych i podstawowe przygotowanie do startu reklamy.",
      "budget.cta": "Uruchom stronę",
      "budget.pill.1": "Do reklamy",
      "budget.pill.2": "Na start biznesu",
      "budget.pill.3": "Wizytówka",
      "budget.pill.4": "Szybki start",
      "budget.pill.5": "Bez dużych nakładów",
      "budget.plan1.name": "Strona pod klucz",
      "budget.plan1.desc": "Zwięzła strona z responsywnym projektem, podstawową strukturą, kontaktami i formularzem zgłoszeń.",
      "budget.plan1.f1": "Responsywny projekt",
      "budget.plan1.f2": "Podstawowa struktura",
      "budget.plan1.f3": "Kontakty i formularz",
      "budget.plan1.f4": "Gotowość do reklamy",
      "budget.plan2.name": "Strona z panelem admina",
      "budget.plan2.tag": "Pełna kontrola",
      "budget.plan2.desc": "Rozwiązanie dla tych, którzy chcą samodzielnie zmieniać teksty, zdjęcia, usługi i inne treści po uruchomieniu.",
      "budget.plan2.f1": "Wszystko z taryfy 200€",
      "budget.plan2.f2": "Panel administracyjny",
      "budget.plan2.f3": "Samodzielna edycja treści",
      "budget.plan2.f4": "Zarządzanie usługami",
      "budget.plan.cta": "Wybierz format",
      "budget.plan.unit": "pod klucz",
      "budget.cases.tag": "Formaty",
      "budget.cases.title": "Przykłady naszych stron",
      "budget.case1.t": "TD-SOLAR",
      "budget.case1.m": "Energetyka słoneczna · Niemcy",
      "budget.case2.t": "Bellissimo Home",
      "budget.case2.m": "Meble i wnętrza · Polska",
      "budget.case3.t": "TARIK Invest",
      "budget.case3.m": "Instalacje elektryczne · Czechy",
      "budget.seeTariffs": "Zobacz cennik",

      "tariff.tag": "Cennik",
      "tariff.title": "Przejrzysty cennik",
      "tariff.lead": "Stała cena pod klucz — bez ukrytych dopłat. Wybierz format, który najlepiej pasuje do Twojego zadania",
      "tariff.unit.project": "/ projekt",
      "tariff.unit.month": "/ miesiąc",
      "tariff.1.tag": "Start w 3 dni",
      "tariff.1.name": "Start",
      "tariff.1.desc": "Podstawowy format do szybkiego uruchomienia strony, sprawdzenia pomysłu lub startu reklamy bez zbędnych komplikacji.",
      "tariff.1.f1": "Indywidualny projekt graficzny",
      "tariff.1.f2": "Adaptacja pod urządzenia mobilne",
      "tariff.1.f3": "Podstawowa optymalizacja SEO",
      "tariff.1.f4": "Formularz z wysyłką do Telegrama",
      "tariff.1.f5": "Pomoc z tekstami",
      "tariff.1.f6": "30 dni wsparcia po starcie",
      "tariff.1.cta": "Zamów stronę",
      "tariff.2.tag": "Start w 4–5 dni",
      "tariff.2.badge": "Optymalny wybór",
      "tariff.2.name": "Pro",
      "tariff.2.desc": "Rozszerzony format dla biznesu, który potrzebuje mocniejszego designu, większej funkcjonalności i wygodnego zarządzania stroną po starcie.",
      "tariff.2.f1": "Wszystko z taryfy „Start”",
      "tariff.2.f2": "Bardziej dopracowany design",
      "tariff.2.f3": "Animacje i mikrointerakcje",
      "tariff.2.f4": "Rozszerzona praca z tekstami",
      "tariff.2.f5": "Podłączenie systemów analityki",
      "tariff.2.f6": "Panel admina do edycji treści",
      "tariff.2.f7": "30 dni wsparcia po starcie",
      "tariff.2.cta": "Wybierz taryfę",
      "tariff.3.name": "Wsparcie",
      "tariff.3.tag": "Co miesiąc",
      "tariff.3.desc": "Wsparcie techniczne po uruchomieniu strony: aktualizacje treści, drobne poprawki, konsultacje i pomoc w obsłudze.",
      "tariff.3.cta": "Dodaj wsparcie",

      "services.tag": "Usługi",
      "services.title": "Nasze usługi",
      "services.desc": "Tworzymy narzędzia digital, które pomagają firmom pozyskiwać klientów, sprzedawać online i wyglądać lepiej niż konkurencja.",
      "service.1.t": "Tworzenie stron internetowych",
      "service.1.d": "Tworzymy landing page, strony firmowe i rozbudowane serwisy pod klucz. Projektujemy strukturę, design, wersję mobilną i wygodę użytkownika.",
      "service.1.cta": "Zamówić stronę",
      "service.2.t": "Sklepy internetowe",
      "service.2.d": "Tworzymy sklepy online do sprzedaży produktów i usług. Konfigurujemy katalog, karty produktów, koszyk, formularze zamówień i podstawowe integracje.",
      "service.2.cta": "Stworzyć sklep",
      "service.3.t": "Boty Telegram",
      "service.3.d": "Tworzymy boty Telegram do automatyzacji zgłoszeń, konsultacji, sprzedaży, rezerwacji, procesów wewnętrznych i obsługi klientów.",
      "service.3.cta": "Zamówić bota",
      "service.4.t": "Pozycjonowanie SEO",
      "service.4.d": "Pomagamy stronie lepiej indeksować się w wyszukiwarkach, pozyskiwać ruch organiczny i zdobywać więcej potencjalnych klientów.",
      "service.4.cta": "Poprawić SEO",
      "service.5.t": "Identyfikacja wizualna",
      "service.5.d": "Projektujemy styl wizualny marki, który pomaga firmie wyglądać rozpoznawalnie, profesjonalnie i spójnie.",
      "service.5.cta": "Stworzyć identyfikację",

      "cases.tag": "Case studies",
      "cases.title": "Nasze realizacje",
      "cases.tab.all": "Wszystkie",
      "cases.tab.ecom": "Sklepy internetowe",
      "cases.tab.multi": "Wielostronicowe",
      "cases.tab.landing": "Landing page",
      "cases.desc": "Każdy projekt tworzymy z uwzględnieniem celów biznesowych, odbiorców i końcowego rezultatu: zapytań, sprzedaży, automatyzacji lub rozpoznawalności marki.",
      "case.label.task": "Cel",
      "case.label.did": "Co zrobiliśmy",
      "case.label.result": "Rezultat",
      "case.1.meta": "Sklep internetowy • Konta",
      "case.2.meta": "Sklep internetowy • Drony",
      "case.3.meta": "Sklep internetowy • Perfumy",
      "case.4.meta": "Sklep internetowy • Obuwie",
      "case.5.meta": "Strona wielostronicowa • Nieruchomości",
      "case.6.meta": "Strona wielostronicowa • Sushi",
      "case.7.meta": "Strona wielostronicowa • Sushi",
      "case.8.meta": "Strona wielostronicowa • Przekąski",
      "case.9.meta": "Strona wielostronicowa • Lasery",
      "case.10.meta": "Strona wielostronicowa • Panele słoneczne",
      "case.11.meta": "Strona wielostronicowa • Panele dekoracyjne",
      "case.12.meta": "Landing page • Kursy montażu wideo",
      "case.13.meta": "Landing page • Księgowość",
      "case.1.tag": "Landing page",
      "case.1.t": "Landing page dla usługi",
      "case.1.task": "Stworzyć nowoczesną stronę do prezentacji usługi i zbierania zapytań.",
      "case.1.did": "Opracowaliśmy strukturę, design, wersję responsywną i formularz kontaktowy.",
      "case.1.result": "Firma otrzymała czytelną stronę, która prezentuje usługę i prowadzi klienta do wysłania zapytania.",
      "case.2.tag": "Bot Telegram",
      "case.2.t": "Bot Telegram do zgłoszeń",
      "case.2.task": "Zautomatyzować przyjmowanie zapytań od klientów.",
      "case.2.did": "Stworzyliśmy scenariusz bota, przyciski, formularz zbierania danych i przekazywanie zgłoszenia administratorowi.",
      "case.2.result": "Klienci mogą szybko zostawiać zgłoszenia, a firma obsługuje je bez zbędnej pracy ręcznej.",
      "case.3.tag": "Sklep",
      "case.3.t": "Sklep internetowy",
      "case.3.task": "Uruchomić sprzedaż produktów online.",
      "case.3.did": "Stworzyliśmy katalog, karty produktów, koszyk, stronę składania zamówienia i wersję responsywną.",
      "case.3.result": "Firma otrzymała pełne narzędzie do sprzedaży online.",

      "faq.tag": "FAQ",
      "faq.title": "Pytania i odpowiedzi",
      "faq.desc": "Nie znalazłeś odpowiedzi?<br>Napisz do nas na Telegramie — odpowiemy szybko.",
      "faq.1.q": "Ile czasu zajmuje stworzenie strony?",
      "faq.1.a": "Czas realizacji zależy od złożoności projektu. Prosty landing page można przygotować szybciej, a sklep internetowy lub bardziej rozbudowana strona wymaga więcej czasu ze względu na strukturę, design, funkcjonalność i integracje.",
      "faq.2.q": "Czy można zamówić stronę pod klucz?",
      "faq.2.a": "Tak. Możemy zająć się strukturą, designem, wdrożeniem, responsywnością, formularzami kontaktowymi, podstawową optymalizacją SEO i uruchomieniem.",
      "faq.3.q": "Czy tworzycie boty Telegram dla firm?",
      "faq.3.a": "Tak. Tworzymy boty do zgłoszeń, konsultacji, sprzedaży, rezerwacji, obsługi klientów i automatyzacji procesów wewnętrznych.",
      "faq.4.q": "Czy można stworzyć sklep internetowy?",
      "faq.4.a": "Tak. Tworzymy sklepy internetowe z katalogiem produktów, kartami produktów, koszykiem, składaniem zamówienia i wersją mobilną.",
      "faq.5.q": "Czy zajmujecie się SEO?",
      "faq.5.a": "Tak. Możemy wykonać podstawową optymalizację SEO strony, przygotować strukturę, meta tagi, rekomendacje i poprawić techniczną bazę pod pozycjonowanie.",
      "faq.6.q": "Czy można zamówić tylko design lub identyfikację wizualną?",
      "faq.6.a": "Tak. Możesz zamówić osobno logo, styl wizualny, materiały do social media lub pełną identyfikację wizualną marki.",
      "faq.7.q": "Jak rozpocząć współpracę?",
      "faq.7.a": "Napisz do nas na Telegramie lub Instagramie, krótko opisz zadanie, a zaproponujemy najlepsze rozwiązanie dla Twojego biznesu.",

      "contact.tag": "Kontakt",
      "form.title": "Gotowy uruchomić stronę, sklep lub bota Telegram?",
      "form.desc": "Zostaw zgłoszenie, a skontaktujemy się z Tobą, aby omówić zadanie, format projektu, terminy i możliwe rozwiązanie",
      "form.name": "Imię",
      "form.contact": "Telefon lub Telegram",
      "form.need": "Co chcesz stworzyć?",
      "form.comment": "Komentarz do projektu",
      "form.submit": "Wyślij zgłoszenie",
      "form.agree": "Wyrażam zgodę na przetwarzanie danych osobowych zgodnie z Polityką prywatności",
      "form.ph.name": "Twoje imię",
      "form.ph.contact": "+48 ... lub @username",
      "form.ph.comment": "Krótko opisz zadanie",
      "form.opt.choose": "Wybierz opcję",
      "form.opt.site": "Strona internetowa",
      "form.opt.shop": "Sklep internetowy",
      "form.opt.bot": "Bot Telegram",
      "form.opt.seo": "SEO",
      "form.opt.identity": "Identyfikacja wizualna",
      "form.opt.other": "Inne",
      "form.success": "Dziękujemy! Twoje zgłoszenie zostało wysłane. Wkrótce się z Tobą skontaktujemy.",
      "form.error": "Proszę wypełnić wymagane pola.",
      "form.err.required": "To pole jest wymagane",
      "form.err.agree": "Wymagana jest akceptacja zgody",

      "partners.tag": "Partnerzy",
      "partners.title": "Oferta partnerska",
      "partners.desc": "Jesteśmy otwarci na współpracę z marketerami, specjalistami od reklam, SMM, designerami, producentami, konsultantami biznesowymi i agencjami. Jeśli Twoi klienci potrzebują strony, sklepu internetowego, bota Telegram, SEO lub identyfikacji wizualnej — możesz przekazać ich nam i otrzymać wynagrodzenie partnerskie.",
      "partners.who.title": "Dla kogo",
      "partners.who.1": "Marketerzy",
      "partners.who.2": "Specjaliści SMM",
      "partners.who.3": "Specjaliści od reklam",
      "partners.who.4": "Designerzy",
      "partners.who.5": "Freelancerzy",
      "partners.who.6": "Agencje",
      "partners.who.7": "Konsultanci biznesowi",
      "partners.adv.title": "Korzyści",
      "partners.adv.1": "Przejrzyste warunki współpracy",
      "partners.adv.2": "Jakościowa realizacja projektów",
      "partners.adv.3": "Stały kontakt w sprawie statusu prac",
      "partners.adv.4": "Możliwość długoterminowej współpracy",
      "partners.adv.5": "Wynagrodzenie za przekazanego klienta",
      "partners.advdesc.1": "Ustalamy stawki i procent wynagrodzenia na starcie — bez ukrytych zmian i niespodzianek w trakcie pracy.",
      "partners.advdesc.2": "Twój klient otrzymuje stronę, sklep lub bota na tym samym poziomie co nasze własne projekty — czysty kod, design i terminy.",
      "partners.advdesc.3": "Informujemy o każdym etapie: uzgodnienia, wersje pośrednie, uruchomienie — zawsze znasz status projektu.",
      "partners.advdesc.4": "Pracujemy nie na jedną transakcję: przekazuj klientów regularnie i otrzymuj wynagrodzenie z każdego nowego projektu.",
      "partners.advdesc.5": "Wypłacamy procent za każdego klienta, który dochodzi do płatności — przejrzyście i na czas, zaraz po starcie projektu.",
      "partners.cta": "Zostać partnerem",

      "footer.desc": "Web Shestakov — tworzymy strony internetowe, sklepy online, boty Telegram, rozwiązania SEO i identyfikację wizualną dla firm, które chcą rozwijać się online.",
      "footer.menu": "Menu",
      "footer.contacts": "Kontakt",
      "footer.cta": "Napisać na Telegramie",
      "footer.big": "Porozmawiajmy o Twoim projekcie?",
      "footer.copyright": "© Web Shestakov. Wszelkie prawa zastrzeżone.",
      "footer.privacy": "polityka prywatności",
      "footer.consent": "zgoda na przetwarzanie danych osobowych",
      "footer.offer": "oferta publiczna"
    }
  };

  var STORE_KEY = "ws-lang";
  var currentLang = "uk";

  function t(key) {
    var dict = I18N[currentLang] || I18N.uk;
    return dict[key] != null ? dict[key] : (I18N.uk[key] != null ? I18N.uk[key] : key);
  }

  function applyLang(lang) {
    if (!I18N[lang]) lang = "uk";
    currentLang = lang;

    document.documentElement.setAttribute("lang", lang);
    try { localStorage.setItem(STORE_KEY, lang); } catch (e) {}

    // Text nodes
    var nodes = document.querySelectorAll("[data-i18n]");
    nodes.forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      var val = t(key);
      if (el.tagName === "TITLE") {
        el.textContent = val;
      } else if (el.tagName === "META") {
        el.setAttribute("content", val);
      } else if (val.indexOf("<br") !== -1) {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    });

    // Attributes (e.g. placeholder)
    var attrNodes = document.querySelectorAll("[data-i18n-attr]");
    attrNodes.forEach(function (el) {
      var pairs = el.getAttribute("data-i18n-attr").split(",");
      pairs.forEach(function (pair) {
        var parts = pair.split(":");
        if (parts.length === 2) {
          el.setAttribute(parts[0].trim(), t(parts[1].trim()));
        }
      });
    });

    // Active state on all lang switchers
    document.querySelectorAll(".lang__btn").forEach(function (btn) {
      var isActive = btn.getAttribute("data-lang") === lang;
      btn.classList.toggle("is-active", isActive);
      btn.setAttribute("aria-pressed", isActive ? "true" : "false");
    });

    // Re-split any word-reveal statements after their text was set
    splitWords();
  }

  // Wrap each word of a [data-split] element in a span for staggered reveal.
  function splitWords() {
    document.querySelectorAll("[data-split]").forEach(function (el) {
      var text = el.textContent.trim();
      if (!text) return;
      el.textContent = "";
      var words = text.split(/\s+/);
      words.forEach(function (w, i) {
        var span = document.createElement("span");
        span.className = "word";
        span.style.setProperty("--i", i);
        span.textContent = w;
        el.appendChild(span);
        if (i < words.length - 1) el.appendChild(document.createTextNode(" "));
      });
    });
  }

  function initLangSwitch() {
    var saved = "uk";
    try { saved = localStorage.getItem(STORE_KEY) || "uk"; } catch (e) {}

    document.querySelectorAll(".lang__btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var lang = btn.getAttribute("data-lang");
        if (lang === currentLang) return;
        document.body.classList.add("lang-switching");
        applyLang(lang);
        window.setTimeout(function () { document.body.classList.remove("lang-switching"); }, 400);
      });
    });

    applyLang(saved);
  }

  /* ------------------------------ Preloader ------------------------------
     Handled by preloader.js (GSAP "Signal Reveal" timeline + inline head
     failsafe in index.html). Nothing to do here. */

  /* ------------------------------ Header behavior ------------------------------ */
  function initHeader() {
    var header = document.getElementById("header");
    if (!header) return;
    var lastY = window.pageYOffset;
    var ticking = false;

    function update() {
      var y = window.pageYOffset;
      header.classList.toggle("is-scrolled", y > 20);
      if (y > lastY && y > 260) {
        header.classList.add("is-hidden");
      } else {
        header.classList.remove("is-hidden");
      }
      lastY = y;
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ------------------------------ Mobile menu ------------------------------ */
  function initMobileMenu() {
    var menu = document.getElementById("mobile-menu");
    var burger = document.getElementById("burger");
    var close = document.getElementById("menu-close");
    if (!menu || !burger) return;

    function open() {
      menu.classList.add("is-open");
      menu.setAttribute("aria-hidden", "false");
      burger.setAttribute("aria-expanded", "true");
      document.body.classList.add("is-locked");
    }
    function shut() {
      menu.classList.remove("is-open");
      menu.setAttribute("aria-hidden", "true");
      burger.setAttribute("aria-expanded", "false");
      document.body.classList.remove("is-locked");
    }

    burger.addEventListener("click", open);
    if (close) close.addEventListener("click", shut);
    menu.querySelectorAll("[data-close-menu]").forEach(function (el) {
      el.addEventListener("click", shut);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) shut();
    });
  }

  /* ------------------------------ FAQ accordion ------------------------------ */
  function initFaq() {
    var items = document.querySelectorAll(".faq__item");
    items.forEach(function (item) {
      var q = item.querySelector(".faq__q");
      var a = item.querySelector(".faq__a");
      if (!q || !a) return;

      q.addEventListener("click", function () {
        var isOpen = item.classList.contains("is-open");

        // Close siblings
        items.forEach(function (other) {
          if (other !== item && other.classList.contains("is-open")) {
            other.classList.remove("is-open");
            other.querySelector(".faq__q").setAttribute("aria-expanded", "false");
            other.querySelector(".faq__a").style.height = "0px";
          }
        });

        if (isOpen) {
          item.classList.remove("is-open");
          q.setAttribute("aria-expanded", "false");
          a.style.height = "0px";
        } else {
          item.classList.add("is-open");
          q.setAttribute("aria-expanded", "true");
          a.style.height = a.scrollHeight + "px";
        }
      });
    });

    // Keep open item height correct on resize / lang change
    window.addEventListener("resize", function () {
      document.querySelectorAll(".faq__item.is-open .faq__a").forEach(function (a) {
        a.style.height = a.scrollHeight + "px";
      });
    });
  }

  /* ------------------------------ Popup ------------------------------ */
  function initPopup() {
    var popup = document.getElementById("popup");
    if (!popup) return;
    var lastFocused = null;

    function open() {
      lastFocused = document.activeElement;
      popup.classList.add("is-open");
      popup.setAttribute("aria-hidden", "false");
      document.body.classList.add("is-locked");
      var first = popup.querySelector("input, select, textarea, button");
      if (first) window.setTimeout(function () { first.focus(); }, 260);
    }
    function shut() {
      popup.classList.remove("is-open");
      popup.setAttribute("aria-hidden", "true");
      document.body.classList.remove("is-locked");
      if (lastFocused && lastFocused.focus) lastFocused.focus();
    }

    document.querySelectorAll("[data-open-popup]").forEach(function (btn) {
      btn.addEventListener("click", open);
    });
    popup.querySelectorAll("[data-close-popup]").forEach(function (el) {
      el.addEventListener("click", shut);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && popup.classList.contains("is-open")) shut();
      // Simple focus trap
      if (e.key === "Tab" && popup.classList.contains("is-open")) {
        var focusables = popup.querySelectorAll('a[href], button:not([disabled]), input, select, textarea');
        if (!focusables.length) return;
        var first = focusables[0];
        var last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* ------------------------------ Forms + validation ------------------------------ */
  function initForms() {
    var forms = document.querySelectorAll(".form");
    forms.forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var valid = true;

        // Required text/select fields
        form.querySelectorAll("[required]").forEach(function (input) {
          if (input.type === "checkbox") {
            var box = input.closest(".checkbox");
            var err = form.querySelector(".field__error--checkbox");
            if (!input.checked) {
              valid = false;
              if (err) err.classList.add("is-shown");
            } else if (err) {
              err.classList.remove("is-shown");
            }
            return;
          }
          var field = input.closest(".field");
          var empty = !input.value.trim();
          if (field) field.classList.toggle("is-invalid", empty);
          if (empty) valid = false;
        });

        form.classList.remove("is-success", "is-error");
        if (valid) {
          form.classList.add("is-success");
          form.reset();
          form.querySelectorAll(".field.is-invalid").forEach(function (f) { f.classList.remove("is-invalid"); });
          var errChk = form.querySelector(".field__error--checkbox");
          if (errChk) errChk.classList.remove("is-shown");
          window.setTimeout(function () { form.classList.remove("is-success"); }, 6000);
        } else {
          form.classList.add("is-error");
        }
      });

      // Clear error on input
      form.querySelectorAll(".field__input").forEach(function (input) {
        input.addEventListener("input", function () {
          var field = input.closest(".field");
          if (field && input.value.trim()) field.classList.remove("is-invalid");
          form.classList.remove("is-error");
        });
      });
      form.querySelectorAll('input[type="checkbox"]').forEach(function (chk) {
        chk.addEventListener("change", function () {
          if (chk.checked) {
            var err = form.querySelector(".field__error--checkbox");
            if (err) err.classList.remove("is-shown");
          }
        });
      });
    });
  }

  /* ------------------------------ Floating widget + sticky CTA ------------------------------ */
  function initFloating() {
    var widget = document.querySelector(".floating-widget");
    var sticky = document.querySelector(".sticky-cta");
    var hero = document.getElementById("home");
    var footer = document.querySelector(".footer");
    var heroH = hero ? hero.offsetHeight : 400;

    function update() {
      var y = window.pageYOffset;
      var show = y > heroH * 0.6;
      // Hide when footer visible
      if (footer) {
        var fRect = footer.getBoundingClientRect();
        if (fRect.top < window.innerHeight - 40) show = false;
      }
      if (widget) widget.classList.toggle("is-visible", show);
      if (sticky) sticky.classList.toggle("is-visible", show);
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", function () { heroH = hero ? hero.offsetHeight : 400; update(); });
    update();
  }

  /* ------------------------------ Active nav highlight ------------------------------ */
  function initActiveNav() {
    var links = document.querySelectorAll(".nav__link");
    var map = {};
    links.forEach(function (l) {
      var id = l.getAttribute("href").replace("#", "");
      var sec = document.getElementById(id);
      if (sec) map[id] = l;
    });
    var ids = Object.keys(map);
    if (!ids.length || !("IntersectionObserver" in window)) return;

    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          links.forEach(function (l) { l.classList.remove("is-active"); });
          var active = map[entry.target.id];
          if (active) active.classList.add("is-active");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px", threshold: 0 });

    ids.forEach(function (id) { obs.observe(document.getElementById(id)); });
  }

  /* ------------------------------ Case media fallback ------------------------------
     If a case screenshot fails to load, swap the broken img for a branded
     placeholder instead of leaving an empty white block. */
  function initCaseMedia() {
    document.querySelectorAll(".case__media img, .bx-card__media img").forEach(function (img) {
      function fail() {
        var media = img.parentNode;
        if (!media || media.querySelector(".case__media-fallback")) return;
        img.style.display = "none";
        var f = document.createElement("span");
        f.className = "case__media-fallback";
        f.textContent = img.getAttribute("alt") || "Web Shestakov";
        media.appendChild(f);
      }
      if (img.complete && img.naturalWidth === 0) { fail(); return; }
      img.addEventListener("error", fail);
    });
  }

  /* ------------------------------ Reveal animations (IntersectionObserver) ------------------------------ */
  function initReveal() {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // Reduced motion or no IntersectionObserver support -> show everything instantly.
    if (reduce || !("IntersectionObserver" in window)) {
      revealAll();
      return;
    }

    // Smooth CSS transitions for the reveal.
    // .service-preview is a hover overlay with its own transition — leave it alone.
    document.querySelectorAll(".reveal, .reveal-group > *").forEach(function (el) {
      if (el.classList.contains("service-preview")) return;
      el.style.transition = "opacity 0.8s cubic-bezier(0.16,1,0.3,1), transform 0.8s cubic-bezier(0.16,1,0.3,1)";
    });

    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        if (el.classList.contains("reveal-group")) {
          Array.prototype.forEach.call(el.children, function (kid, i) {
            kid.style.transitionDelay = (i * 90) + "ms";
            kid.classList.add("is-in");
          });
        } else {
          el.classList.add("is-in");
        }
        obs.unobserve(el);
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.08 });

    document.querySelectorAll(".reveal, .reveal-group").forEach(function (el) { obs.observe(el); });

    // Reveal anything already in view on load (covers the hero / above-the-fold).
    window.requestAnimationFrame(function () {
      document.querySelectorAll(".reveal, .reveal-group").forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.92) {
          if (el.classList.contains("reveal-group")) {
            Array.prototype.forEach.call(el.children, function (kid, i) {
              kid.style.transitionDelay = (i * 90) + "ms";
              kid.classList.add("is-in");
            });
          } else {
            el.classList.add("is-in");
          }
        }
      });
    });
  }

  /* ------------------------------ Smooth anchor scroll ------------------------------ */
  function initAnchors() {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener("click", function (e) {
        var id = link.getAttribute("href");
        if (id === "#" || id.length < 2) return;
        var target = document.querySelector(id);
        if (!target) return;
        e.preventDefault();
        var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        target.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      });
    });
  }

  /* ------------------------------ Typewriter (hero rotating word) ------------------------------ */
  function initTypewriter() {
    var host = document.querySelector("[data-rotate]");
    if (!host) return;
    var wordEl = host.querySelector(".hero__rotate-word");
    if (!wordEl) return;

    var keys = ["hero.rot.1", "hero.rot.2", "hero.rot.3", "hero.rot.4", "hero.rot.5"];
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (reduce) { wordEl.textContent = t(keys[0]); return; }

    var i = 0, ch = 0, deleting = false;

    function tick() {
      var full = t(keys[i]);
      if (!deleting) {
        ch++;
        wordEl.textContent = full.slice(0, ch);
        if (ch >= full.length) { deleting = true; return window.setTimeout(tick, 1600); }
        return window.setTimeout(tick, 70);
      } else {
        ch--;
        wordEl.textContent = full.slice(0, ch);
        if (ch <= 0) { deleting = false; i = (i + 1) % keys.length; return window.setTimeout(tick, 260); }
        return window.setTimeout(tick, 38);
      }
    }
    wordEl.textContent = "";
    window.setTimeout(tick, 500);
  }

  /* ------------------------------ Init ------------------------------ */
  function revealAll() {
    // Failsafe: make every reveal element visible no matter what.
    document.documentElement.classList.remove("anim-on");
    document.querySelectorAll(".reveal, .reveal-group > *").forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  function initWhyAccordion() {
    var acc = document.querySelector(".why-acc");
    if (!acc) return;
    var cards = Array.prototype.slice.call(acc.querySelectorAll(".wa-card"));
    if (!cards.length) return;

    function open(card) {
      cards.forEach(function (c) {
        var on = c === card;
        c.classList.toggle("wa-card--open", on);
        c.setAttribute("aria-expanded", on ? "true" : "false");
      });
    }

    cards.forEach(function (card) {
      card.setAttribute("role", "button");
      card.setAttribute("tabindex", "0");
      card.setAttribute("aria-expanded", card.classList.contains("wa-card--open") ? "true" : "false");
      card.addEventListener("click", function () { open(card); });
      card.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
          e.preventDefault();
          open(card);
        }
      });
    });
  }

  /* ------------------------------ Services: cursor-following image reveal ------------------------------ */
  function initServiceReveal() {
    var list = document.querySelector(".services");
    var preview = list && list.querySelector(".service-preview");
    if (!list || !preview) return;

    // Skip on touch devices (no hover) and when reduced motion is requested.
    if (window.matchMedia("(hover: none)").matches) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    var services = Array.prototype.slice.call(list.querySelectorAll(".service"));
    var mx = 0, my = 0, cx = 0, cy = 0; // target vs current (lerped) coords
    var active = false, raf = null, primed = false, curSrc = null;

    // Preload the images so the first hover doesn't flash.
    function prime() {
      if (primed) return;
      primed = true;
      services.forEach(function (s) {
        var src = s.getAttribute("data-img");
        if (src) { var img = new Image(); img.src = src; }
      });
    }

    function loop() {
      cx += (mx - cx) * 0.16;
      cy += (my - cy) * 0.16;
      preview.style.left = cx + "px";
      preview.style.top = cy + "px";
      if (active || Math.abs(mx - cx) > 0.5 || Math.abs(my - cy) > 0.5) {
        raf = window.requestAnimationFrame(loop);
      } else {
        raf = null;
      }
    }

    function start() { if (!raf) raf = window.requestAnimationFrame(loop); }

    // Which service row (if any) sits under the given viewport point.
    function rowAt(x, y) {
      for (var i = 0; i < services.length; i++) {
        var r = services[i].getBoundingClientRect();
        if (x >= r.left && x <= r.right && y >= r.top && y <= r.bottom) return services[i];
      }
      return null;
    }

    function follow(e) {
      var r = list.getBoundingClientRect();
      mx = e.clientX - r.left;
      my = e.clientY - r.top;
    }

    function show(row, e) {
      var src = row.getAttribute("data-img");
      if (!src) return;
      follow(e);
      if (!active) { cx = mx; cy = my; } // snap to cursor so it never flies in from a corner
      if (src !== curSrc) { curSrc = src; preview.style.backgroundImage = 'url("' + src + '")'; }
      if (!active) { active = true; preview.classList.add("is-active"); }
      start();
    }

    function hide() {
      if (!active) return;
      active = false; curSrc = null;
      preview.classList.remove("is-active");
      start();
    }

    // The preview lives and dies with the container: it only shows while the
    // cursor is inside .services (over a row) and vanishes the moment it leaves.
    list.addEventListener("pointerenter", function (e) {
      if (e.pointerType === "touch") return;
      prime();
    });

    list.addEventListener("pointermove", function (e) {
      if (e.pointerType === "touch") return;
      prime();
      var row = rowAt(e.clientX, e.clientY);
      if (row) { show(row, e); }
      else if (active) { follow(e); start(); }
    });

    list.addEventListener("pointerleave", hide);
    list.addEventListener("pointercancel", hide);

    // Safety net: if a fast move or an overlapping layer swallows pointerleave,
    // hide as soon as the cursor is anywhere outside the container's box.
    window.addEventListener("pointermove", function (e) {
      if (!active) return;
      var r = list.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) hide();
    }, { passive: true });
    window.addEventListener("scroll", function () { if (active) hide(); }, { passive: true });
  }

  /* ------------------------------ Cases: category tabs + pagination ------------------------------ */
  function initCasesFilter() {
    var grid = document.getElementById("cases-grid");
    var pager = document.getElementById("cases-pager");
    var section = document.getElementById("cases");
    var tabs = Array.prototype.slice.call(document.querySelectorAll(".cases-tab"));
    if (!grid || !pager || !tabs.length) return;

    var cards = Array.prototype.slice.call(grid.querySelectorAll(".case"));
    var PER = 6;
    var filter = "all";
    var page = 1;
    var firstRender = true;

    function pad(n) { return ("0" + n).slice(-2); }

    function filtered() {
      return cards.filter(function (c) {
        return filter === "all" || c.getAttribute("data-cat") === filter;
      });
    }

    function render() {
      var list = filtered();
      var pages = Math.max(1, Math.ceil(list.length / PER));
      if (page > pages) page = pages;
      var startI = (page - 1) * PER;

      cards.forEach(function (c) { c.classList.add("is-hidden"); });

      list.forEach(function (c, i) {
        if (i < startI || i >= startI + PER) return;
        c.classList.remove("is-hidden");
        var num = c.querySelector(".case__num");
        if (num) num.textContent = "(" + pad(i + 1) + ")";
        if (!firstRender) {
          c.classList.remove("is-enter");
          void c.offsetWidth; // reflow to restart the entrance animation
          c.classList.add("is-enter");
        }
      });

      buildPager(pages);
      firstRender = false;
    }

    function chevron(dir) {
      return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="' +
        (dir === "prev" ? "M15 18l-6-6 6-6" : "M9 18l6-6-6-6") + '"/></svg>';
    }

    function goTo(p) {
      page = p;
      render();
      if (section && section.scrollIntoView) section.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    function buildPager(pages) {
      pager.innerHTML = "";
      if (pages <= 1) return;

      var prev = document.createElement("button");
      prev.type = "button"; prev.className = "cases-pager__btn"; prev.innerHTML = chevron("prev");
      prev.setAttribute("aria-label", "Попередня сторінка");
      prev.disabled = page === 1;
      prev.addEventListener("click", function () { if (page > 1) goTo(page - 1); });
      pager.appendChild(prev);

      for (var p = 1; p <= pages; p++) {
        (function (p) {
          var b = document.createElement("button");
          b.type = "button";
          b.className = "cases-pager__btn" + (p === page ? " is-active" : "");
          b.textContent = pad(p);
          b.setAttribute("aria-label", "Сторінка " + p);
          if (p === page) b.setAttribute("aria-current", "page");
          b.addEventListener("click", function () { if (p !== page) goTo(p); });
          pager.appendChild(b);
        })(p);
      }

      var next = document.createElement("button");
      next.type = "button"; next.className = "cases-pager__btn"; next.innerHTML = chevron("next");
      next.setAttribute("aria-label", "Наступна сторінка");
      next.disabled = page === pages;
      next.addEventListener("click", function () { if (page < pages) goTo(page + 1); });
      pager.appendChild(next);
    }

    tabs.forEach(function (t) {
      t.addEventListener("click", function () {
        var f = t.getAttribute("data-filter");
        if (f === filter) return;
        filter = f;
        page = 1;
        tabs.forEach(function (x) { x.classList.remove("is-active"); x.setAttribute("aria-selected", "false"); });
        t.classList.add("is-active");
        t.setAttribute("aria-selected", "true");
        render();
      });
    });

    render();
  }

  /* ------------------------------ Budget case switcher ------------------------------ */
  function initCaseSwitch() {
    var root = document.querySelector(".case-switch");
    if (!root) return;
    var dots = Array.prototype.slice.call(root.querySelectorAll(".case-dots__dot"));
    var slides = Array.prototype.slice.call(root.querySelectorAll(".case-slide"));

    function go(n) {
      if (root.getAttribute("data-active") === n) return;
      root.setAttribute("data-active", n);
      dots.forEach(function (dot) {
        var on = dot.getAttribute("data-go") === n;
        dot.classList.toggle("is-active", on);
        dot.setAttribute("aria-selected", on ? "true" : "false");
      });
      slides.forEach(function (s) {
        s.classList.toggle("is-active", s.getAttribute("data-slide") === n);
      });
    }

    dots.forEach(function (dot) {
      dot.addEventListener("click", function () { go(dot.getAttribute("data-go")); });
    });

    var arrows = Array.prototype.slice.call(root.querySelectorAll(".case-dots__arrow"));
    arrows.forEach(function (arrow) {
      arrow.addEventListener("click", function () {
        var dir = parseInt(arrow.getAttribute("data-dir"), 10) || 1;
        var n = (parseInt(root.getAttribute("data-active"), 10) || 1) + dir;
        if (n < 1) n = slides.length;
        if (n > slides.length) n = 1;
        go(String(n));
      });
    });
  }

  function init() {
    // Independent try/catch per module so one failure never blanks the page.
    var steps = [initLangSwitch, initHeader, initMobileMenu,
      initFaq, initPopup, initForms, initFloating, initActiveNav, initAnchors, initTypewriter, initReveal, initWhyAccordion, initServiceReveal, initCasesFilter, initCaseSwitch, initCaseMedia];
    for (var i = 0; i < steps.length; i++) {
      try { steps[i](); } catch (e) { if (window.console) console.error("[ws] init step failed:", e); }
    }
    window.__wsReady = true;
  }

  function boot() {
    try {
      init();
    } catch (e) {
      if (window.console) console.error("[ws] init failed, revealing content:", e);
      revealAll();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
