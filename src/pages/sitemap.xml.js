/* sitemap.xml з hreflang-зв'язками між мовними версіями. */
import { PAGES, SITE, DEFAULT_LANG, alternates, href } from "../lib/site.mjs";

export function GET() {
  const today = new Date().toISOString().slice(0, 10);
  const urls = PAGES.map((page) => {
    const alts = alternates(page.group);
    const links = alts.length > 1
      ? alts.map((a) => `    <xhtml:link rel="alternate" hreflang="${a.lang}" href="${SITE + a.path}"/>`)
          .concat(`    <xhtml:link rel="alternate" hreflang="x-default" href="${SITE + href(page.group, DEFAULT_LANG)}"/>`)
          .join("\n") + "\n"
      : "";
    return `  <url>\n    <loc>${SITE + page.path}</loc>\n${links}    <lastmod>${today}</lastmod>\n    <priority>${page.priority.toFixed(1)}</priority>\n  </url>`;
  });
  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n${urls.join("\n")}\n</urlset>\n`;
  return new Response(xml, { headers: { "Content-Type": "application/xml; charset=utf-8" } });
}
