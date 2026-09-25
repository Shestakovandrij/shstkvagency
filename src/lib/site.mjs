import { readFileSync } from "node:fs";
import { join } from "node:path";

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
    title: "Розробка сайтів під ключ від €300 — Україна та Польща | Web Shestakov",
    description:
      "Лендінги, корпоративні сайти, інтернет-магазини та Telegram-боти під ключ від €300. Запуск від 3 днів, 30+ проєктів для бізнесу в Польщі, Україні та ЄС. Безкоштовна консультація.",
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
    crumb: "Портфоліо",
    template: "portfolio",
    title: "Портфоліо: сайти та інтернет-магазини, які ми створили | Web Shestakov",
    description:
      "Кейси Web Shestakov: лендінги, корпоративні сайти та інтернет-магазини для бізнесу в Польщі, Україні, Німеччині, Чехії та Нідерландах.",
    priority: 0.8
  },
  {
    group: "portfolio",
    lang: "pl",
    path: "/pl/realizacje/",
    crumb: "Portfolio",
    template: "portfolio-pl",
    title: "Portfolio — strony i sklepy internetowe dla firm | Web Shestakov",
    description:
      "Realizacje Web Shestakov: landing page, strony firmowe i sklepy internetowe dla firm w Polsce, Ukrainie, Niemczech, Czechach i Holandii.",
    priority: 0.8
  },
  {
    group: "about",
    lang: "uk",
    path: "/pro-nas/",
    crumb: "Про нас",
    template: "about",
    title: "Про нас — SHSTKV Digital, веб-студія у Вроцлаві, 12+ років досвіду",
    description:
      "SHSTKV Digital — студія Андрія Шестакова у Вроцлаві: сайти від €300, магазини від €800, Telegram-боти. 12+ років досвіду, 35+ проєктів у 6 країнах, договір і faktura.",
    ogType: "website",
    priority: 0.7
  },
  {
    group: "about",
    lang: "pl",
    path: "/pl/o-nas/",
    crumb: "O nas",
    template: "about",
    title: "O nas — SHSTKV Digital, studio stron www we Wrocławiu",
    description:
      "SHSTKV Digital to studio Andrija Szestakowa we Wrocławiu: strony od 300 €, sklepy od 800 €, boty Telegram. 12+ lat doświadczenia, 35+ projektów, umowa i faktura.",
    ogType: "website",
    priority: 0.7
  },
  {
    group: "privacy",
    lang: "uk",
    path: "/privacy/",
    crumb: "Політика конфіденційності",
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
    crumb: "Polityka prywatności",
    template: "privacy",
    title: "Polityka prywatności — Web Shestakov",
    description:
      "Polityka prywatności i plików cookies serwisu shstkv-digital.com: cele przetwarzania danych, podstawy prawne, prawa użytkownika i zarządzanie zgodą.",
    ogType: "article",
    priority: 0.3
  }
];

/* Сторінки кейсів: генерує scripts/build_cases.py (src/lib/cases.json). */
let BLOG = { posts: [] };
try { BLOG = JSON.parse(readFileSync(join(process.cwd(), "src", "lib", "blog.json"), "utf8")); } catch (e) {}
if (BLOG.posts.length) {
  PAGES.push(
    { group: "blog", lang: "uk", path: "/blog/", template: "blog", crumb: "Блог", title: "Блог про створення сайтів, SEO і продажі онлайн | SHSTKV Digital", description: "Практичні статті від веб-студії SHSTKV Digital: скільки коштує сайт, яку платформу обрати, чому сайту немає в Google. Досвід 35+ проєктів.", priority: 0.7 },
    { group: "blog", lang: "pl", path: "/pl/blog/", template: "blog", crumb: "Blog", title: "Blog o tworzeniu stron internetowych i SEO | SHSTKV Digital", description: "Praktyczne artykuły studia SHSTKV Digital: ile kosztuje strona, jaką platformę wybrać, dlaczego strony nie ma w Google. Doświadczenie z 35+ projektów.", priority: 0.7 }
  );
  for (const b of BLOG.posts) {
    const post = { date: b.date, modified: b.modified, img: b.img };
    PAGES.push(
      { group: "post-" + b.key, lang: "uk", path: b.path_uk, template: "post-" + b.key, crumb: b.h1_uk, post, ogType: "article", title: b.title_uk, description: b.desc_uk, priority: 0.6 },
      { group: "post-" + b.key, lang: "pl", path: b.path_pl, template: "post-" + b.key, crumb: b.h1_pl, post, ogType: "article", title: b.title_pl, description: b.desc_pl, priority: 0.6 }
    );
  }
}

const SVC = JSON.parse(readFileSync(join(process.cwd(), "src", "lib", "services.json"), "utf8"));
for (const v of SVC.services) {
  PAGES.push(
    { group: "svc-" + v.key, lang: "uk", path: v.path_uk, template: "svc-" + v.key, crumb: v.name_uk, service: v, title: v.title_uk, description: v.desc_uk, priority: 0.9 },
    { group: "svc-" + v.key, lang: "pl", path: v.path_pl, template: "svc-" + v.key, crumb: v.name_pl, service: v, title: v.title_pl, description: v.desc_pl, priority: 0.9 }
  );
}
for (const c of SVC.cities || []) {
  PAGES.push({ group: "city-" + c.key, lang: "uk", path: c.path_uk, template: "city-" + c.key, crumb: c.name_uk, title: c.title_uk, description: c.desc_uk, priority: 0.8 });
  if (c.path_pl) PAGES.push({ group: "city-" + c.key, lang: "pl", path: c.path_pl, template: "city-" + c.key, crumb: c.name_pl, title: c.title_pl, description: c.desc_pl, priority: 0.8 });
}
PAGES.push(
  { group: "prices", lang: "uk", path: "/tsiny/", template: "prices", crumb: "Ціни", title: SVC.prices.title_uk, description: SVC.prices.desc_uk, priority: 0.9 },
  { group: "prices", lang: "pl", path: "/pl/cennik/", template: "prices", crumb: "Cennik", title: SVC.prices.title_pl, description: SVC.prices.desc_pl, priority: 0.9 },
  { group: "contacts", lang: "uk", path: "/kontakty/", template: "contacts", crumb: "Контакти", title: SVC.contacts.title_uk, description: SVC.contacts.desc_uk, priority: 0.6 },
  { group: "contacts", lang: "pl", path: "/pl/kontakt/", template: "contacts", crumb: "Kontakt", title: SVC.contacts.title_pl, description: SVC.contacts.desc_pl, priority: 0.6 }
);

/* Нішеві сторінки: генерує scripts/build_niches.py (src/lib/niches.json). */
let NICHES = { niches: [] };
try { NICHES = JSON.parse(readFileSync(join(process.cwd(), "src", "lib", "niches.json"), "utf8")); } catch (e) {}
for (const n of NICHES.niches) {
  PAGES.push(
    { group: "niche-" + n.key, lang: "uk", path: n.path_uk, template: "niche-" + n.key, crumb: n.h1_uk, service: n, title: n.title_uk, description: n.desc_uk, priority: 0.8 },
    { group: "niche-" + n.key, lang: "pl", path: n.path_pl, template: "niche-" + n.key, crumb: n.h1_pl, service: n, title: n.title_pl, description: n.desc_pl, priority: 0.8 }
  );
}

const CASES = JSON.parse(readFileSync(join(process.cwd(), "src", "lib", "cases.json"), "utf8"));
for (const c of CASES) {
  PAGES.push(
    { group: "case-" + c.slug, lang: "uk", path: "/keisy/" + c.slug + "/", template: "case-" + c.slug, crumb: c.name, title: c.title_uk, description: c.desc_uk, ogType: "article", priority: 0.6 },
    { group: "case-" + c.slug, lang: "pl", path: "/pl/realizacje/" + c.slug + "/", template: "case-" + c.slug, crumb: c.name, title: c.title_pl, description: c.desc_pl, ogType: "article", priority: 0.6 }
  );
}

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
