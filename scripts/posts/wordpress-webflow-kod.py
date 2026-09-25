# Стаття блогу. Автор: Andrii Shestakov. Поля й формат — див. scripts/build_blog.py.

POST = {'key': 'wordpress-webflow-kod',
 'path_uk': '/blog/wordpress-webflow-chy-kod/',
 'path_pl': '/pl/blog/wordpress-webflow-czy-kod/',
 'img': 'assets/why-4.webp',
 'title_uk': 'WordPress, Webflow чи код: на чому робити сайт у 2026 | SHSTKV Digital',
 'title_pl': 'WordPress, Webflow czy strona pisana od zera? Wybór 2026',
 'desc_uk': 'На чому зробити сайт у 2026: WordPress, Webflow чи код на Next.js. Чесно про плюси й мінуси, витрати щомісяця, хто чим володіє і як ми обираємо платформу.',
 'desc_pl': 'WordPress, Webflow czy strona pisana od zera w Next.js? Uczciwie o plusach i minusach, kosztach utrzymania, własności strony i o tym, jak dobieramy platformę.',
 'h1_uk': 'WordPress, Webflow чи код: на чому робити сайт',
 'h1_pl': 'WordPress, Webflow czy strona pisana od zera',
 'sub_uk': 'Порівнюємо три підходи, якими працюємо щодня, і пояснюємо, як обрати свій.',
 'sub_pl': 'Porównujemy trzy technologie, na których pracujemy na co dzień, i podpowiadamy, jak wybrać.',
 'topic_uk': 'Платформи',
 'topic_pl': 'Platformy',
 'minutes': 8,
 'answer_uk': 'Універсальної відповіді немає. WordPress підходить, коли потрібні гнучкість, магазин на WooCommerce і дешевий хостинг. Webflow — для маркетингових і корпоративних сайтів, які команда '
              'редагує сама без розробника. Код на React чи Next.js — коли важливі максимальна швидкість і нестандартна логіка. Tilda й Wix годяться для простих сторінок, але обмежують ріст.',
 'answer_pl': 'Nie ma jednej dobrej odpowiedzi. WordPress sprawdza się, gdy liczy się elastyczność, sklep na WooCommerce i tani hosting. Webflow — przy stronach firmowych i marketingowych, które '
              'zespół edytuje sam, bez programisty. Kod w React lub Next.js — gdy kluczowe są szybkość i nietypowa logika. Kreatory typu Wix wystarczą na prostą wizytówkę, ale ograniczają rozwój.',
 'sections': [{'h2_uk': 'Чому питання «на чому робити сайт» таке важливе',
               'h2_pl': 'Dlaczego wybór technologii ma znaczenie',
               'blocks': [('p',
                           'Платформа визначає не лише те, як сайт виглядає на старті. Від неї залежить, хто й скільки коштуватиме вам за правки, скільки ви платитимете щомісяця і чи зможете через '
                           'два роки додати магазин, другу мову або калькулятор без переробки з нуля.',
                           'Technologia to nie tylko kwestia startu. Od niej zależy, kto i za ile będzie wprowadzał zmiany, ile zapłacisz co miesiąc za utrzymanie i czy za dwa lata dodasz sklep, '
                           'drugą wersję językową albo kalkulator bez stawiania strony od nowa.'),
                          ('p',
                           'За 12+ років ми бачили обидві крайнощі: простий сайт-візитку, «прикручений» до важкого WordPress із тридцятьма плагінами, і складний сервіс, який намагалися втиснути в '
                           'конструктор. Обидва варіанти закінчувалися переробкою. Тому ми не маємо «улюбленої» платформи — працюємо на WordPress (Bricks), WooCommerce, Webflow і чистому коді з '
                           'React та Next.js і обираємо під задачу.',
                           'Przez ponad 12 lat widzieliśmy obie skrajności: prostą wizytówkę na ciężkim WordPressie z trzydziestoma wtyczkami i rozbudowany serwis upchnięty na siłę w kreatorze. W obu '
                           'przypadkach kończyło się przebudową. Dlatego nie mamy „ulubionej” platformy — pracujemy na WordPressie (Bricks), WooCommerce, Webflow oraz w czystym kodzie z React i '
                           'Next.js, a wybór zależy od projektu.')]},
              {'h2_uk': 'WordPress: гнучкість і плагіни, але потрібен догляд',
               'h2_pl': 'WordPress: elastyczność i wtyczki, ale wymaga opieki',
               'blocks': [('p',
                           'WordPress — найпоширеніша CMS у світі, і це її головна сила: під будь-яку задачу є плагін, а розробника знайти легко. Ми збираємо сайти в конструкторі Bricks — він дає '
                           'чистіший код і кращу швидкість, ніж популярні «важкі» білдери. Для магазинів використовуємо WooCommerce: каталог, кошик, оплати, доставка.',
                           'WordPress to najpopularniejszy CMS na świecie i w tym tkwi jego siła: na niemal każdy problem jest wtyczka, a wykonawcę łatwo znaleźć. Strony budujemy w Bricks — daje '
                           'czystszy kod i lepszą wydajność niż popularne, ciężkie page buildery. Sklepy stawiamy na WooCommerce: katalog, koszyk, płatności (np. BLIK), dostawa (np. InPost).'),
                          ('ul',
                           [('Плюси: гнучкість, тисячі плагінів, дешевий хостинг, повний контроль над файлами й базою.',
                             'Plusy: elastyczność, tysiące wtyczek, tani hosting, pełna kontrola nad plikami i bazą danych.'),
                            ('Плюси: зручна адмінка — тексти, фото, товари клієнт змінює сам.', 'Plusy: wygodny panel — teksty, zdjęcia i produkty klient zmienia sam.'),
                            ('Мінуси: ядро, тему й плагіни треба регулярно оновлювати, інакше зростає ризик злому.',
                             'Minusy: rdzeń, motyw i wtyczki trzeba regularnie aktualizować, inaczej rośnie ryzyko włamania.'),
                            ('Мінуси: кожен зайвий плагін уповільнює сайт, тому потрібна дисципліна.', 'Minusy: każda zbędna wtyczka spowalnia stronę, więc potrzebna jest dyscyplina.')]),
                          ('p',
                           'Приклад — квітковий магазин <a href="case-rozmarin">Rozmarin на WooCommerce</a>: каталог букетів, кошик і оформлення замовлення, якими можна керувати з адмінки без '
                           'розробника.',
                           'Przykład: <a href="case-rozmarin">kwiaciarnia Rozmarin na WooCommerce</a> — katalog bukietów, koszyk i zamówienia, którymi można zarządzać z panelu bez programisty.')]},
              {'h2_uk': 'Webflow: візуальний редактор і хостинг «під ключ»',
               'h2_pl': 'Webflow: wizualny edytor i hosting w pakiecie',
               'blocks': [('p',
                           'Webflow — платформа, де дизайн, CMS і хостинг живуть в одному місці. Сайт не потрібно оновлювати й захищати від вразливостей плагінів: це робить сама платформа. Редактор '
                           'зрозумілий навіть людині без технічного досвіду, тому маркетолог може сам додати статтю, кейс чи вакансію.',
                           'Webflow łączy w jednym miejscu projekt, CMS i hosting. Nie trzeba samodzielnie aktualizować strony ani łatać dziur we wtyczkach — tym zajmuje się platforma. Edytor jest '
                           'zrozumiały nawet dla osoby bez technicznego zaplecza, więc marketingowiec sam doda wpis, case study czy ofertę pracy.'),
                          ('ul',
                           [('Плюси: стабільність, швидкий хостинг, анімації без «милиць», зручна CMS для блогу й кейсів.',
                             'Plusy: stabilność, szybki hosting, animacje bez kombinowania, wygodny CMS do bloga i realizacji.'),
                            ('Мінуси: платний хостинг-план Webflow — щомісячна чи щорічна підписка, яку треба закласти в бюджет.',
                             'Minusy: płatny plan hostingowy Webflow — subskrypcja miesięczna lub roczna, którą trzeba wliczyć w budżet.'),
                            ("Мінуси: у CMS є ліміти на кількість записів і складність зв'язків, а e-commerce скромніший за WooCommerce.",
                             'Minusy: CMS ma limity liczby rekordów i złożoności powiązań, a e-commerce jest skromniejszy niż WooCommerce.'),
                            ('Мінуси: сайт не можна просто «забрати» на свій сервер у повному вигляді — експорт обмежений.',
                             'Minusy: strony nie przeniesiesz w pełni na własny serwer — eksport jest ograniczony.')]),
                          ('p',
                           'Так ми зробили <a href="case-core-accounting">сайт бухгалтерської компанії Core Accounting на Webflow CMS</a>: послуги й публікації оновлюються через CMS без розробника, '
                           'а дизайн при цьому не «розвалюється».',
                           'Tak powstała <a href="case-core-accounting">strona biura rachunkowego Core Accounting na Webflow CMS</a>: usługi i publikacje aktualizuje się przez CMS bez programisty, a '
                           'układ strony się nie rozjeżdża.')]},
              {'h2_uk': 'Код на React або Next.js: швидкість і свобода',
               'h2_pl': 'Kod w React lub Next.js: szybkość i pełna swoboda',
               'blocks': [('p',
                           'Сайт, написаний з нуля, не обмежений можливостями конструктора чи плагінів. Немає зайвого коду, тож сторінки відкриваються дуже швидко, а будь-яку логіку — калькулятор, '
                           'особистий кабінет, інтеграцію з CRM — можна зробити саме так, як потрібно бізнесу.',
                           'Strona pisana od zera nie jest ograniczona możliwościami kreatora ani wtyczek. Nie ma w niej zbędnego kodu, więc ładuje się bardzo szybko, a dowolną logikę — kalkulator, '
                           'panel klienta, integrację z CRM — da się zrobić dokładnie tak, jak potrzebuje firma.'),
                          ('p',
                           'Зворотний бік — правки. Якщо не підключати окрему CMS, навіть заміну тексту в блоці робить розробник. Для лендінгу, який змінюється раз на пів року, це нормально; для '
                           'сайту з блогом, що оновлюється щотижня, — ні.',
                           'Druga strona medalu to zmiany. Bez podpiętego CMS-a nawet podmianę tekstu robi programista. Przy landingu aktualizowanym raz na pół roku to nie problem, przy blogu z '
                           'nowym wpisem co tydzień — już tak.'),
                          ('p',
                           'Приклад — <a href="case-tarik-invest">лендінг для електромонтажної компанії Tarik Invest на Next.js</a>: одна сторінка, максимальна швидкість і нічого, що треба '
                           'оновлювати щомісяця.',
                           'Przykład: <a href="case-tarik-invest">landing firmy elektroinstalacyjnej Tarik Invest w Next.js</a> — jedna strona, maksymalna szybkość i nic, co wymagałoby '
                           'comiesięcznych aktualizacji.')]},
              {'h2_uk': 'А як щодо Tilda і Wix?',
               'h2_pl': 'A co z Wix i innymi kreatorami?',
               'blocks': [('p',
                           'Tilda і Wix — нормальний вибір, коли потрібно швидко й самостійно зібрати просту сторінку з готових блоків. Для тесту ідеї чи сторінки події цього вистачає, і ми не '
                           'вважаємо конструктори «поганими».',
                           'Wix, Tilda czy podobne kreatory to rozsądny wybór, gdy trzeba szybko i samodzielnie złożyć prostą stronę z gotowych bloków. Do sprawdzenia pomysłu albo strony wydarzenia '
                           'w zupełności wystarczą i nie uważamy ich za „złe”.'),
                          ('p',
                           'Ми зазвичай на них не працюємо, бо впираємося в стелю: обмежений контроль над кодом і технічним SEO, складніша багатомовність, залежність від тарифу платформи й фактична '
                           'неможливість перенести сайт деінде. Коли бізнес росте, такий сайт найчастіше переробляють повністю.',
                           'My zwykle z nich nie korzystamy, bo szybko napotykamy ich ograniczenia: ograniczona kontrola nad kodem i technicznym SEO, trudniejsza wielojęzyczność, zależność od abonamentu i '
                           'praktycznie brak możliwości przeniesienia strony gdzie indziej. Gdy firma rośnie, taką stronę zwykle stawia się od nowa.')]},
              {'h2_uk': 'Порівняння: WordPress, Webflow і код',
               'h2_pl': 'Porównanie: WordPress, Webflow i kod',
               'blocks': [('table',
                           [('Критерій', 'Kryterium'), ('WordPress', 'WordPress'), ('Webflow', 'Webflow'), ('Код (Next.js)', 'Kod (Next.js)')],
                           [[('Хто редагує', 'Kto edytuje'), ('Клієнт в адмінці', 'Klient w panelu'), ('Клієнт у редакторі', 'Klient w edytorze'), ('Розробник або CMS', 'Programista lub CMS')],
                            [('Щомісячні витрати', 'Koszty co miesiąc'), ('Недорогий хостинг', 'Tani hosting'), ('Платний план Webflow', 'Płatny plan Webflow'), ('Від нуля до VPS', 'Od 0 € do kosztu VPS')],
                            [('Оновлення й безпека', 'Aktualizacje i bezpieczeństwo'),
                             ('Регулярно, на вас', 'Regularnie, po Twojej stronie'),
                             ('Робить платформа', 'Po stronie platformy'),
                             ('Мінімальні', 'Minimalne')],
                            [('Магазин', 'Sklep'), ('WooCommerce — сильний', 'WooCommerce — mocny'), ('Базовий', 'Podstawowy'), ('Під задачу', 'Na miarę')],
                            [('Швидкість', 'Szybkość'), ('Добра при дисципліні', 'Dobra przy dyscyplinie'), ('Добра', 'Dobra'), ('Найвища', 'Najwyższa')],
                            [('Перенесення', 'Przeniesienie'), ('Будь-куди', 'Gdziekolwiek'), ('Обмежене', 'Ograniczone'), ('Будь-куди', 'Gdziekolwiek')]]),
                          ('card',
                           'Правило, яке рідко підводить: якщо контент змінюється щотижня — CMS (WordPress або Webflow); якщо потрібен магазин — WooCommerce; якщо сторінка статична, а важлива кожна '
                           'мілісекунда — код.',
                           'Zasada, która rzadko zawodzi: jeśli treść zmienia się co tydzień — CMS (WordPress lub Webflow); jeśli potrzebny jest sklep — WooCommerce; jeśli strona jest statyczna, a '
                           'liczy się każda milisekunda — kod.')]},
              {'h2_uk': 'Хто чим володіє і скільки коштує утримання',
               'h2_pl': 'Kto jest właścicielem i ile kosztuje utrzymanie',
               'blocks': [('p',
                           'На WordPress і коді ви володієте файлами повністю: сайт можна перенести на інший хостинг — Hostinger, VPS чи Cloudflare — будь-коли. У Webflow ви володієте контентом і '
                           'акаунтом, але сайт живе в екосистемі платформи. Це не мінус сам по собі, просто про нього варто знати заздалегідь.',
                           'Na WordPressie i w kodzie pliki w całości należą do Ciebie: stronę przeniesiesz na inny hosting — Hostinger, VPS czy Cloudflare — w dowolnej chwili. W Webflow jesteś '
                           'właścicielem treści i konta, ale strona działa w ekosystemie platformy. To nie wada sama w sobie, po prostu warto wiedzieć o tym wcześniej.'),
                          ('p',
                           'Незалежно від платформи, після здачі ви отримуєте всі доступи: домен, хостинг, CMS, аналітику. Домен і хостинг ми радимо оформлювати на вас, а не на підрядника. Щомісячно '
                           'платите за хостинг або план Webflow, домен раз на рік, а за бажанням — за технічну підтримку, яка в нас коштує від €20/міс.',
                           'Niezależnie od technologii po oddaniu projektu dostajesz wszystkie dostępy: domenę, hosting, CMS, analitykę. Domenę i hosting radzimy rejestrować na siebie (lub swoją '
                           'JDG), a nie na wykonawcę. Co miesiąc płacisz za hosting lub plan Webflow, za domenę raz w roku, a opcjonalnie za opiekę techniczną — u nas od 20 € miesięcznie.')]},
              {'h2_uk': 'Як ми обираємо платформу під проєкт',
               'h2_pl': 'Jak dobieramy platformę do projektu',
               'blocks': [('p',
                           'На першій розмові ми питаємо не «яку платформу хочете», а що буде із сайтом через рік. Відповіді на кілька запитань зазвичай одразу звужують вибір до одного варіанта.',
                           'Na pierwszej rozmowie nie pytamy „na jakiej platformie chcesz stronę”, tylko co będzie się działo ze stroną za rok. Odpowiedzi na kilka pytań zwykle od razu zawężają '
                           'wybór do jednej opcji.'),
                          ('ul',
                           [('Хто і як часто змінюватиме тексти, ціни, товари?', 'Kto i jak często będzie zmieniał teksty, ceny, produkty?'),
                            ('Чи потрібен кошик і онлайн-оплата — зараз або в найближчих планах?', 'Czy potrzebujesz koszyka i płatności online — teraz lub w najbliższych planach?'),
                            ('Чи є нестандартна логіка: калькулятор, кабінет, інтеграції?', 'Czy potrzebna jest nietypowa logika: kalkulator, panel klienta, integracje?'),
                            ('Скільки мов і чи важливе SEO під кілька ринків?', 'Ile wersji językowych i czy liczy się SEO na kilku rynkach?'),
                            ('Який бюджет на старт і які щомісячні витрати комфортні?', 'Jaki budżet na start i jakie koszty miesięczne są akceptowalne?')]),
                          ('p',
                           'Для <a href="svc-korporatyvnyi-sait">корпоративного сайту</a> з блогом і кейсами найчастіше радимо Webflow або WordPress, для <a '
                           'href="svc-internet-magazyn">інтернет-магазину</a> — WooCommerce, для лендінгу з високими вимогами до швидкості — Next.js.',
                           'Przy <a href="svc-korporatyvnyi-sait">stronie firmowej</a> z blogiem i realizacjami najczęściej polecamy Webflow albo WordPressa, przy <a '
                           'href="svc-internet-magazyn">sklepie internetowym</a> — WooCommerce, a przy landingu, w którym liczy się szybkość — Next.js.'),
                          ('h3', 'Типові помилки при виборі платформи', 'Najczęstsze błędy przy wyborze platformy'),
                          ('ul',
                           [('Обирати за ціною старту й не рахувати щомісячні витрати та вартість правок за рік-два.',
                             'Patrzeć tylko na cenę wykonania, a nie liczyć kosztów utrzymania i zmian w perspektywie roku czy dwóch.'),
                            ('Брати WordPress «на виріст» для односторінкового лендінгу, який ніхто не оновлюватиме.',
                             'Brać WordPressa „na zapas” pod jednostronicowy landing, którego nikt nie będzie aktualizował.'),
                            ('Будувати магазин на сотні товарів у Webflow чи конструкторі замість WooCommerce.', 'Stawiać sklep na setki produktów w Webflow albo kreatorze zamiast na WooCommerce.'),
                            ('Реєструвати домен і хостинг на підрядника, а потім місяцями повертати доступи.', 'Rejestrować domenę i hosting na wykonawcę, a potem miesiącami odzyskiwać dostępy.')]),
                          ('p',
                           'Якщо сумніваєтеся, почніть із простого: чесно опишіть, хто працюватиме із сайтом і що ви плануєте додати. Ми запропонуємо платформу, пояснимо, чому саме її, і назвемо '
                           'щомісячні витрати ще до старту. Орієнтири по бюджету є на сторінці <a href="prices">цін</a>.',
                           'Jeśli masz wątpliwości, zacznij od prostego opisu: kto będzie pracował ze stroną i co planujesz dodać. Zaproponujemy platformę, wyjaśnimy, dlaczego właśnie ta, i podamy '
                           'koszty utrzymania jeszcze przed startem. Orientacyjne kwoty znajdziesz w <a href="prices">cenniku</a>.'),
                          ('card',
                           'Найдорожча помилка — обрати платформу «бо так зробив знайомий». Переробка сайту через рік коштує більше, ніж пів години розмови на старті.',
                           'Najdroższy błąd to wybór platformy „bo znajomy tak zrobił”. Przebudowa strony po roku kosztuje więcej niż pół godziny rozmowy na starcie.')]}],
 'faq': [['WordPress чи Webflow — що краще для бізнесу?',
          'Webflow czy WordPress — co lepsze dla firmy?',
          'Залежить від задачі. WordPress кращий для магазинів на WooCommerce, складних сайтів із великою кількістю плагінів і коли хочеться дешевий хостинг. Webflow кращий для маркетингових і '
          'корпоративних сайтів, які команда оновлює сама й не хоче думати про оновлення та безпеку. Для обох ми передаємо клієнту всі доступи.',
          'To zależy od zadania. WordPress lepiej sprawdza się przy sklepach na WooCommerce, rozbudowanych stronach z wieloma wtyczkami i gdy zależy Ci na tanim hostingu. Webflow wygrywa przy '
          'stronach firmowych i marketingowych, które zespół edytuje sam i nie chce zajmować się aktualizacjami ani bezpieczeństwem. W obu przypadkach przekazujemy komplet dostępów.'],
         ['Сайт на коді чи на CMS — що обрати?',
          'Strona pisana od zera czy CMS — co wybrać?',
          'Якщо контент змінюється часто, обирайте CMS: WordPress або Webflow. Код на React чи Next.js виправданий, коли потрібна максимальна швидкість, нестандартна логіка або сторінка майже не '
          'змінюється. До коду можна підключити CMS, але це додає роботи на старті, тому ми радимо такий варіант лише там, де він справді потрібен.',
          'Jeśli treść zmienia się często, wybierz CMS: WordPressa lub Webflow. Kod w React czy Next.js ma sens, gdy potrzebujesz maksymalnej szybkości, nietypowej logiki albo strona prawie się nie '
          'zmienia. Do kodu można podpiąć CMS, ale to więcej pracy na starcie, więc polecamy takie rozwiązanie tylko tam, gdzie naprawdę jest potrzebne.'],
         ['Tilda чи WordPress — що краще?',
          'Wix czy WordPress — co lepsze?',
          'Для простої сторінки, яку ви збираєте самі за вечір, конструктор на кшталт Tilda цілком підійде. Для сайту, який росте, потребує магазину, кількох мов і серйозного SEO, кращий WordPress: '
          'більше контролю над кодом, будь-який хостинг і можливість перенести сайт. Тому ми зазвичай працюємо на WordPress, а не на конструкторах.',
          'Na prostą stronę składaną samodzielnie w jeden wieczór kreator typu Wix w zupełności wystarczy. Przy stronie, która ma rosnąć, potrzebuje sklepu, kilku języków i poważnego SEO, lepszy '
          'jest WordPress: więcej kontroli nad kodem, dowolny hosting i możliwość przeniesienia strony. Dlatego zwykle pracujemy na WordPressie, a nie na kreatorach.'],
         ['Скільки коштує утримання сайту щомісяця?',
          'Ile kosztuje utrzymanie strony miesięcznie?',
          'Залежить від платформи. На WordPress і коді основна стаття — хостинг, він зазвичай недорогий; у Webflow — платний хостинг-план платформи. Плюс домен раз на рік. Технічна підтримка в нас — '
          "від €20/міс, вона необов'язкова, але для WordPress ми її радимо через регулярні оновлення.",
          'To zależy od platformy. Przy WordPressie i kodzie głównym kosztem jest hosting, zwykle niedrogi; w Webflow — płatny plan hostingowy platformy. Do tego domena raz w roku. Opieka techniczna '
          'u nas kosztuje od 20 € miesięcznie; nie jest obowiązkowa, ale przy WordPressie ją polecamy ze względu na regularne aktualizacje.'],
         ['Чи зможу я сам редагувати сайт?',
          'Czy sam będę mógł edytować stronę?',
          'Так, якщо сайт на WordPress або Webflow: тексти, фото, товари й статті змінюєте в адмінці без розробника. Для деяких проєктів ми записуємо відеоінструкцію. На сайті, написаному з нуля без '
          'CMS, правки робить розробник, тому такий варіант радимо для сторінок, які змінюються рідко.',
          'Tak, jeśli strona powstała na WordPressie lub Webflow: teksty, zdjęcia, produkty i wpisy zmieniasz w panelu bez programisty. Przy części projektów nagrywamy instrukcję wideo. Na stronie '
          'pisanej od zera bez CMS-a zmiany wprowadza programista, dlatego polecamy takie rozwiązanie przy stronach, które zmieniają się rzadko.']],
 'service': 'korporatyvnyi-sait',
 'cta_uk': 'Не впевнені, яка платформа підійде саме вам? Опишіть задачу — порадимо варіант і дамо оцінку за 24 години, або перегляньте, як ми робимо корпоративні сайти.',
 'cta_pl': 'Nie wiesz, która platforma pasuje do Twojej firmy? Opisz projekt — doradzimy technologię i przygotujemy wycenę w ciągu 24 godzin. Zobacz też, jak tworzymy strony firmowe.',
 'date': '2026-09-24'}
