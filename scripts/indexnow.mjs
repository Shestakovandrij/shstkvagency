/* Повідомляє Bing/Yandex (IndexNow) про всі URL із sitemap.
   Запуск після деплою: node scripts/indexnow.mjs */
const KEY = "343d04767e1f03f34a94a5438d0e8894";
const HOST = "www.shstkv-digital.com";
const xml = await (await fetch("https://" + HOST + "/sitemap.xml")).text();
const urlList = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const res = await fetch("https://api.indexnow.org/indexnow", {
  method: "POST",
  headers: { "Content-Type": "application/json; charset=utf-8" },
  body: JSON.stringify({ host: HOST, key: KEY, keyLocation: "https://" + HOST + "/" + KEY + ".txt", urlList })
});
console.log("IndexNow:", res.status, urlList.length, "URL");
