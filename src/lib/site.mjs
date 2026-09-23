/* Карта сторінок сайту: URL кожної мовної версії + SEO-теги.
   hreflang, canonical, sitemap і перемикач мов будуються звідси. */

export const SITE = "https://www.shstkv-digital.com";
export const LANGS = ["uk", "pl"];
export const DEFAULT_LANG = "uk";
export const OG_LOCALE = { uk: "uk_UA", pl: "pl_PL" };

export const BUSINESS = {
  name: "Web Shestakov",
  legalName: "Andrii Shestakov",
  founder: "Andrii Shestakov",
  email: "webdeveloperandrii@gmail.com",
  phone: "+48577503534",
  address: {
    streetAddress: "Akacjowa 96j lok. 1",
    postalCode: "55-093",
    addressLocality: "Kiełczów",
    addressRegion: "dolnośląskie",
    addressCountry: "PL"
  },
  vatID: "PL8961659922",
  sameAs: ["https://www.instagram.com/web.shestakov", "https://t.me/Andrii_DEV9"]
};

/* group — сторінки однієї групи є перекладами одна одної (hreflang). */
export const PAGES = [
  {
    group: "home",
    lang: "uk",
    path: "/",
    template: "home",
    title: "Розробка сайтів під ключ від $300 — Україна та Польща | Web Shestakov",
    description:
      "Лендінги, корпоративні сайти, інтернет-магазини та Telegram-боти під ключ від $300. Запуск від 3 днів, 30+ проєктів для бізнесу в Польщі, Україні та ЄС. Безкоштовна консультація.",
    priority: 1.0
  },
  {
    group: "home",
    lang: "pl",
    path: "/pl/",
    template: "home",
    title: "Tworzenie stron internetowych dla firm — Wrocław i cała Polska | Web Shestakov",
    description:
      "Strony internetowe, landing page, sklepy online i boty Telegram pod klucz. Start od 3 dni, ponad 30 realizacji w Polsce i UE. Obsługa po polsku i ukraińsku. Bezpłatna konsultacja.",
    priority: 1.0
  },
  {
    group: "portfolio",
    lang: "uk",
    path: "/portfolio/",
    template: "portfolio",
    title: "Портфоліо: сайти та інтернет-магазини, які ми створили | Web Shestakov",
    description:
      "Кейси Web Shestakov: лендінги, корпоративні сайти та інтернет-магазини для бізнесу в Польщі, Україні, Німеччині, Чехії та Нідерландах.",
    priority: 0.8
  },
  {
    group: "about",
    lang: "uk",
    path: "/pro-nas/",
    template: "about",
    title: "Про нас — Web Shestakov, веб-студія у Вроцлаві: 12+ років досвіду, 35+ проєктів",
    description:
      "Web Shestakov — студія Андрія Шестакова у Вроцлаві: сайти від $300, магазини від $800, Telegram-боти. 12+ років досвіду, 35+ проєктів у 6 країнах, договір і faktura.",
    ogType: "website",
    priority: 0.7
  },
  {
    group: "about",
    lang: "pl",
    path: "/pl/o-nas/",
    template: "about",
    title: "O nas — Web Shestakov, studio stron internetowych we Wrocławiu: 12+ lat doświadczenia",
    description:
      "Web Shestakov to studio Andrija Szestakowa we Wrocławiu: strony od $300, sklepy od $800, boty Telegram. 12+ lat doświadczenia, 35+ projektów w 6 krajach, umowa i faktura.",
    ogType: "website",
    priority: 0.7
  },
  {
    group: "privacy",
    lang: "uk",
    path: "/privacy/",
    template: "privacy",
    title: "Політика конфіденційності — Web Shestakov",
    description:
      "Політика конфіденційності та файлів cookies сайту shstkv-digital.com: цілі обробки даних, правові підстави, права користувача та керування згодою.",
    ogType: "article",
    priority: 0.3
  },
  {
    group: "privacy",
    lang: "pl",
    path: "/pl/polityka-prywatnosci/",
    template: "privacy",
    title: "Polityka prywatności — Web Shestakov",
    description:
      "Polityka prywatności i plików cookies serwisu shstkv-digital.com: cele przetwarzania danych, podstawy prawne, prawa użytkownika i zarządzanie zgodą.",
    ogType: "article",
    priority: 0.3
  }
];

export function page(group, lang) {
  return PAGES.find((p) => p.group === group && p.lang === lang);
}

export function alternates(group) {
  return PAGES.filter((p) => p.group === group);
}

/* Внутрішнє посилання на групу сторінок у потрібній мові
   (якщо перекладу немає — українська версія). */
export function href(group, lang) {
  const p = page(group, lang) || page(group, DEFAULT_LANG);
  return p ? p.path : "/";
}
