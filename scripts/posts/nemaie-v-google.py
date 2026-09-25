# Стаття блогу. Автор: Andrii Shestakov. Поля й формат — див. scripts/build_blog.py.

POST = {'key': 'nemaie-v-google',
 'path_uk': '/blog/chomu-saitu-nemaie-v-google/',
 'path_pl': '/pl/blog/dlaczego-strony-nie-ma-w-google/',
 'img': 'assets/why-5.webp',
 'title_uk': 'Чому сайту немає в Google: чекліст 2026 | SHSTKV Digital',
 'title_pl': 'Dlaczego strony nie ma w Google? Checklista 2026 | SHSTKV Digital',
 'desc_uk': 'Сайт не індексується? Перевіряємо site:, Search Console, noindex, robots.txt, canonical і sitemap. Покроковий чекліст від веб-студії з 12+ роками досвіду.',
 'desc_pl': 'Strona nie jest indeksowana? Sprawdź site:, Google Search Console, noindex, robots.txt, canonical i mapę witryny. Praktyczna checklista od studia z Wrocławia.',
 'h1_uk': 'Чому сайту немає в Google і що з цим робити',
 'h1_pl': 'Dlaczego mojej strony nie ma w Google i jak to naprawić',
 'sub_uk': 'Покроковий чекліст: від перевірки site: до Search Console та технічних помилок.',
 'sub_pl': 'Krok po kroku: od komendy site: po Search Console i błędy techniczne.',
 'topic_uk': 'SEO',
 'topic_pl': 'SEO',
 'minutes': 8,
 'answer_uk': 'Найчастіше сайту немає в Google через технічну заборону (noindex, закритий robots.txt, галочка в CMS), відсутність у Search Console і sitemap, помилки canonical або просто молодий '
              'домен. Почніть із запиту site:вашдомен, додайте сайт у Google Search Console як ресурс «Домен», надішліть sitemap і перевірте звіт «Індексування сторінок» — він покаже точну причину.',
 'answer_pl': 'Najczęściej strony nie ma w Google przez blokadę techniczną (noindex, zablokowany robots.txt, opcja w CMS), brak Search Console i mapy witryny, błędny canonical albo po prostu młodą '
              'domenę. Zacznij od wyszukania site:twojadomena, dodaj stronę do Google Search Console jako usługę typu „Domena”, prześlij sitemap i sprawdź raport indeksowania stron — wskaże '
              'konkretną przyczynę.',
 'sections': [{'h2_uk': 'Крок 1. Перевірте, чи сайту справді немає в індексі',
               'h2_pl': 'Krok 1. Sprawdź, czy strony naprawdę nie ma w indeksie',
               'blocks': [('p',
                           'Власники часто кажуть «нас немає в Google», коли насправді сайт є, просто не на першій сторінці за потрібним запитом. Тому спершу введіть у пошук '
                           '<strong>site:вашдомен.com</strong> — без пробілу після двокрапки. Якщо видача порожня, Google сторінок не знає або свідомо їх не показує.',
                           'Właściciele firm często mówią „nie ma nas w Google”, a w praktyce strona jest w indeksie, tylko nie na pierwszej stronie wyników dla ważnej frazy. Dlatego zacznij od wpisania w wyszukiwarkę '
                           '<strong>site:twojadomena.pl</strong> — bez spacji po dwukropku. Pusty wynik oznacza, że Google nie zna Twoich podstron albo świadomie ich nie pokazuje.'),
                          ('p',
                           'Оператор site: дає лише приблизну картину: кількість результатів неточна, а окремі сторінки можуть не відображатися. Надійне джерело — Google Search Console, до якої '
                           'переходимо далі.',
                           'Pamiętaj, że site: daje tylko przybliżony obraz — liczba wyników jest szacunkowa, a niektóre adresy mogą się w ogóle nie wyświetlać. Wiarygodne dane ma dopiero Google '
                           'Search Console, więc to kolejny krok.'),
                          ('table',
                           [('Що бачите', 'Co widzisz'), ('Що це означає', 'Co to znaczy'), ('Що робити', 'Co zrobić')],
                           [[('site: порожній', 'site: nic nie zwraca'),
                             ('Сайт не в індексі', 'Strony nie ma w indeksie'),
                             ('Шукати технічну причину (кроки 2–4)', 'Szukać przyczyny technicznej (kroki 2–4)')],
                            [('Є лише головна', 'Jest tylko strona główna'),
                             ('Решту сторінок Google не знайшов або відкинув', 'Reszty Google nie znalazł lub odrzucił'),
                             ('Sitemap, внутрішні посилання, звіт індексування', 'Sitemap, linkowanie wewnętrzne, raport indeksowania')],
                            [('Сторінки є, але за запитом вас не видно', 'Podstrony są w indeksie, ale nie widać Cię na ważne frazy'),
                             ('Проблема позицій, а не індексації', 'Problem pozycji, nie indeksacji'),
                             ('Контент, структура, SEO-оптимізація', 'Treści, struktura, optymalizacja SEO')]])]},
              {'h2_uk': 'Крок 2. Додайте сайт у Google Search Console',
               'h2_pl': 'Krok 2. Dodaj stronę do Google Search Console',
               'blocks': [('p',
                           'Search Console — безкоштовний інструмент Google, і без нього діагностика йде наосліп. Додавайте ресурс типу <strong>«Домен»</strong>: він охоплює http і https, www і без '
                           'www та всі піддомени. Підтвердження — через TXT-запис у DNS у панелі реєстратора або Cloudflare.',
                           'Search Console to darmowe narzędzie Google i bez niego diagnoza to zgadywanie. Wybierz usługę typu <strong>„Domena”</strong> — obejmuje http i https, wersję z www i bez '
                           'oraz wszystkie subdomeny. Weryfikacja odbywa się przez rekord TXT w DNS, u rejestratora domeny albo w Cloudflare.'),
                          ('ul',
                           [('Надішліть карту сайту (sitemap.xml) у розділі «Файли Sitemap».', 'Prześlij mapę witryny (sitemap.xml) w sekcji „Mapy witryn”.'),
                            ('Через «Перевірку URL» перевірте головну й кілька ключових сторінок.', 'Sprawdź stronę główną i kluczowe podstrony narzędziem „Sprawdzanie adresu URL”.'),
                            ('Якщо сторінку можна індексувати, натисніть «Надіслати запит на індексування».', 'Jeśli adres można zindeksować, kliknij „Poproś o zindeksowanie”.'),
                            ('Відкрийте звіт «Індексування сторінок» — там причини, чому URL не в індексі.',
                             'Otwórz raport „Indeksowanie stron” — znajdziesz tam powody, dla których adresy są poza indeksem.')]),
                          ('p',
                           'Запит на індексування не пришвидшує все миттєво і не гарантує потрапляння в індекс. Він лише ставить сторінку в чергу на сканування, тому натискати його щодня немає '
                           'сенсу.',
                           'Prośba o zindeksowanie nie działa natychmiast i niczego nie gwarantuje. Po prostu dodaje adres do kolejki skanowania, więc ponawianie jej codziennie nic nie da.')]},
              {'h2_uk': 'Крок 3. Шукайте технічну заборону',
               'h2_pl': 'Krok 3. Poszukaj blokady technicznej',
               'blocks': [('p',
                           'У наших аудитах це найчастіша причина — і найприкріша, бо виправляється за хвилини. Сайт розробляли на тестовому домені, закрили від пошуку, а після запуску забули '
                           'відкрити.',
                           'W naszych audytach to najczęstsza przyczyna, a zarazem najbardziej irytująca, bo naprawa zajmuje kilka minut. Strona powstawała na domenie testowej, zablokowano ją przed '
                           'wyszukiwarkami, a po starcie nikt tej blokady nie zdjął.'),
                          ('ul',
                           [('Тег <strong>noindex</strong> у коді сторінки або в HTTP-заголовку X-Robots-Tag.', 'Tag <strong>noindex</strong> w kodzie strony lub w nagłówku HTTP X-Robots-Tag.'),
                            ('У WordPress увімкнена опція «Попросити пошукові системи не індексувати сайт» (Налаштування → Читання).',
                             'W WordPressie zaznaczona opcja „Proś wyszukiwarki o nieindeksowanie tej witryny” (Ustawienia → Czytanie).'),
                            ('У robots.txt лишився рядок Disallow: / з етапу розробки.', 'W pliku robots.txt został wpis Disallow: / z czasu budowy strony.'),
                            ('У Webflow вимкнено індексацію в налаштуваннях SEO або сайт живе лише на піддомені webflow.io.',
                             'W Webflow wyłączona indeksacja w ustawieniach SEO albo strona działa tylko na subdomenie webflow.io.'),
                            ('Сторінки віддають помилку 4xx/5xx або редирект по колу.', 'Podstrony zwracają błąd 4xx/5xx albo zapętlone przekierowanie.')]),
                          ('card',
                           'Важливий нюанс: robots.txt забороняє сканування, а не індексацію. Якщо сторінку закрито в robots.txt, Google не побачить на ній noindex. Щоб прибрати сторінку з пошуку, '
                           'потрібен noindex при відкритому скануванні, а не Disallow.',
                           'Ważny niuans: robots.txt blokuje skanowanie, a nie indeksowanie. Jeśli podstrona jest zablokowana w robots.txt, Google nie zobaczy na niej tagu noindex. Żeby usunąć adres '
                           'z wyników, potrzebujesz noindex przy otwartym skanowaniu, a nie Disallow.')]},
              {'h2_uk': 'Крок 4. Розберіться зі статусами «виявлено» і «проскановано»',
               'h2_pl': 'Krok 4. Zrozum statusy „wykryta” i „zeskanowana”',
               'blocks': [('p',
                           'Якщо блокувань немає, дивіться у звіті індексування на два статуси. Назви в інтерфейсі залежать від мови, тож орієнтуйтеся також на англійські: <strong>Discovered – '
                           'currently not indexed</strong> і <strong>Crawled – currently not indexed</strong>.',
                           'Jeśli blokad nie ma, szukaj w raporcie indeksowania dwóch statusów. Polskie nazwy w interfejsie bywają różne, więc warto znać angielskie odpowiedniki: <strong>Discovered '
                           '– currently not indexed</strong> i <strong>Crawled – currently not indexed</strong>.'),
                          ('h3', '«Виявлено, але не проіндексовано»', '„Strona wykryta – obecnie nie zindeksowana”'),
                          ('p',
                           'Google знає адресу, але ще не сканував її. Для нового сайту це нормально. Якщо стан триває тижнями, зазвичай бракує внутрішніх посилань на сторінку, сервер відповідає '
                           'повільно або сайт генерує тисячі схожих URL (фільтри, параметри), і Google не бачить сенсу їх обходити.',
                           'Google zna adres, ale jeszcze go nie odwiedził. Przy nowej stronie to normalne. Jeśli ten status utrzymuje się tygodniami, zwykle brakuje linków wewnętrznych do podstrony, serwer '
                           'odpowiada wolno albo witryna generuje tysiące podobnych adresów (filtry, parametry) i Google nie widzi sensu ich przeglądać.'),
                          ('h3', '«Проскановано, але не проіндексовано»', '„Strona zeskanowana, ale jeszcze nie zindeksowana”'),
                          ('p',
                           'Google сторінку бачив і вирішив не додавати. Найчастіше це тонкий або дубльований контент: три речення тексту, скопійовані описи товарів від постачальника, однакові '
                           'сторінки послуг для різних міст із заміною лише назви.',
                           'Google widział podstronę i uznał, że nie warto jej dodawać. Zwykle chodzi o treść cienką lub zduplikowaną: trzy zdania tekstu, opisy produktów skopiowane od hurtowni albo '
                           'identyczne strony usług dla różnych miast, różniące się tylko nazwą miejscowości.')]},
              {'h2_uk': 'Інші типові причини: canonical, JavaScript, hreflang, швидкість',
               'h2_pl': 'Inne typowe przyczyny: canonical, JavaScript, hreflang, szybkość',
               'blocks': [('ul',
                           [('<strong>Помилковий canonical.</strong> Усі сторінки вказують canonical на головну — і Google індексує лише її. Статус «Дублікат: Google вибрав іншу канонічну сторінку» '
                             'теж варто перевірити.',
                             '<strong>Błędny canonical.</strong> Wszystkie podstrony wskazują canonical na stronę główną, więc Google indeksuje tylko ją. Warto też przejrzeć status „Duplikat, '
                             'wybrana przez Google strona kanoniczna jest inna niż wskazana przez użytkownika”.'),
                            ("<strong>Контент лише в JavaScript.</strong> Google рендерить JS, але із затримкою. Якщо текст і посилання з'являються тільки після кліку чи прокрутки, вони можуть не "
                             'потрапити в індекс. Для React-сайтів ми використовуємо Next.js із серверним рендерингом.',
                             '<strong>Treść tylko w JavaScripcie.</strong> Google renderuje JS, ale z opóźnieniem. Tekst i linki pojawiające się dopiero po kliknięciu lub przewinięciu mogą nie '
                             'trafić do indeksu. Przy projektach w React stawiamy na Next.js z renderowaniem po stronie serwera.'),
                            ('<strong>Сторінки-сироти.</strong> Сторінка є в sitemap, але на неї не веде жодне посилання з меню чи тексту. Для Google це сигнал, що вона неважлива.',
                             '<strong>Osierocone podstrony.</strong> Adres jest w sitemapie, ale nie prowadzi do niego żaden link z menu ani treści. Dla Google to sygnał, że podstrona jest mało '
                             'istotna.'),
                            ('<strong>Багатомовність без hreflang.</strong> Українська й польська версії без взаємних hreflang можуть конкурувати між собою або вважатися дублями, якщо тексти майже '
                             'однакові.',
                             '<strong>Wielojęzyczność bez hreflang.</strong> Wersje polska i ukraińska bez wzajemnych tagów hreflang mogą ze sobą konkurować, a przy bardzo podobnych treściach — być '
                             'traktowane jak duplikaty.'),
                            ('<strong>Повільний сервер.</strong> Швидкість сама не блокує індексацію, але якщо хостинг відповідає повільно або з помилками, Google сканує менше сторінок.',
                             '<strong>Wolny serwer.</strong> Szybkość sama w sobie nie blokuje indeksacji, ale gdy hosting odpowiada wolno lub z błędami, Google skanuje mniej podstron.')])]},
              {'h2_uk': 'Новий домен: скільки чекати',
               'h2_pl': 'Nowa domena: ile czekać',
               'blocks': [('p',
                           "Точного терміну Google не називає. На практиці головна нового сайту з Search Console і sitemap часто з'являється в індексі за кілька днів, а решта сторінок — протягом "
                           'кількох тижнів. Без Search Console і посилань ззовні це може тягнутися довше.',
                           'Google nie podaje konkretnego terminu. W praktyce, jeśli nowa witryna jest dodana do Search Console i ma sitemap, jej strona główna często trafia do indeksu w ciągu kilku dni, a pozostałe '
                           'podstrony — w ciągu kilku tygodni. Bez Search Console i linków z zewnątrz może to trwać dłużej.'),
                          ('p',
                           'Прискорити процес допомагають прості речі: профіль у Google Business Profile з посиланням на сайт, згадки в каталогах і соцмережах, логічна структура з меню, яке веде на '
                           'всі ключові сторінки. Саме тому структуру <a href="svc-korporatyvnyi-sait">багатосторінкового сайту</a> ми погоджуємо ще до дизайну.',
                           'Przyspieszyć proces pomagają proste rzeczy: Profil Firmy w Google z linkiem do strony, wpisy w katalogach branżowych i mediach społecznościowych, logiczna struktura z '
                           'menu prowadzącym do wszystkich ważnych podstron. Dlatego strukturę <a href="svc-korporatyvnyi-sait">strony firmowej</a> ustalamy z klientem jeszcze przed projektem '
                           'graficznym.')]},
              {'h2_uk': '«Не в індексі» і «низькі позиції» — різні проблеми',
               'h2_pl': '„Brak w indeksie” a „niskie pozycje” to dwa różne problemy',
               'blocks': [('p',
                           'Якщо site: показує ваші сторінки, а Search Console — що вони проіндексовані, технічно все гаразд. Тоді питання вже в тому, чи відповідає сторінка на запит краще за '
                           'конкурентів: чи є на ній потрібні слова, чи вистачає тексту, чи зрозуміло, де ви працюєте і скільки це коштує.',
                           'Jeśli site: pokazuje Twoje podstrony, a Search Console potwierdza indeksację, technicznie wszystko jest w porządku. Wtedy pytanie brzmi, czy strona odpowiada na zapytanie '
                           'lepiej niż konkurencja: czy zawiera właściwe frazy, czy ma wystarczająco treści, czy jasno mówi, gdzie działasz i ile to kosztuje.'),
                          ('card',
                           'Індексація — це вхідний квиток, а не місце в топі. Жодна студія чесно не гарантує конкретних позицій: вони залежать від конкуренції в ніші, якості контенту й часу. Ми '
                           'відповідаємо за інше — щоб технічно сайт не заважав Google його знайти.',
                           'Indeksacja to bilet wstępu, a nie miejsce na szczycie wyników. Żadne uczciwe studio nie gwarantuje konkretnych pozycji — zależą od konkurencji w branży, jakości treści i czasu. My '
                           'odpowiadamy za coś innego: żeby od strony technicznej nic nie przeszkadzało Google w znalezieniu witryny.'),
                          ('p',
                           'Для локального бізнесу варто одразу подбати і про картки в Google Maps, бо частина клієнтів бачить вас саме там, ще до органічної видачі.',
                           'Jeśli działasz lokalnie, warto od razu zadbać też o wizytówkę w Mapach Google — część klientów trafia na Ciebie właśnie tam, zanim zobaczy wyniki organiczne.')]},
              {'h2_uk': 'Що робимо ми: технічний аудит індексації',
               'h2_pl': 'Co robimy my: audyt techniczny indeksacji',
               'blocks': [('p',
                           'Коли клієнт приходить із питанням «чому нас немає в Google», ми не починаємо з ключових слів. Спершу — доступи до Search Console, хостингу й CMS, а далі перевірка по '
                           'чеклісту:',
                           'Gdy klient przychodzi z pytaniem „dlaczego nie ma nas w Google”, nie zaczynamy od fraz kluczowych. Najpierw prosimy o dostęp do Search Console, hostingu i CMS, a potem '
                           'przechodzimy przez checklistę:'),
                          ('ul',
                           [('robots.txt, мета-теги robots, X-Robots-Tag і налаштування CMS;', 'robots.txt, meta tagi robots, X-Robots-Tag i ustawienia CMS;'),
                            ('sitemap, canonical, редиректи й коди відповіді сервера;', 'sitemap, canonical, przekierowania i kody odpowiedzi serwera;'),
                            ('hreflang для багатомовних версій;', 'hreflang dla wersji językowych;'),
                            ('внутрішні посилання, дублі й тонкі сторінки;', 'linkowanie wewnętrzne, duplikaty i cienkie podstrony;'),
                            ('швидкість і рендеринг JavaScript.', 'szybkość i renderowanie JavaScriptu.')]),
                          ('p',
                           'Після аудиту ви отримуєте список проблем із пріоритетами: що виправляємо ми, а що можна зробити самостійно. Вартість <a href="svc-seo">SEO-оптимізації та аудиту</a> '
                           'рахуємо після брифу, оцінка — за 24 години. Базова SEO-оптимізація вже входить у наші тарифи на <a href="svc-lending">лендінг</a>, тож нові сайти запускаються відкритими '
                           'для індексації.',
                           'Po audycie dostajesz listę problemów z priorytetami: co poprawiamy my, a co możesz zrobić sam. Koszt <a href="svc-seo">audytu i optymalizacji SEO</a> ustalamy po '
                           'briefie, a wycenę dostajesz w ciągu 24 godzin. Podstawowa optymalizacja SEO wchodzi już w nasze pakiety <a href="svc-lending">landing page</a>, więc nowe strony startują od razu otwarte '
                           'na indeksację.')]}],
 'faq': [['Як додати сайт у Google?',
          'Jak dodać stronę do Google?',
          'Найнадійніше — через Google Search Console. Додайте ресурс типу «Домен», підтвердіть його TXT-записом у DNS, надішліть sitemap.xml і через «Перевірку URL» попросіть проіндексувати головну '
          'сторінку. Окремої платної «реєстрації в Google» не існує, а сервіси, які її продають, роблять те саме, що ви можете зробити самі безкоштовно.',
          'Najpewniej przez Google Search Console. Dodaj usługę typu „Domena”, zweryfikuj ją rekordem TXT w DNS, prześlij sitemap.xml i narzędziem „Sprawdzanie adresu URL” poproś o zindeksowanie '
          'strony głównej. Płatna „rejestracja w Google” nie istnieje, a firmy, które ją sprzedają, robią dokładnie to, co możesz zrobić sam i za darmo.'],
         ['Скільки часу Google індексує новий сайт?',
          'Ile trwa indeksowanie nowej strony w Google?',
          "Зазвичай від кількох днів до кількох тижнів, і Google не дає точних термінів. Головна сторінка часто з'являється швидше, внутрішні — поступово. Процес пришвидшують Search Console, "
          'sitemap, зрозуміле меню з посиланнями на всі сторінки та зовнішні згадки, наприклад Google Business Profile.',
          'Zwykle od kilku dni do kilku tygodni — Google nie podaje dokładnych terminów. Strona główna często pojawia się szybciej, podstrony stopniowo. Proces przyspieszają Search Console, mapa '
          'witryny, czytelne menu z linkami do wszystkich podstron i wzmianki z zewnątrz, na przykład Profil Firmy w Google.'],
         ['Чому Google пише «проскановано, але не проіндексовано»?',
          'Co znaczy status „Strona zeskanowana, ale jeszcze nie zindeksowana”?',
          'Це означає, що Google відвідав сторінку, але вирішив поки не додавати її в індекс. Найчастіше причина в тонкому або дубльованому контенті. Допомагає розширити текст унікальною корисною '
          'інформацією, прибрати дублі та додати на сторінку внутрішні посилання з важливих розділів сайту. Після змін попросіть повторне індексування через «Перевірку URL».',
          'Oznacza, że Google odwiedził podstronę, ale na razie nie dodał jej do indeksu. Najczęściej chodzi o cienką lub zduplikowaną treść. Warto rozbudować tekst o unikalne, przydatne '
          'informacje, usunąć duplikaty i dodać linki wewnętrzne z ważnych sekcji serwisu. Po zmianach poproś o ponowne zindeksowanie w narzędziu „Sprawdzanie adresu URL”.'],
         ['Сайт є в Google, але його не знаходять за запитами. Чому?',
          'Strona jest w Google, ale nikt jej nie znajduje. Dlaczego?',
          'Це вже проблема позицій, а не індексації. Сторінка в індексі, але Google вважає інші результати кориснішими для запиту. Потрібно перевірити, чи є на сторінці ключові фрази, чи достатньо в '
          "ній змісту, як вона пов'язана з рештою сайту і наскільки сильні конкуренти в ніші.",
          'To problem pozycji, a nie indeksacji. Podstrona jest w indeksie, ale Google uznaje inne wyniki za trafniejsze. Trzeba sprawdzić, czy strona zawiera właściwe frazy, czy ma wystarczająco '
          'treści, jak jest powiązana linkami z resztą serwisu i jak silna jest konkurencja w branży.'],
         ['Чи можна гарантувати потрапляння в топ Google?',
          'Czy da się zagwarantować TOP 10 w Google?',
          'Ні, чесно гарантувати конкретні позиції не може ніхто, бо алгоритм і конкуренти від підрядника не залежать. Можна гарантувати технічно правильний сайт: відкритий для індексації, з '
          'коректними sitemap, canonical і hreflang. Це базова умова, без якої позиції неможливі в принципі, а далі все вирішують контент і час.',
          'Nie — nikt uczciwie nie zagwarantuje konkretnych pozycji, bo algorytm i konkurencja są poza kontrolą wykonawcy. Można zagwarantować poprawną technicznie stronę: otwartą na indeksację, z '
          'prawidłową mapą witryny, canonical i hreflang. To warunek wstępny, bez którego pozycje w ogóle nie są możliwe. Dalej decydują treść i czas.']],
 'service': 'seo',
 'cta_uk': 'Не знаєте, яка з причин ваша? <a href="contacts">Напишіть нам</a> — подивимося на Search Console і скажемо, що заважає індексації та скільки коштуватиме виправлення.',
 'cta_pl': 'Nie wiesz, która przyczyna dotyczy Twojej strony? <a href="contacts">Napisz do nas</a> — zajrzymy do Search Console i powiemy, co blokuje indeksację i ile będzie kosztować naprawa.',
 'date': '2026-09-24'}
