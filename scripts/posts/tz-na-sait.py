# Стаття блогу. Автор: Andrii Shestakov. Поля й формат — див. scripts/build_blog.py.

POST = {'key': 'tz-na-sait',
 'path_uk': '/blog/tz-na-sait/',
 'path_pl': '/pl/blog/brief-strony-internetowej/',
 'img': 'assets/why-4.webp',
 'title_uk': 'ТЗ на сайт: шаблон і приклад технічного завдання | SHSTKV Digital',
 'title_pl': 'Brief strony internetowej — przykład i szablon | SHSTKV Digital',
 'desc_uk': 'Що писати в ТЗ на сайт і чим воно відрізняється від брифу. Готовий шаблон з 11 розділів, приклад заповненого брифу, типові помилки й наш процес роботи.',
 'desc_pl': 'Co wpisać w brief strony internetowej i czym różni się od specyfikacji. Gotowy szablon z 11 punktami, przykład wypełnionego briefu, typowe błędy i nasz proces.',
 'h1_uk': 'ТЗ на сайт: шаблон і приклад технічного завдання',
 'h1_pl': 'Brief strony internetowej — przykład i szablon',
 'sub_uk': 'Що написати студії, щоб отримати точну оцінку й сайт, який закриває вашу задачу.',
 'sub_pl': 'Co przekazać wykonawcy, żeby dostać trafną wycenę i stronę, która realizuje Twój cel.',
 'topic_uk': 'Підготовка',
 'topic_pl': 'Przygotowanie',
 'minutes': 9,
 'answer_uk': 'ТЗ на сайт (технічне завдання) — документ, який описує, навіщо потрібен сайт, для кого він, які сторінки й функції в ньому будуть, звідки береться контент і в які терміни та '
              'бюджет треба вкластися. Для невеликого сайту замість повного ТЗ достатньо брифу на 1–2 сторінки: 11 розділів із шаблону нижче, заповнені своїми словами.',
 'answer_pl': 'Brief strony internetowej to krótki dokument, w którym opisujesz, po co firmie strona, do kogo jest skierowana, jakie podstrony i funkcje ma mieć, kto przygotuje treści oraz jaki '
              'jest termin i budżet. Przy małej stronie w zupełności wystarczy brief na 1–2 strony A4: 11 punktów z szablonu poniżej, opisanych własnymi słowami.',
 'sections': [{'h2_uk': 'Що таке ТЗ на сайт і навіщо воно',
               'h2_pl': 'Co to jest brief strony internetowej i po co go pisać',
               'blocks': [('p',
                           'ТЗ на сайт — це домовленість між вами й виконавцем, записана до початку роботи. Воно фіксує мету сайту, аудиторію, перелік сторінок, функції, мови, інтеграції, терміни й '
                           'бюджет. Без нього кожна сторона уявляє свій сайт, і різниця стає помітною лише тоді, коли дизайн уже намальовано.',
                           'Brief to spisane przed startem ustalenia między Tobą a wykonawcą. Opisuje cel strony, odbiorców, listę podstron, funkcje, wersje językowe, integracje, termin i budżet. '
                           'Bez niego każda strona wyobraża sobie inny serwis, a różnica wychodzi na jaw dopiero wtedy, gdy projekt graficzny jest już gotowy.'),
                          ('p',
                           'Від ТЗ залежать три речі. Перша — точна ціна: студія рахує не «сайт», а конкретний обсяг. Друга — терміни: коли матеріали й рішення зібрані заздалегідь, проєкт не стоїть '
                           'у паузах. Третя — результат: сайт відповідає вашій задачі, а не смаку дизайнера.',
                           'Od briefu zależą trzy rzeczy. Po pierwsze wycena: wykonawca liczy nie „stronę”, tylko konkretny zakres prac. Po drugie termin: gdy materiały i decyzje są zebrane '
                           'wcześniej, projekt nie stoi w miejscu. Po trzecie efekt: strona odpowiada na Twój cel, a nie na gust grafika.'),
                          ('p',
                           'Писати ТЗ мовою програмістів не потрібно. Технічну частину — платформу, хостинг, структуру коду — ми беремо на себе. Від вас потрібне інше: знання свого бізнесу, клієнтів і '
                           'того, що має статися, коли людина відкриє сайт.',
                           'Nie musisz pisać briefu językiem programistów. Część techniczną — platformę, hosting, kod — bierzemy na siebie. Od Ciebie potrzebujemy czegoś innego: wiedzy o firmie, '
                           'klientach i o tym, co ma się wydarzyć, gdy ktoś wejdzie na stronę.')]},
              {'h2_uk': 'Чим бриф відрізняється від ТЗ',
               'h2_pl': 'Brief a specyfikacja techniczna — czym się różnią',
               'blocks': [('p',
                           'Бриф — це анкета від замовника: що за бізнес, яка мета, які побажання. ТЗ — детальний документ, який зазвичай готує виконавець на основі брифу: точна структура, функції, '
                           'поведінка форм, інтеграції. Для лендінгу чи візитки брифу досить, повне ТЗ потрібне складним сайтам і магазинам.',
                           'Brief to opis od klienta: czym zajmuje się firma, jaki jest cel, jakie są oczekiwania. Specyfikacja techniczna to szczegółowy dokument, który zwykle przygotowuje wykonawca '
                           'na podstawie briefu: dokładna struktura, funkcje, działanie formularzy, integracje. Przy landing page lub wizytówce brief wystarczy, specyfikacja przydaje się w dużych '
                           'serwisach i sklepach.'),
                          ('table',
                           [('Критерій', 'Kryterium'), ('Бриф', 'Brief'), ('ТЗ', 'Specyfikacja')],
                           [[('Хто пише', 'Kto pisze'), ('Замовник', 'Klient'), ('Виконавець разом із замовником', 'Wykonawca razem z klientem')],
                            [('Обсяг', 'Objętość'), ('1–2 сторінки', '1–2 strony A4'), ('Від кількох сторінок і більше', 'Od kilku stron wzwyż')],
                            [('Що описує', 'Co opisuje'), ('Бізнес, мету, аудиторію, побажання', 'Firmę, cel, odbiorców, oczekiwania'),
                             ('Сторінки, функції, логіку, інтеграції', 'Podstrony, funkcje, logikę, integracje')],
                            [('Коли досить', 'Kiedy wystarczy'), ('Лендінг, візитка, невеликий сайт', 'Landing, wizytówka, mała strona firmowa'),
                             ('Магазин, сервіс, складні інтеграції', 'Sklep, serwis, złożone integracje')],
                            [('Мета', 'Cel'), ('Оцінка й старт проєкту', 'Wycena i start projektu'), ('Фіксація обсягу робіт', 'Zamknięcie zakresu prac')]]),
                          ('p',
                           'На практиці межа розмита: добрий бриф із переліком сторінок і функцій уже наполовину ТЗ. Тому шаблон нижче ми зробили так, щоб він годився для обох випадків — для '
                           'невеликого сайту його достатньо, для складного він стає основою технічного завдання.',
                           'W praktyce granica jest płynna: dobry brief z listą podstron i funkcji to już połowa specyfikacji. Dlatego szablon poniżej działa w obu przypadkach — przy małej stronie '
                           'w zupełności wystarczy, przy większym projekcie staje się podstawą specyfikacji.')]},
              {'h2_uk': 'Шаблон ТЗ на сайт: 11 розділів',
               'h2_pl': 'Szablon briefu strony internetowej: 11 punktów',
               'blocks': [('p',
                           'Скопіюйте цей шаблон у документ і дайте відповідь на кожен пункт кількома реченнями. Якщо на щось відповіді ще немає, так і напишіть — це теж корисна інформація, і '
                           'рішення можна знайти разом на обговоренні.',
                           'Skopiuj ten szablon do dokumentu i odpowiedz na każdy punkt kilkoma zdaniami. Jeśli na któreś pytanie nie znasz jeszcze odpowiedzi, po prostu to zaznacz — to też cenna '
                           'informacja, a rozwiązanie znajdziemy razem podczas rozmowy.'),
                          ('ul',
                           [('<strong>Про компанію.</strong> Назва, чим займаєтеся, місто чи регіон, скільки працюєте, чим відрізняєтеся від конкурентів.',
                             '<strong>O firmie.</strong> Nazwa, czym się zajmujesz, miasto lub region, jak długo działasz, czym różnisz się od konkurencji.'),
                            ('<strong>Цілі сайту.</strong> Яку одну головну дію має зробити відвідувач: подзвонити, залишити заявку, записатися, купити.',
                             '<strong>Cel strony.</strong> Jakie jedno główne działanie ma wykonać odwiedzający: zadzwonić, wysłać zapytanie, zarezerwować termin, kupić.'),
                            ('<strong>Аудиторія.</strong> Хто ваш клієнт, звідки він прийде (Google, реклама, рекомендації), з якого пристрою найчастіше.',
                             '<strong>Odbiorcy.</strong> Kim jest Twój klient, skąd trafi na stronę (Google, reklamy, polecenia), z jakiego urządzenia korzysta najczęściej.'),
                            ('<strong>Конкуренти й референси.</strong> 2–3 сайти конкурентів і 2–3 сайти, які подобаються, з поясненням, що саме подобається.',
                             '<strong>Konkurencja i inspiracje.</strong> 2–3 strony konkurentów i 2–3 strony, które Ci się podobają, z opisem, co dokładnie Ci się w nich podoba.'),
                            ('<strong>Структура сторінок.</strong> Перелік сторінок чи блоків: головна, послуги, ціни, роботи, про нас, контакти.',
                             '<strong>Struktura.</strong> Lista podstron lub sekcji: strona główna, usługi, cennik, realizacje, o nas, kontakt.'),
                            ('<strong>Функції.</strong> Форма заявки, онлайн-запис, калькулятор, каталог, оплата, блог, куди надходять заявки.',
                             '<strong>Funkcje.</strong> Formularz, rezerwacja online, kalkulator, katalog, płatności, blog, dokąd mają trafiać zapytania.'),
                            ('<strong>Контент.</strong> Хто пише тексти, чи є фото робіт, логотип, фірмові кольори, відгуки клієнтів.',
                             '<strong>Treści.</strong> Kto przygotuje teksty, czy są zdjęcia realizacji, logo, kolory firmowe, opinie klientów.'),
                            ('<strong>Мови.</strong> Скільки мовних версій і яка з них основна.',
                             '<strong>Wersje językowe.</strong> Ile wersji językowych i która jest główna.'),
                            ('<strong>Інтеграції.</strong> Telegram, CRM, Google Analytics, Meta Pixel, система бронювання, платіжний сервіс.',
                             '<strong>Integracje.</strong> Telegram, CRM, Google Analytics, Piksel Meta, system rezerwacji, bramka płatności.'),
                            ('<strong>Терміни й бюджет.</strong> Бажана дата запуску, чи є жорсткий дедлайн, орієнтовний бюджет або діапазон.',
                             '<strong>Termin i budżet.</strong> Planowana data startu, czy jest sztywny termin, orientacyjny budżet lub widełki.'),
                            ('<strong>Доступи.</strong> Чи є домен, хостинг, пошта на домені, старий сайт, акаунти Google — і на кого вони оформлені.',
                             '<strong>Dostępy.</strong> Czy masz domenę, hosting, pocztę firmową, starą stronę, konta Google — i na kogo są zarejestrowane.')]),
                          ('card',
                           'Найважливіший пункт — ціль сайту. Якщо ви можете одним реченням сказати, що має зробити відвідувач, решта брифу складається значно легше.',
                           'Najważniejszy punkt to cel strony. Jeśli potrafisz jednym zdaniem powiedzieć, co ma zrobić odwiedzający, reszta briefu układa się znacznie łatwiej.')]},
              {'h2_uk': 'Приклад заповненого брифу',
               'h2_pl': 'Brief strony internetowej — przykład wypełniony',
               'blocks': [('p',
                           'Нижче — вигаданий приклад брифу для умовної клінінгової компанії з Познані. Це не реальний клієнт, а ілюстрація того, скільки тексту достатньо: коротко, конкретно, з '
                           'відповіддю на кожен пункт. Такого брифу нам вистачає, щоб запропонувати формат і назвати ціну.',
                           'Poniżej fikcyjny przykład briefu dla umownej firmy sprzątającej z Poznania. To nie jest prawdziwy klient, tylko ilustracja, ile tekstu wystarczy: krótko, konkretnie, z '
                           'odpowiedzią na każdy punkt. Taki brief wystarcza nam, żeby zaproponować format i podać cenę.'),
                          ('table',
                           [('Розділ', 'Punkt'), ('Відповідь (приклад)', 'Odpowiedź (przykład)')],
                           [[('Про компанію', 'O firmie'),
                             ('Клінінг квартир і офісів у Познані, команда з 6 людей, працюємо своїми засобами', 'Sprzątanie mieszkań i biur w Poznaniu, zespół 6 osób, pracujemy własnymi środkami')],
                            [('Ціль', 'Cel'), ('Заявка на прибирання з розрахунком ціни', 'Zapytanie o sprzątanie z wyliczeniem ceny')],
                            [('Аудиторія', 'Odbiorcy'),
                             ('Орендарі й власники квартир, невеликі офіси; приходять із Google і рекомендацій, переважно зі смартфона',
                              'Najemcy i właściciele mieszkań, małe biura; trafiają z Google i z poleceń, głównie z telefonu')],
                            [('Референси', 'Inspiracje'), ('2 сайти конкурентів; подобається, коли ціни видно одразу', '2 strony konkurencji; podoba nam się, gdy ceny widać od razu')],
                            [('Структура', 'Struktura'), ('Одна сторінка: послуги, пакети й ціни, як працюємо, фото, FAQ, контакти', 'Jedna strona: usługi, pakiety i ceny, jak pracujemy, zdjęcia, FAQ, kontakt')],
                            [('Функції', 'Funkcje'), ('Форма з вибором кількості кімнат, заявки в Telegram', 'Formularz z wyborem liczby pokoi, zapytania na Telegram')],
                            [('Контент', 'Treści'), ('Є логотип і фото до/після, тексти потрібна допомога', 'Mamy logo i zdjęcia przed i po, potrzebna pomoc z tekstami')],
                            [('Мови', 'Języki'), ('Польська основна, українська друга', 'Polski główny, ukraiński drugi')],
                            [('Інтеграції', 'Integracje'), ('Google Analytics, пізніше Meta Pixel під рекламу', 'Google Analytics, później Piksel Meta pod kampanie')],
                            [('Терміни й бюджет', 'Termin i budżet'), ('Запуск за 2 тижні, бюджет до €500', 'Start w ciągu 2 tygodni, budżet do 500 €')],
                            [('Доступи', 'Dostępy'), ('Домен є, хостингу немає, пошта на Gmail', 'Domena jest, hostingu brak, poczta na Gmailu')]]),
                          ('p',
                           'З такого брифу видно: людям потрібна ціна одразу, клієнти приходять зі смартфонів, а текстів ще немає. Під це підходить односторінковий сайт — ось як ми розбирали '
                           'різницю між форматами в статті <a href="post-lendinh-chy-vizytka">лендінг чи сайт-візитка</a>. Схожий реальний проєкт — <a href="case-elart-cleaning">лендінг '
                           'клінінгової компанії Elart Cleaning</a> у Познані з прайсом і бронюванням. Що ще варто передбачити на сайті клінінгу, ми зібрали на сторінці <a href="niche-klininh">сайт для клінінгової компанії</a>.',
                           'Z takiego briefu od razu widać: klienci chcą znać cenę, wchodzą z telefonu, a tekstów jeszcze nie ma. Pasuje tu strona typu one page — różnice między formatami '
                           'opisaliśmy w artykule <a href="post-lendinh-chy-vizytka">landing page czy strona wizytówka</a>. Podobny prawdziwy projekt to <a href="case-elart-cleaning">landing page '
                           'firmy sprzątającej Elart Cleaning</a> z Poznania, z cennikiem i rezerwacją. Co jeszcze warto zaplanować, opisaliśmy na stronie <a href="niche-klininh">strona internetowa dla firmy sprzątającej</a>.')]},
              {'h2_uk': 'Як заповнити ТЗ, якщо ви не розбираєтеся в сайтах',
               'h2_pl': 'Jak napisać brief, jeśli nie znasz się na stronach',
               'blocks': [('p',
                           'Пишіть мовою свого бізнесу, а не мовою веб-розробки. Замість «потрібен лендінг із CTA» напишіть «хочу, щоб люди одразу бачили ціну й залишали номер телефону». Студія '
                           'сама переведе це в структуру, функції й технічні рішення.',
                           'Pisz językiem swojej branży, a nie językiem programistów. Zamiast „potrzebny landing z CTA” napisz „chcę, żeby ludzie od razu widzieli cenę i zostawiali numer telefonu”. '
                           'Wykonawca sam przełoży to na strukturę, funkcje i rozwiązania techniczne.'),
                          ('ul',
                           [('Почніть із питань, які клієнти ставлять вам телефоном, — з них виходять блоки сайту й FAQ.',
                             'Zacznij od pytań, które klienci zadają Ci przez telefon — z nich powstają sekcje strony i FAQ.'),
                            ('Референси пояснюйте: «подобається, як подано ціни», а не просто посилання.', 'Opisuj inspiracje: „podoba mi się, jak pokazano ceny”, a nie tylko link.'),
                            ('Розділяйте «обов’язково зараз» і «можна пізніше» — це допомагає вкластися в бюджет.',
                             'Oddziel „musi być teraz” od „może być później” — to pomaga zmieścić się w budżecie.'),
                            ('Платформу не обов’язково обирати самому: різницю ми пояснили в статті <a href="post-wordpress-webflow-kod">WordPress, Webflow чи код</a>.',
                             'Platformy nie musisz wybierać sam — różnice opisaliśmy w artykule <a href="post-wordpress-webflow-kod">WordPress, Webflow czy kod</a>.')]),
                          ('p',
                           'Бюджет теж варто вказати, навіть діапазоном. Це не спосіб «вичавити» максимум, а орієнтир: під €300 і під €1500 ми запропонуємо різні рішення для тієї самої задачі. '
                           'Від чого залежить ціна, розписали в статті <a href="post-skilky-koshtuie-sait">скільки коштує сайт</a>.',
                           'Warto też podać budżet, choćby w widełkach. To nie sposób, by „wycisnąć” maksimum, tylko punkt odniesienia: przy 300 € i przy 1500 € zaproponujemy różne rozwiązania tego '
                           'samego problemu. Od czego zależy cena, opisaliśmy w artykule <a href="post-skilky-koshtuie-sait">ile kosztuje strona internetowa</a>.')]},
              {'h2_uk': 'Типові помилки в ТЗ на сайт',
               'h2_pl': 'Najczęstsze błędy w briefie',
               'blocks': [('p',
                           'Найчастіші помилки в ТЗ — розмита мета, «зробіть як у них» без пояснень, відсутність контенту й приховані функції, про які згадують уже під час розробки. Кожна з них '
                           'коштує часу, а іноді й перерахунку бюджету, тому краще закрити їх ще на етапі брифу.',
                           'Najczęstsze błędy w briefie to niejasny cel, „zróbcie jak u nich” bez wyjaśnienia, brak treści i ukryte funkcje, o których klient przypomina sobie w trakcie prac. Każdy z '
                           'nich kosztuje czas, a czasem zmianę wyceny, dlatego lepiej wyeliminować je już na etapie briefu.'),
                          ('h3', 'Мета «щоб був сайт»', 'Cel „żeby była strona”'),
                          ('p',
                           'Сайт без мети неможливо оцінити: незрозуміло, що вважати успіхом і які блоки потрібні. Навіть проста мета «отримувати заявки на прибирання з Познані» одразу підказує '
                           'структуру, тексти й форму.',
                           'Strony bez celu nie da się ocenić: nie wiadomo, co jest sukcesem ani jakie sekcje są potrzebne. Nawet prosty cel „pozyskiwać zapytania o sprzątanie w Poznaniu” od razu '
                           'podpowiada strukturę, teksty i formularz.'),
                          ('h3', 'Копія чужого сайту', 'Kopia cudzej strony'),
                          ('p',
                           'Референси корисні, але проєкти, де треба скопіювати чужий сайт один в один, ми не беремо. Краще пояснити, що саме працює в прикладі — подача цін, фото, простота форми, — '
                           'і ми зробимо це у вашому стилі.',
                           'Inspiracje są przydatne, ale projektów polegających na skopiowaniu cudzej strony 1:1 nie przyjmujemy. Lepiej opisać, co w przykładzie działa — sposób pokazania cen, '
                           'zdjęcia, prosty formularz — a zrobimy to w Twoim stylu.'),
                          ('h3', 'Контент «потім»', 'Treści „na później”'),
                          ('p',
                           'Дизайн під порожні блоки часто доводиться переробляти, коли з’являються справжні тексти й фото. Якщо текстів немає, напишіть це в брифі — допомогу з текстами можна '
                           'закласти в проєкт одразу.',
                           'Projekt graficzny pod puste sekcje często trzeba poprawiać, gdy pojawiają się prawdziwe teksty i zdjęcia. Jeśli nie masz treści, zaznacz to w briefie — pomoc z tekstami '
                           'można uwzględnić w projekcie od początku.'),
                          ('h3', 'Функції, про які згадали пізніше', 'Funkcje dodane w trakcie'),
                          ('p',
                           'Калькулятор, друга мова чи онлайн-оплата, додані після погодження структури, — це вже новий обсяг робіт, який оцінюється окремо. Навіть якщо функція потрібна «колись '
                           'потім», згадайте її в брифі: ми закладемо структуру так, щоб її було легко додати.',
                           'Kalkulator, druga wersja językowa czy płatności online dodane po zatwierdzeniu struktury to nowy zakres prac, wyceniany osobno. Nawet jeśli funkcja będzie potrzebna „kiedyś”, '
                           'wspomnij o niej w briefie — zaplanujemy strukturę tak, żeby łatwo ją dodać.')]},
              {'h2_uk': 'Як ми в студії працюємо з брифом',
               'h2_pl': 'Jak pracujemy z briefem w naszym studiu',
               'blocks': [('p',
                           'Бриф — друга сходинка нашого процесу після короткого обговорення формату, функцій, мов та інтеграцій. Протягом 24 годин після брифу ми даємо оцінку, а далі проєкт іде '
                           'етапами, і на кожному ви погоджуєте результат, перш ніж ми рухаємося далі.',
                           'Brief to drugi krok naszego procesu, po krótkiej rozmowie o formacie, funkcjach, językach i integracjach. W ciągu 24 godzin od otrzymania briefu podajemy wycenę, a dalej '
                           'projekt idzie etapami — na każdym zatwierdzasz efekt, zanim ruszymy dalej.'),
                          ('ul',
                           [('<strong>Бриф і матеріали.</strong> Тексти, фото, референси, логотип. Якщо зі структурою складно — допомагаємо.',
                             '<strong>Brief i materiały.</strong> Teksty, zdjęcia, inspiracje, logo. Jeśli struktura sprawia trudność — pomagamy.'),
                            ('<strong>Структура.</strong> Погоджуємо перелік сторінок і блоків до початку дизайну.',
                             '<strong>Struktura.</strong> Zatwierdzamy listę podstron i sekcji, zanim zaczniemy projekt graficzny.'),
                            ('<strong>Дизайн.</strong> Спершу 1–2 блоки, щоб погодити стилістику, потім решта сторінок.',
                             '<strong>Projekt graficzny.</strong> Najpierw 1–2 sekcje, żeby ustalić styl, potem pozostałe podstrony.'),
                            ('<strong>Розробка.</strong> Webflow, WordPress/Bricks, чистий код або React; форми, CMS, калькулятори, аналітика, оплати.',
                             '<strong>Wdrożenie.</strong> Webflow, WordPress/Bricks, czysty kod lub React; formularze, CMS, kalkulatory, analityka, płatności.'),
                            ('<strong>Правки.</strong> Ви надсилаєте всі правки одним списком — так нічого не губиться.',
                             '<strong>Poprawki.</strong> Przesyłasz wszystkie poprawki w jednej liście — dzięki temu nic nie ginie.'),
                            ('<strong>Запуск і передача.</strong> Домен, хостинг, пошта й усі доступи переходять вам.',
                             '<strong>Start i przekazanie.</strong> Domena, hosting, poczta i wszystkie dostępy trafiają do Ciebie.')]),
                          ('p',
                           'Від вас потрібні інформація й вчасні погодження етапів, технічну частину ми беремо на себе. Роботу оформлюємо за договором, оплата поетапна: перший платіж до старту, '
                           'наступний — після погодженого етапу або перед запуском.',
                           'Od Ciebie potrzebujemy informacji i terminowego zatwierdzania etapów, część techniczną bierzemy na siebie. Pracujemy na umowę i fakturę, płatność jest etapowa: pierwsza '
                           'wpłata przed startem, kolejna po zatwierdzonym etapie albo przed publikacją.'),
                          ('card',
                           'Шаблон вище можна надіслати нам заповненим або частково — решту уточнимо на короткому дзвінку чи в месенджері.',
                           'Szablon możesz wysłać nam wypełniony w całości albo częściowo — resztę ustalimy w krótkiej rozmowie lub na komunikatorze.')]},
              {'h2_uk': 'Скільки коштує сайт після брифу',
               'h2_pl': 'Ile kosztuje strona po briefie',
               'blocks': [('p',
                           'Після брифу ми називаємо точну ціну, але базові орієнтири відомі заздалегідь: лендінг — від €300, багатосторінковий сайт — від €450, інтернет-магазин — від €800. Для '
                           'складних проєктів вартість рахуємо саме за брифом, оцінка — протягом 24 годин.',
                           'Dokładną cenę podajemy po briefie, ale punkty odniesienia są znane z góry: landing page od 300 €, strona firmowa od 450 €, sklep internetowy od 800 €. Przy złożonych '
                           'projektach wycena powstaje właśnie na podstawie briefu, w ciągu 24 godzin. Ceny są bez VAT (zw.).'),
                          ('table',
                           [('Формат', 'Format'), ('Ціна', 'Cena'), ('Терміни', 'Termin')],
                           [[('<a href="svc-lending">Лендінг</a>', '<a href="svc-lending">Landing page</a>'), ('від €300', 'od 300 €'), ('3–5 днів', '3–5 dni')],
                            [('<a href="svc-sait-vizytka">Сайт-візитка</a>', '<a href="svc-sait-vizytka">Strona wizytówka</a>'), ('від €300', 'od 300 €'), ('Після брифу', 'Po briefie')],
                            [('<a href="svc-korporatyvnyi-sait">Багатосторінковий сайт</a>', '<a href="svc-korporatyvnyi-sait">Strona firmowa</a>'), ('від €450', 'od 450 €'),
                             ('15–25 роб. днів', '15–25 dni rob.')],
                            [('<a href="svc-internet-magazyn">Інтернет-магазин</a>', '<a href="svc-internet-magazyn">Sklep internetowy</a>'), ('від €800', 'od 800 €'),
                             ('20–30 роб. днів', '20–30 dni rob.')]]),
                          ('p',
                           'Терміни відраховуються після погодження обсягу, договору й першого платежу. Після запуску сайт можна залишити на нашій підтримці — від €20 на місяць. Усі тарифи зібрані '
                           'на сторінці <a href="prices">ціни</a>, а надіслати бриф можна через <a href="contacts">контакти</a>.',
                           'Termin liczymy od zatwierdzenia zakresu, podpisania umowy i pierwszej wpłaty. Po starcie możesz zostawić stronę pod naszą opieką — od 20 € miesięcznie. Wszystkie pakiety '
                           'znajdziesz na stronie <a href="prices">cennik</a>, a brief wyślesz przez <a href="contacts">kontakt</a>.')]}],
 'faq': [['Що має бути в ТЗ на сайт?',
          'Co powinien zawierać brief strony internetowej?',
          'Мінімум — 11 пунктів: про компанію, мета сайту, аудиторія, конкуренти й референси, структура сторінок, функції, контент, мови, інтеграції, терміни й бюджет, доступи до домену й '
          'хостингу. Для невеликого сайту достатньо кількох речень на кожен пункт, для магазину чи сервісу функції й інтеграції розписують детальніше.',
          'Minimum to 11 punktów: o firmie, cel strony, odbiorcy, konkurencja i inspiracje, struktura, funkcje, treści, wersje językowe, integracje, termin i budżet oraz dostępy do domeny i '
          'hostingu. Przy małej stronie wystarczy kilka zdań na punkt, przy sklepie lub serwisie funkcje i integracje opisuje się dokładniej.'],
         ['Чим бриф відрізняється від технічного завдання?',
          'Czym brief różni się od specyfikacji technicznej?',
          'Бриф пише замовник: що за бізнес, яка мета, які побажання. ТЗ — детальніший документ, який виконавець складає на основі брифу: точна структура, функції, логіка форм, інтеграції. '
          'Для лендінгу чи візитки брифу зазвичай досить, повне ТЗ потрібне магазинам і складним сайтам.',
          'Brief pisze klient: czym zajmuje się firma, jaki jest cel i jakie oczekiwania. Specyfikacja to bardziej szczegółowy dokument, który wykonawca przygotowuje na podstawie briefu: '
          'dokładna struktura, funkcje, logika formularzy, integracje. Przy landingu czy wizytówce brief zwykle wystarczy, specyfikacja przydaje się przy sklepach i dużych serwisach.'],
         ['Хто має писати ТЗ на сайт — замовник чи студія?',
          'Kto powinien przygotować brief — klient czy wykonawca?',
          'Бриф заповнює замовник, бо лише він знає свій бізнес і клієнтів. Технічну частину — платформу, функції, інтеграції — формулює студія. У нас так: ви надсилаєте бриф своїми словами, '
          'ми уточнюємо деталі й погоджуємо з вами структуру перед дизайном.',
          'Brief wypełnia klient, bo tylko on zna swoją firmę i klientów. Część techniczną — platformę, funkcje, integracje — opracowuje wykonawca. U nas wygląda to tak: przesyłasz brief '
          'własnymi słowami, my dopytujemy o szczegóły i zatwierdzamy z Tobą strukturę przed projektem graficznym.'],
         ['Що робити, якщо немає текстів і фото?',
          'Co zrobić, jeśli nie mam tekstów i zdjęć?',
          'Так і напишіть у брифі. Ми допомагаємо зі структурою й текстами, а фото можна додати пізніше або використати тимчасові. Важливо знати це заздалегідь, щоб дизайн робився під реальний '
          'обсяг контенту, а не під порожні блоки.',
          'Napisz to wprost w briefie. Pomagamy ze strukturą i tekstami, a zdjęcia można dodać później albo użyć tymczasowych. Ważne, żeby wiedzieć o tym wcześniej — wtedy projekt powstaje pod '
          'prawdziwą ilość treści, a nie pod puste sekcje.'],
         ['Скільки часу займає оцінка сайту за брифом?',
          'Ile trwa wycena strony na podstawie briefu?',
          'Оцінку ми даємо протягом 24 годин після брифу. На заявки відповідаємо зазвичай за кілька годин у робочий час (пн–пт); повідомлення ввечері чи у вихідні обробляємо наступного робочого '
          'дня.',
          'Wycenę podajemy w ciągu 24 godzin od otrzymania briefu. Na zapytania odpowiadamy zwykle w ciągu kilku godzin w dni robocze (pn–pt); wiadomości wysłane wieczorem lub w weekend '
          'obsługujemy następnego dnia roboczego.'],
         ['Чи можна змінити ТЗ під час роботи?',
          'Czy można zmienić brief w trakcie prac?',
          'Так, але зміни затвердженої структури чи новий функціонал оцінюються окремо, бо це вже інший обсяг робіт. Дрібні уточнення в межах погодженого — звичайна частина процесу. Тому '
          'найкраще згадати в брифі навіть ті функції, які знадобляться «колись потім».',
          'Tak, ale zmiany zatwierdzonej struktury lub nowe funkcje wyceniamy osobno, bo to już inny zakres prac. Drobne doprecyzowania w ramach ustaleń to normalna część procesu. Dlatego '
          'najlepiej wspomnieć w briefie nawet o funkcjach, które będą potrzebne „kiedyś”.']],
 'service': 'korporatyvnyi-sait',
 'cta_uk': 'Заповніть бриф за шаблоном — хоч повністю, хоч частково — і надішліть нам. Протягом 24 годин запропонуємо формат і назвемо ціну.',
 'cta_pl': 'Wypełnij brief według szablonu — w całości albo częściowo — i wyślij go do nas. W ciągu 24 godzin zaproponujemy format i podamy cenę.',
 'date': '2026-09-25'}
