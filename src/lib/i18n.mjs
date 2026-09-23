/* Словник перекладів береться з public/script.js — єдине джерело тексту,
   яке використовує і браузер (динамічні повідомлення форм), і збірка. */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import vm from "node:vm";

const SCRIPT = join(process.cwd(), "public", "script.js");

let cache;

export function dictionaries() {
  if (cache) return cache;
  const src = readFileSync(SCRIPT, "utf8");
  const start = src.indexOf("var I18N = {");
  const end = src.indexOf("\n  };\n", start);
  if (start < 0 || end < 0) throw new Error("I18N object not found in public/script.js");
  const literal = src.slice(start + "var I18N = ".length, end + 4);
  cache = vm.runInNewContext("(" + literal + ")");
  return cache;
}

export function t(lang, key) {
  const d = dictionaries();
  const dict = d[lang] || d.uk;
  return dict[key] != null ? dict[key] : d.uk[key] != null ? d.uk[key] : key;
}
