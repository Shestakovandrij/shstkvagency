/* Збирає фінальний HTML сторінки з шаблону в src/templates:
     1. підставляє текст потрібної мови (та сама логіка, що applyLang у script.js);
     2. переписує <head>: title, description, canonical, hreflang, Open Graph, JSON-LD;
     3. робить відносні шляхи абсолютними і веде внутрішні посилання на мовні URL.
   Розмітка й класи шаблону не змінюються — вигляд сторінки лишається тим самим. */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { parseHTML } from "linkedom";
import { t } from "./i18n.mjs";
import { SITE, OG_LOCALE, DEFAULT_LANG, BUSINESS, alternates, href } from "./site.mjs";

const TEMPLATES = join(process.cwd(), "src", "templates");

/* Старі файли → група сторінок */
const LEGACY_LINKS = { "index.html": "home", "privacy.html": "privacy", "portfolio.html": "portfolio" };

function applyLang(document, lang) {
  document.documentElement.setAttribute("lang", lang);

  document.querySelectorAll("body [data-i18n]").forEach((el) => {
    const val = t(lang, el.getAttribute("data-i18n"));
    if (val.indexOf("<br") !== -1) el.innerHTML = val;
    else el.textContent = val;
  });

  document.querySelectorAll("body [data-i18n-attr]").forEach((el) => {
    el.getAttribute("data-i18n-attr").split(",").forEach((pair) => {
      const parts = pair.split(":");
      if (parts.length === 2) el.setAttribute(parts[0].trim(), t(lang, parts[1].trim()));
    });
  });

  // Юридичні тексти лежать у шаблоні обома мовами — лишаємо лише потрібну.
  document.querySelectorAll("[data-lang-block]").forEach((el) => {
    if (el.getAttribute("data-lang-block") !== lang) el.remove();
    else el.removeAttribute("hidden");
  });

  document.querySelectorAll(".lang__btn").forEach((btn) => {
    const active = btn.getAttribute("data-lang") === lang;
    btn.classList.toggle("is-active", active);
    btn.setAttribute("aria-pressed", active ? "true" : "false");
  });
}

function rewriteUrls(document, lang) {
  const isExternal = (u) => /^(?:[a-z][a-z0-9+.-]*:|\/\/|#|\/)/i.test(u);

  const fix = (value) => {
    if (!value || isExternal(value)) return value;
    const [file, hash] = value.split("#");
    if (LEGACY_LINKS[file] != null) return href(LEGACY_LINKS[file], lang) + (hash ? "#" + hash : "");
    if (/^(case-[a-z0-9-]+|svc-[a-z0-9-]+|about|prices|contacts)$/.test(file)) return href(file, lang) + (hash ? "#" + hash : "");
    return "/" + value.replace(/^\.\//, "");
  };

  for (const attr of ["src", "href", "poster", "data-src", "data-img"]) {
    document.querySelectorAll(`[${attr}]`).forEach((el) => {
      if (el.tagName === "LINK" && el.getAttribute("rel") === "alternate") return;
      el.setAttribute(attr, fix(el.getAttribute(attr)));
    });
  }
  document.querySelectorAll("[srcset]").forEach((el) => {
    const set = el.getAttribute("srcset").split(",").map((part) => {
      const [u, d] = part.trim().split(/\s+/);
      return fix(u) + (d ? " " + d : "");
    });
    el.setAttribute("srcset", set.join(", "));
  });
}

function jsonLd(page, document) {
  const org = {
    "@type": "ProfessionalService",
    "@id": SITE + "/#organization",
    name: BUSINESS.name,
    alternateName: ["SHSTKV Digital", "SHSTKV"],
    legalName: BUSINESS.legalName,
    url: SITE + "/",
    logo: SITE + "/assets/apple-touch-icon.png",
    image: SITE + "/assets/og-image.jpg",
    email: BUSINESS.email,
    telephone: BUSINESS.phone,
    vatID: BUSINESS.vatID,
    priceRange: "$$",
    address: { "@type": "PostalAddress", ...BUSINESS.address },
    areaServed: [
      { "@type": "Country", name: "Poland" },
      { "@type": "Country", name: "Ukraine" },
      { "@type": "Place", name: "European Union" },
      { "@type": "Country", name: "United States" }
    ],
    knowsLanguage: ["uk", "pl"],
    founder: { "@type": "Person", "@id": SITE + "/#founder", name: BUSINESS.founder, jobTitle: "Founder & CEO" },
    sameAs: BUSINESS.sameAs
  };

  const graph = [org];

  if (page.group === "home") {
    graph.push({
      "@type": "WebSite",
      "@id": SITE + "/#website",
      url: SITE + "/",
      name: BUSINESS.name,
      inLanguage: ["uk", "pl"],
      publisher: { "@id": SITE + "/#organization" }
    });

    // Послуги й тарифи — рівно те, що видно на сторінці.
    org.makesOffer = [1, 2].map((n) => {
      const price = document.querySelectorAll(".tariff__price")[n - 1];
      const amount = price ? price.textContent.replace(/[^0-9]/g, "") : null;
      return {
        "@type": "Offer",
        name: t(page.lang, `tariff.${n}.name`),
        ...(amount ? { price: amount, priceCurrency: "EUR" } : {}),
        itemOffered: { "@type": "Service", name: t(page.lang, "service.1.t") }
      };
    });

    const faq = [];
    for (let i = 1; i <= 20; i++) {
      const q = t(page.lang, `faq.${i}.q`);
      if (q === `faq.${i}.q`) break;
      faq.push({
        "@type": "Question",
        name: q,
        acceptedAnswer: { "@type": "Answer", text: t(page.lang, `faq.${i}.a`).replace(/<[^>]+>/g, " ") }
      });
    }
    if (faq.length) graph.push({ "@type": "FAQPage", "@id": SITE + page.path + "#faq", inLanguage: page.lang, mainEntity: faq });
  }

  graph.push({
    "@type": page.group === "about" ? "AboutPage" : "WebPage",
    "@id": SITE + page.path + "#webpage",
    url: SITE + page.path,
    name: page.title,
    description: page.description,
    inLanguage: page.lang,
    isPartOf: { "@id": SITE + "/#website" },
    about: { "@id": SITE + "/#organization" },
    ...(page.group !== "home" ? { breadcrumb: { "@id": SITE + page.path + "#breadcrumb" } } : {})
  });

  // Послуга з ціною «від» — рівно те, що видно в тарифах сторінки.
  if (page.service) {
    graph.push({
      "@type": "Service",
      "@id": SITE + page.path + "#service",
      name: page.crumb,
      serviceType: page.crumb,
      url: SITE + page.path,
      description: page.description,
      provider: { "@id": SITE + "/#organization" },
      areaServed: ["PL", "UA", "EU"].map((c) => (c === "EU" ? { "@type": "Place", name: "European Union" } : { "@type": "Country", name: c === "PL" ? "Poland" : "Ukraine" })),
      ...(page.service.price
        ? { offers: { "@type": "Offer", priceCurrency: "EUR", price: page.service.price, priceSpecification: { "@type": "PriceSpecification", minPrice: page.service.price, priceCurrency: "EUR" } } }
        : {})
    });
  }

  // FAQ на сторінках послуг, цін, контактів і «Про нас» — з розмітки сторінки.
  if (/^(svc-|prices$|contacts$|about$)/.test(page.group)) {
    const qa = [...document.querySelectorAll("#faq .faq__item")].map((it) => ({
      "@type": "Question",
      name: it.querySelector(".faq__q").textContent.replace(/^\s*\(\d+\)/, "").trim(),
      acceptedAnswer: { "@type": "Answer", text: it.querySelector(".faq__a").textContent.trim() }
    }));
    if (qa.length) graph.push({ "@type": "FAQPage", "@id": SITE + page.path + "#faq", inLanguage: page.lang, mainEntity: qa });
  }

  // Хлібні крихти: Головна → (Портфоліо для кейсів) → сторінка.
  if (page.group !== "home") {
    const home = page.lang === "pl" ? "Strona główna" : "Головна";
    const trail = [{ name: home, path: href("home", page.lang) }];
    if (page.group.startsWith("case-")) trail.push({ name: "Portfolio", path: href("portfolio", page.lang) });
    trail.push({ name: page.crumb || page.title, path: page.path });
    graph.push({
      "@type": "BreadcrumbList",
      "@id": SITE + page.path + "#breadcrumb",
      itemListElement: trail.map((c, i) => ({ "@type": "ListItem", position: i + 1, name: c.name, item: SITE + c.path }))
    });
  }

  return JSON.stringify({ "@context": "https://schema.org", "@graph": graph });
}

function rewriteHead(document, page) {
  const head = document.head;
  head
    .querySelectorAll('title, meta[name="description"], meta[name="robots"], link[rel="canonical"], meta[property^="og:"], meta[name^="twitter:"]')
    .forEach((el) => el.remove());
  head.querySelectorAll("[data-i18n]").forEach((el) => el.removeAttribute("data-i18n"));

  const url = SITE + page.path;
  const alts = alternates(page.group);
  const ogImage = SITE + "/assets/og-image.jpg";
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");

  const tags = [
    `<title>${esc(page.title)}</title>`,
    `<meta name="description" content="${esc(page.description)}" />`,
    `<meta name="robots" content="index, follow, max-image-preview:large" />`,
    `<link rel="canonical" href="${url}" />`,
    ...alts.map((a) => `<link rel="alternate" hreflang="${a.lang}" href="${SITE + a.path}" />`),
    ...(alts.length > 1 ? [`<link rel="alternate" hreflang="x-default" href="${SITE + href(page.group, DEFAULT_LANG)}" />`] : []),
    `<meta property="og:type" content="${page.ogType || "website"}" />`,
    `<meta property="og:site_name" content="${BUSINESS.name}" />`,
    `<meta property="og:url" content="${url}" />`,
    `<meta property="og:locale" content="${OG_LOCALE[page.lang]}" />`,
    ...alts.filter((a) => a.lang !== page.lang).map((a) => `<meta property="og:locale:alternate" content="${OG_LOCALE[a.lang]}" />`),
    `<meta property="og:title" content="${esc(page.title)}" />`,
    `<meta property="og:description" content="${esc(page.description)}" />`,
    `<meta property="og:image" content="${ogImage}" />`,
    `<meta property="og:image:type" content="image/jpeg" />`,
    `<meta property="og:image:width" content="1200" />`,
    `<meta property="og:image:height" content="630" />`,
    `<meta property="og:image:alt" content="${esc(page.title)}" />`,
    `<meta name="twitter:card" content="summary_large_image" />`,
    `<meta name="twitter:image" content="${ogImage}" />`,
    `<script type="application/ld+json">${jsonLd(page, document)}</script>`
  ];

  const anchor = head.querySelector('meta[name="viewport"]');
  const frag = document.createElement("template");
  frag.innerHTML = "\n  " + tags.join("\n  ");
  anchor.after(...frag.content.childNodes);
}

export function renderPage(page) {
  const source = readFileSync(join(TEMPLATES, page.template + ".html"), "utf8");
  const { document } = parseHTML(source);
  applyLang(document, page.lang);
  rewriteUrls(document, page.lang);
  rewriteHead(document, page);
  return "<!DOCTYPE html>\n" + document.documentElement.outerHTML + "\n";
}
