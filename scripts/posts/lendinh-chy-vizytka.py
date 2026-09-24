# Стаття блогу. Автор: Andrii Shestakov. Поля й формат — див. scripts/build_blog.py.

POST = {'key': 'lendinh-chy-vizytka',
 'path_uk': '/blog/lendinh-chy-sait-vizytka/',
 'path_pl': '/pl/blog/landing-page-czy-strona-wizytowka/',
 'img': 'assets/why-3.webp',
 'title_uk': 'Лендінг чи сайт-візитка: що обрати для бізнесу | SHSTKV Digital',
 'title_pl': 'Landing page czy strona wizytówka — co wybrać | SHSTKV Digital',
 'desc_uk': 'Чим відрізняється лендінг від сайту-візитки, кому що підходить і коли потрібен багатосторінковий сайт. Порівняльна таблиця, типові помилки й ціни від €300.',
 'desc_pl': 'Landing page a strona wizytówka: czym się różnią, kiedy wybrać każdą z nich i kiedy potrzebna jest większa strona. Tabela porównawcza, błędy i ceny od 300 €.',
 'h1_uk': 'Лендінг чи сайт-візитка: що обрати для бізнесу',
 'h1_pl': 'Landing page czy strona wizytówka — co wybrać?',
 'sub_uk': 'Розбираємо різницю, типові помилки й те, як обрати формат під свою задачу.',
 'sub_pl': 'Różnice, typowe błędy i prosty sposób, by dobrać format strony do celu.',
 'topic_uk': 'Формати',
 'topic_pl': 'Formaty',
 'minutes': 8,
 'answer_uk': 'Лендінг — це одна сторінка під одну пропозицію, куди ведуть рекламу, щоб отримати заявку. Сайт-візитка представляє компанію: послуги, ціни, приклади робіт і контакти на одній або 1–5 '
              'сторінках, її знаходять у Google за назвою чи «послуга + місто». Запускаєте рекламу на один продукт — беріть лендінг. Потрібна постійна адреса бізнесу в мережі — візитку.',
 'answer_pl': 'Landing page to jedna strona pod jedną ofertę, na którą kieruje się ruch z reklam, żeby zbierać zapytania. Strona wizytówka przedstawia firmę: usługi, cennik, realizacje i kontakt na '
              'jednej lub 1–5 podstronach, a klienci trafiają na nią z Google po nazwie lub frazie „usługa + miasto”. Planujesz kampanię na jeden produkt — wybierz landing. Potrzebujesz stałej '
              'wizytówki firmy w sieci — wizytówkę.',
 'sections': [{'h2_uk': 'Що таке лендінг',
               'h2_pl': 'Co to jest landing page',
               'blocks': [('p',
                           'Лендінг (landing page, посадкова сторінка) — це одна довга сторінка, яка продає одну конкретну пропозицію: послугу, продукт, курс, акцію. Усе на ній працює на одну дію — '
                           'залишити заявку, подзвонити чи записатися. Меню, яке веде «кудись ще», там зазвичай немає, бо кожен зайвий клік — це шанс, що людина піде.',
                           'Landing page to jedna długa strona, która sprzedaje jedną konkretną ofertę: usługę, produkt, kurs albo promocję. Wszystko na niej prowadzi do jednego działania — wysłania '
                           'formularza, telefonu lub rezerwacji. Zwykle nie ma tu rozbudowanego menu, bo każde kliknięcie „gdzieś indziej” to szansa, że klient zamknie kartę.'),
                          ('p',
                           'Лендінг рідко живе сам по собі. Трафік на нього ведуть із Google Ads, Meta чи TikTok, а сторінка має швидко відповісти на запитання з оголошення: що це, скільки коштує, '
                           'чому вам можна довіряти й що робити далі. Тому ми завжди питаємо клієнта не «який дизайн», а «звідки прийдуть люди».',
                           'Landing rzadko działa w pojedynkę. Ruch kieruje się na niego z Google Ads, Meta albo TikToka, a strona ma szybko odpowiedzieć na pytania z reklamy: co to jest, ile '
                           'kosztuje, dlaczego warto Ci zaufać i co zrobić dalej. Dlatego zanim zaczniemy rozmawiać o wyglądzie, pytamy, skąd przyjdą odwiedzający.'),
                          ('p',
                           'Приклад із нашої практики — <a href="case-bellissimo-home">лендінг салону італійських меблів Bellissimo Home</a> у Вроцлаві. Людина одразу може порахувати орієнтовну '
                           'вартість у калькуляторі й записатися на зустріч у шоурумі, не шукаючи потрібну сторінку.',
                           'Przykład z naszej praktyki to <a href="case-bellissimo-home">landing page salonu włoskich mebli Bellissimo Home</a> we Wrocławiu. Odwiedzający od razu liczy orientacyjny '
                           'koszt w kalkulatorze i umawia się na spotkanie w showroomie, bez szukania właściwej podstrony.')]},
              {'h2_uk': 'Що таке сайт-візитка',
               'h2_pl': 'Co to jest strona wizytówka',
               'blocks': [('p',
                           "Сайт-візитка — це компактний сайт, який представляє компанію цілком: хто ви, які послуги надаєте, де працюєте, скільки це коштує і як з вами зв'язатися. Він буває "
                           'односторінковим (one page) або має 1–5 окремих сторінок: головна, послуги, ціни, роботи, контакти.',
                           'Strona wizytówka to niewielka witryna, która pokazuje firmę w całości: kim jesteś, co robisz, gdzie działasz, ile to kosztuje i jak się z Tobą skontaktować. Może to być '
                           'strona one page albo 1–5 podstron: start, usługi, cennik, realizacje, kontakt.'),
                          ('p',
                           'Головна різниця — у джерелі клієнтів. На візитку рідко ведуть рекламу: її знаходять за назвою компанії, з профілю в Google Maps, з паперової візитки чи за локальним '
                           'запитом на кшталт «клінінг Познань». Для такого пошуку важливі дані компанії, адреса, послуги окремими блоками й базове SEO.',
                           'Najważniejsza różnica to źródło klientów. Na wizytówkę rzadko kieruje się reklamę: ludzie trafiają na nią po nazwie firmy, z Profilu Firmy w Google, z papierowej '
                           'wizytówki albo po lokalnej frazie typu „sprzątanie mieszkań Poznań”. Liczą się tu dane firmy, adres, opisane usługi i podstawowe SEO.'),
                          ('p',
                           'Візитка — це постійна адреса бізнесу в мережі. Її відкривають, щоб перевірити, чи ви справжні, перед дзвінком, після рекомендації знайомого або коли порівнюють кількох '
                           'підрядників.',
                           'Wizytówka to stały adres firmy w internecie. Otwiera się ją, żeby sprawdzić, czy firma naprawdę istnieje: przed telefonem, po poleceniu znajomego albo przy porównywaniu '
                           'kilku wykonawców. Dla wielu klientów to też miejsce, gdzie szukają NIP-u i danych do faktury.')]},
              {'h2_uk': 'Чим відрізняється лендінг від сайту-візитки',
               'h2_pl': 'Landing page a strona wizytówka — różnice',
               'blocks': [('p',
                           'Зовні обидва формати можуть виглядати схоже, особливо якщо візитка зроблена як one page. Відрізняються вони задачею, джерелом трафіку й тим, як їх оцінюють.',
                           'Z zewnątrz oba formaty mogą wyglądać podobnie, zwłaszcza gdy wizytówka jest zrobiona jako one page. Różnią się celem, źródłem ruchu i tym, po czym ocenia się, czy '
                           'działają.'),
                          ('table',
                           [('Критерій', 'Kryterium'), ('Лендінг', 'Landing page'), ('Сайт-візитка', 'Strona wizytówka')],
                           [[('Задача', 'Cel'), ('Продати одну пропозицію', 'Sprzedać jedną ofertę'), ('Представити компанію', 'Przedstawić firmę')],
                            [('Обсяг', 'Zakres'), ('Одна сторінка', 'Jedna strona'), ('One page або 1–5 сторінок', 'One page lub 1–5 podstron')],
                            [('Звідки люди', 'Skąd ruch'),
                             ('Реклама: Google Ads, Meta, TikTok', 'Reklamy: Google Ads, Meta, TikTok'),
                             ('Пошук за назвою, Google Maps, рекомендації', 'Wyszukiwanie po nazwie, Mapy Google, polecenia')],
                            [('Головна дія', 'Główne działanie'), ('Одна заявка чи запис', 'Jedno zapytanie lub rezerwacja'), ('Дзвінок, лист, візит', 'Telefon, wiadomość, wizyta')],
                            [('Як оцінюють', 'Jak mierzyć'), ('Заявки з реклами', 'Zapytania z kampanii'), ('Звернення й видимість у пошуку', 'Kontakty i widoczność w Google')],
                            [('Ціна в нас', 'Cena u nas'), ('від €300', 'od 300 €'), ('від €300, з адмінкою €450', 'od 300 €, z panelem 450 €')]]),
                          ('p',
                           'Ціни однакові не випадково: за обсягом роботи це схожі проєкти. Різниця — у структурі, текстах і тому, що саме ми налаштовуємо: для лендінгу — структуру під рекламне '
                           'оголошення й, за потреби, аналітику та пікселі, для візитки — дані компанії й локальне SEO.',
                           'Ceny są podobne nie bez powodu: pod względem nakładu pracy to zbliżone projekty. Różnica leży w strukturze, tekstach i konfiguracji: przy landingu układ pod konkretną '
                           'reklamę i w razie potrzeby analitykę oraz piksele, przy wizytówce — dane firmy i lokalne SEO.')]},
              {'h2_uk': 'Коли обрати лендінг',
               'h2_pl': 'Kiedy wybrać landing page',
               'blocks': [('p',
                           'Лендінг — правильний вибір, коли у вас є одна зрозуміла пропозиція і план, як приводити на неї людей. Типові ситуації з наших проєктів:',
                           'Landing page to dobry wybór, gdy masz jedną jasną ofertę i plan, jak przyprowadzić na nią ludzi. Typowe sytuacje z naszych projektów:'),
                          ('ul',
                           [('запускаєте рекламу на одну послугу — монтаж, ремонт, клінінг, встановлення сонячних панелей;',
                             'startujesz z kampanią na jedną usługę — montaż, remont, sprzątanie, fotowoltaikę;'),
                            ('продаєте курс, консультацію чи подію з конкретною датою;', 'sprzedajesz kurs, konsultację albo wydarzenie z konkretną datą;'),
                            ('тестуєте нову нішу чи місто й не хочете одразу вкладатися у великий сайт;', 'testujesz nową branżę lub miasto i nie chcesz od razu inwestować w dużą stronę;'),
                            ('у вас уже є основний сайт, а під рекламну кампанію потрібна окрема сторінка;', 'masz już stronę firmową, a pod kampanię potrzebujesz osobnej strony;'),
                            ('B2B-пропозиція, де клієнту потрібна одна зустріч чи розрахунок, а не каталог.',
                             'oferta B2B, w której klient ma umówić spotkanie lub poprosić o wycenę, a nie przeglądać katalog.')]),
                          ('p',
                           'Наприклад, для клінінгової компанії з Познані ми зробили <a href="case-elart-cleaning">лендінг Elart Cleaning</a>: прайс і пакети, кроки співпраці, фото до/після та '
                           'онлайн-бронювання на одній сторінці. Детальніше про формат і що входить у роботу — на сторінці <a href="svc-lending">створення лендінгу під ключ</a>.',
                           'Dla firmy sprzątającej z Poznania zrobiliśmy <a href="case-elart-cleaning">landing page Elart Cleaning</a>: cennik i pakiety, etapy współpracy, zdjęcia przed i po oraz '
                           'rezerwacja online na jednej stronie. Więcej o tym formacie i zakresie prac znajdziesz na stronie <a href="svc-lending">tworzenie landing page</a>.')]},
              {'h2_uk': 'Коли обрати сайт-візитку',
               'h2_pl': 'Kiedy wybrać stronę wizytówkę',
               'blocks': [('p',
                           'Візитка підходить бізнесу, який працює локально, отримує клієнтів переважно з рекомендацій і пошуку та не планує постійної реклами. Салон, барбер, бухгалтер, юрист, '
                           'будівельна бригада, стоматологічний кабінет — класичні приклади.',
                           'Wizytówka sprawdza się w firmach działających lokalnie, które pozyskują klientów głównie z poleceń i wyszukiwarki, a nie z ciągłych kampanii. Salon, barber, biuro '
                           'rachunkowe, kancelaria, ekipa budowlana, gabinet stomatologiczny — to klasyczne przykłady.'),
                          ('p',
                           "Для такого бізнесу важливо, щоб людина за хвилину зрозуміла, що ви робите, побачила ціни чи хоча б діапазон, приклади робіт і могла зв'язатися в один дотик зі смартфона. "
                           "Якщо послуг кілька і вас шукають за різними запитами, краще розбити візитку на кілька сторінок: кожна з них має шанс з'явитися в Google за своїм запитом.",
                           'W takiej firmie liczy się to, żeby klient w minutę zrozumiał, czym się zajmujesz, zobaczył ceny albo chociaż widełki, realizacje i mógł się skontaktować jednym '
                           'dotknięciem na telefonie. Jeśli masz kilka usług i ludzie szukają Cię na różne frazy, lepiej podzielić wizytówkę na podstrony — każda ma wtedy szansę pojawić się w Google '
                           'na swoje zapytanie.'),
                          ('card',
                           'Простий тест: якщо ви не збираєтеся платити за рекламу щомісяця, лендінг вам, найімовірніше, не потрібен. Почніть із візитки й профілю в Google Business — це дешевше в '
                           'утриманні й працює без постійного бюджету.',
                           'Prosty test: jeśli nie planujesz co miesiąc płacić za reklamy, landing page raczej nie jest Ci potrzebny. Zacznij od wizytówki i Profilu Firmy w Google — to tańsze w '
                           'utrzymaniu i działa bez stałego budżetu reklamowego.'),
                          ('p',
                           'Що входить у такий сайт і скільки коштує версія з адмін-панеллю, описали на сторінці <a href="svc-sait-vizytka">сайт-візитка під ключ</a>.',
                           'Co zawiera taka strona i ile kosztuje wersja z panelem edycji, opisaliśmy na stronie <a href="svc-sait-vizytka">strona wizytówka dla firmy</a>.')]},
              {'h2_uk': 'Коли потрібен багатосторінковий сайт',
               'h2_pl': 'Kiedy potrzebna jest większa strona firmowa',
               'blocks': [('p',
                           'Буває, що ні лендінг, ні візитка задачу не закривають. Це видно ще на брифі: клієнт перелічує десять послуг, три філії, навчання й франшизу — і все це треба вмістити в '
                           '«невеликий сайт».',
                           'Czasem ani landing, ani wizytówka nie wystarczą. Widać to już na etapie briefu: klient wymienia dziesięć usług, trzy lokalizacje, szkolenia i franczyzę — i wszystko ma '
                           'się zmieścić na „małej stronie”.'),
                          ('ul',
                           [('більше 5–6 послуг, і кожну шукають окремим запитом;', 'masz więcej niż 5–6 usług i każdej szuka się inną frazą;'),
                            ('кілька філій, міст чи аудиторій (клієнти, партнери, франчайзі);', 'kilka oddziałów, miast albo grup odbiorców (klienci, partnerzy, franczyzobiorcy);'),
                            ('потрібні кілька мов, блог чи регулярні новини;', 'potrzebujesz kilku wersji językowych, bloga lub aktualności;'),
                            ('онлайн-запис у різні філії, калькулятори, інтеграції з CRM.', 'rezerwacje do różnych oddziałów, kalkulatory, integracje z CRM.')]),
                          ('p',
                           'Так було з мережею барбершопів у Дніпрі: <a href="case-dictator-barbershop">сайт DICTATOR</a> веде клієнта до запису в потрібну філію, а окремо продає навчання в академії '
                           'та франшизу. Візитка з цим не впоралася б. Такий <a href="svc-korporatyvnyi-sait">багатосторінковий сайт компанії</a> у нас коштує від €450 і займає 15–25 робочих днів, а '
                           'для складніших задач вартість рахуємо після брифу.',
                           'Tak było w przypadku sieci barber shopów z Dniepru: <a href="case-dictator-barbershop">strona DICTATOR</a> prowadzi klienta do rezerwacji w wybranym salonie, a osobno '
                           'sprzedaje szkolenia w akademii i franczyzę. Wizytówka by tego nie udźwignęła. Taka <a href="svc-korporatyvnyi-sait">rozbudowana strona firmowa</a> kosztuje u nas od 450 € '
                           'i powstaje w 15–25 dni roboczych, a przy bardziej złożonych projektach wycenę robimy po briefie.')]},
              {'h2_uk': 'Типові помилки при виборі',
               'h2_pl': 'Najczęstsze błędy przy wyborze',
               'blocks': [('p',
                           'За роки роботи ми бачили ті самі помилки знову й знову. Вони коштують не стільки грошей на розробку, скільки часу й втрачених клієнтів.',
                           'Przez lata widzieliśmy te same błędy w kółko. Kosztują nie tyle pieniądze na wykonanie strony, ile czas i utraconych klientów.'),
                          ('h3', 'Лендінг без рекламного трафіку', 'Landing bez ruchu z reklam'),
                          ('p',
                           'Власник замовляє лендінг, запускає його — і нічого не відбувається. Одна сторінка з одним заголовком майже не має шансів у пошуку за багатьма запитами, а без реклами на '
                           'неї просто ніхто не приходить. Якщо бюджету на рекламу немає, краще вкласти ті самі гроші у візитку з базовим SEO.',
                           'Właściciel zamawia landing, publikuje go — i nic się nie dzieje. Jedna strona z jednym nagłówkiem ma małe szanse w Google na wiele fraz, a bez reklam po prostu nikt na '
                           'nią nie trafia. Jeśli nie masz budżetu na kampanie, lepiej przeznaczyć te same pieniądze na wizytówkę z podstawowym SEO.'),
                          ('h3', 'Візитка на десять послуг', 'Wizytówka na dziesięć usług'),
                          ('p',
                           'Усі послуги в одному списку на одній сторінці: Google не розуміє, за якими запитами її показувати, а клієнт не знаходить свою послугу. Для великого переліку потрібні '
                           'окремі сторінки — хоча б для 3–5 головних напрямів.',
                           'Wszystkie usługi w jednej liście na jednej stronie: Google nie wie, na jakie frazy ją pokazywać, a klient nie może znaleźć tego, czego szuka. Przy długiej liście '
                           'potrzebne są osobne podstrony — choćby dla 3–5 głównych usług.'),
                          ('h3', 'Вибір за ціною, а не за задачею', 'Wybór po cenie, a nie po celu'),
                          ('p',
                           '«Зробіть найдешевше, потім розширимо» — нормальна стратегія, якщо заздалегідь продумати структуру. Гірше, коли лендінг потім намагаються перетворити на сайт компанії: '
                           'простіше й дешевше одразу закласти правильний формат.',
                           '„Zróbmy najtaniej, potem się rozbuduje” — to rozsądne podejście, o ile od początku przemyśli się strukturę. Gorzej, gdy landing próbuje się później przerobić na stronę '
                           'firmową: prościej i taniej od razu wybrać właściwy format.')]},
              {'h2_uk': 'Скільки коштує і як ми допомагаємо обрати',
               'h2_pl': 'Ile to kosztuje i jak pomagamy wybrać',
               'blocks': [('p',
                           'Лендінг у нас коштує від €300 (тариф «Старт», запуск за 3 дні) або €450 у тарифі «Про» з адмін-панеллю, анімаціями й аналітикою — запуск за 4–5 днів. Візитка — від €300, '
                           'з адмін-панеллю — €450. В обидва формати входять індивідуальний дизайн, мобільна версія, базове SEO, форма заявки з відправкою в Telegram і 30 днів підтримки.',
                           'Landing page kosztuje u nas od 300 € (pakiet Start, gotowy w 3 dni) albo 450 € w pakiecie Pro z panelem edycji, animacjami i analityką — gotowy w 4–5 dni. Wizytówka — od '
                           '300 €, z panelem edycji 450 €. Ceny są bez VAT (zwolnienie z VAT), płatność na umowę i fakturę, w EUR, USD lub PLN. W obu formatach masz indywidualny projekt, wersję '
                           'mobilną, podstawowe SEO, formularz z wysyłką na Telegram i 30 dni wsparcia.'),
                          ('card',
                           'Якщо сумніваєтеся, почніть не з формату, а з двох питань: звідки прийдуть клієнти і яку одну дію вони мають зробити на сайті. На брифі ми відповідаємо на них разом і '
                           'радимо формат — оцінку отримаєте протягом 24 годин.',
                           'Jeśli nie wiesz, co wybrać, zacznij nie od formatu, tylko od dwóch pytań: skąd przyjdą klienci i jakie jedno działanie mają wykonać na stronie. Na briefie odpowiadamy na '
                           'nie razem i proponujemy format — wycenę dostajesz w ciągu 24 godzin.')]}],
 'faq': [['Чим відрізняється лендінг від сайту-візитки?',
          'Czym różni się landing page od strony wizytówki?',
          'Лендінг продає одну пропозицію, а сайт-візитка представляє компанію цілком. На лендінг ведуть рекламу, і все на сторінці підводить до однієї заявки. Візитку знаходять за назвою чи '
          'локальним запитом, на ній є послуги, ціни, приклади робіт і контакти — на одній або 1–5 сторінках.',
          'Landing page sprzedaje jedną ofertę, a strona wizytówka przedstawia całą firmę. Na landing kieruje się ruch z reklam i wszystko na nim prowadzi do jednego zapytania. Wizytówkę klienci '
          'znajdują po nazwie albo lokalnej frazie; są na niej usługi, cennik, realizacje i kontakt — na jednej stronie lub 1–5 podstronach.'],
         ['Що краще для малого бізнесу: лендінг чи візитка?',
          'Co lepsze dla małej firmy: landing czy wizytówka?',
          'Для більшості малих локальних бізнесів краще починати з візитки. Вона працює без постійного рекламного бюджету: її знаходять у Google, з профілю в Google Maps і за рекомендаціями. Лендінг '
          'має сенс, коли ви вже плануєте рекламу на конкретну послугу й готові за неї платити щомісяця.',
          'Dla większości małych, lokalnych firm lepszym startem jest wizytówka. Działa bez stałego budżetu na reklamy: klienci trafiają na nią z Google, z Profilu Firmy w Mapach i z poleceń. '
          'Landing page ma sens, gdy planujesz kampanię na konkretną usługę i jesteś gotów regularnie za nią płacić.'],
         ['Чи можна зробити сайт-візитку на одній сторінці?',
          'Czy strona wizytówka może być typu one page?',
          'Так, візитка на одній сторінці (one page) — поширений формат. Він підходить, коли у вас одна-дві послуги й усе вміщується в один скрол. Від лендінгу така візитка відрізняється змістом: '
          'вона розповідає про компанію й дає контакти, а не веде до однієї пропозиції з реклами.',
          'Tak, strona wizytówka typu one page to popularne rozwiązanie. Sprawdza się, gdy masz jedną–dwie usługi i wszystko mieści się w jednym przewijaniu. Od landing page różni się treścią: '
          'opowiada o firmie i podaje kontakt, zamiast prowadzić do jednej oferty z kampanii reklamowej.'],
         ['Скільки коштує лендінг і сайт-візитка?',
          'Ile kosztuje landing page, a ile strona wizytówka?',
          'У нашій студії обидва формати коштують від €300. Лендінг у тарифі «Про» з адмін-панеллю, анімаціями й аналітикою — €450, візитка з адмін-панеллю — теж €450. Лендінг «Старт» запускаємо за '
          '3 дні, «Про» — за 4–5 днів. Багатосторінковий сайт — від €450, 15–25 робочих днів.',
          'U nas oba formaty kosztują od 300 €. Landing w pakiecie Pro z panelem edycji, animacjami i analityką to 450 €, wizytówka z panelem — również 450 €. Landing Start uruchamiamy w 3 dni, Pro '
          'w 4–5 dni. Rozbudowana strona firmowa to koszt od 450 € i 15–25 dni roboczych. Ceny bez VAT.'],
         ['Чи можна потім перетворити лендінг на повноцінний сайт?',
          'Czy landing można później rozbudować do pełnej strony?',
          'Так, але це простіше, якщо структуру продумати заздалегідь. Лендінг можна залишити як сторінку під рекламу, а поруч зробити сайт компанії в тому самому стилі. Переробляти одну рекламну '
          'сторінку на багатосторінковий сайт зазвичай довше, ніж одразу обрати правильний формат, тому це обговорюємо ще на брифі.',
          'Tak, ale łatwiej, gdy struktura jest przemyślana od początku. Landing może zostać stroną pod kampanie, a obok powstaje strona firmowa w tym samym stylu. Przerabianie jednej strony '
          'reklamowej na serwis z wieloma podstronami zwykle trwa dłużej niż od razu dobrany format, dlatego rozmawiamy o tym już na briefie.']],
 'service': 'lending',
 'cta_uk': 'Не впевнені, що вам потрібно — лендінг чи візитка? Опишіть бізнес і джерела клієнтів, і ми порадимо формат та назвемо ціну протягом 24 годин.',
 'cta_pl': 'Nie wiesz, czy potrzebujesz landing page, czy wizytówki? Opisz swoją firmę i to, skąd przychodzą klienci — doradzimy format i podamy cenę w ciągu 24 godzin.',
 'date': '2026-09-24'}
