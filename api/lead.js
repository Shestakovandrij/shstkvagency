/* ==========================================================================
   /api/lead — приймає заявку з форми та надсилає її в Telegram.
   Токен і chat_id беруться з environment variables Vercel:
     TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
   ========================================================================== */

var SERVICES = {
  site: { uk: "Сайт", pl: "Strona internetowa", icon: "🌐" },
  shop: { uk: "Інтернет-магазин", pl: "Sklep internetowy", icon: "🛒" },
  bot: { uk: "Telegram-бот", pl: "Bot Telegram", icon: "🤖" },
  seo: { uk: "SEO", pl: "SEO", icon: "📈" },
  identity: { uk: "Айдентика", pl: "Identyfikacja wizualna", icon: "🎨" },
  other: { uk: "Інше", pl: "Inne", icon: "✨" }
};

var SOURCES = {
  "main-form": { uk: "Форма на сторінці", pl: "Formularz na stronie" },
  "popup-form": { uk: "Спливаюче вікно", pl: "Okno popup" }
};

function escapeHtml(value) {
  return String(value == null ? "" : value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function clean(value, limit) {
  var text = String(value == null ? "" : value).replace(/\s+/g, " ").trim();
  if (text.length > limit) text = text.slice(0, limit) + "…";
  return text;
}

function contactLink(raw) {
  var value = clean(raw, 120);
  var safe = escapeHtml(value);
  var handle = value.match(/^@([A-Za-z0-9_]{4,32})$/);
  if (handle) return '<a href="https://t.me/' + handle[1] + '">' + safe + "</a>";
  if (/^[+\d][\d\s()\-]{6,}$/.test(value)) return "<code>" + safe + "</code>";
  if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) return '<a href="mailto:' + safe + '">' + safe + "</a>";
  return safe;
}

function kyivStamp() {
  var now = new Date();
  var parts = new Intl.DateTimeFormat("uk-UA", {
    timeZone: "Europe/Kyiv",
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  }).format(now);
  return parts + " (Київ)";
}

function buildMessage(data) {
  var lang = data.lang === "pl" ? "pl" : "uk";
  var service = SERVICES[data.need] || null;
  var source = SOURCES[data.source] || null;

  var lines = [];
  lines.push("🔥 <b>НОВА ЗАЯВКА З САЙТУ</b>");
  lines.push("<i>shstkv.agency</i>");
  lines.push("");
  lines.push("👤 <b>Ім’я:</b> " + escapeHtml(clean(data.name, 120)));
  lines.push("📞 <b>Контакт:</b> " + contactLink(data.contact));

  if (service) {
    lines.push("🎯 <b>Послуга:</b> " + service.icon + " " + escapeHtml(service.uk));
  } else if (data.need) {
    lines.push("🎯 <b>Послуга:</b> " + escapeHtml(clean(data.need, 120)));
  }

  var comment = clean(data.comment, 2000);
  if (comment) {
    lines.push("");
    lines.push("💬 <b>Коментар:</b>");
    lines.push("<blockquote>" + escapeHtml(comment) + "</blockquote>");
  }

  lines.push("");
  lines.push("————————————");
  if (source) lines.push("📍 " + escapeHtml(source.uk));
  lines.push("🌐 Мова сайту: " + (lang === "pl" ? "PL 🇵🇱" : "UA 🇺🇦"));
  lines.push("🕒 " + kyivStamp());

  return lines.join("\n");
}

module.exports = async function handler(req, res) {
  if (req.method === "OPTIONS") {
    res.setHeader("Allow", "POST, OPTIONS");
    return res.status(204).end();
  }
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST, OPTIONS");
    return res.status(405).json({ ok: false, error: "method_not_allowed" });
  }

  var token = process.env.TELEGRAM_BOT_TOKEN;
  var chatId = process.env.TELEGRAM_CHAT_ID;
  if (!token || !chatId) {
    console.error("[lead] TELEGRAM_BOT_TOKEN або TELEGRAM_CHAT_ID не налаштовані");
    return res.status(500).json({ ok: false, error: "not_configured" });
  }

  var data = req.body;
  if (typeof data === "string") {
    try { data = JSON.parse(data); } catch (e) { data = null; }
  }
  if (!data || typeof data !== "object") {
    return res.status(400).json({ ok: false, error: "bad_request" });
  }

  // Honeypot: справжні відвідувачі це поле не бачать і не заповнюють.
  if (clean(data.company, 200)) {
    return res.status(200).json({ ok: true });
  }

  if (!clean(data.name, 120) || !clean(data.contact, 120)) {
    return res.status(400).json({ ok: false, error: "missing_fields" });
  }

  var payload = {
    chat_id: chatId,
    text: buildMessage(data),
    parse_mode: "HTML",
    disable_web_page_preview: true
  };

  try {
    var response = await fetch("https://api.telegram.org/bot" + token + "/sendMessage", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    var result = await response.json();
    if (!result.ok) {
      console.error("[lead] Telegram відхилив запит:", result.description);
      return res.status(502).json({ ok: false, error: "telegram_rejected" });
    }
    return res.status(200).json({ ok: true });
  } catch (error) {
    console.error("[lead] Помилка запиту до Telegram:", error);
    return res.status(502).json({ ok: false, error: "telegram_unreachable" });
  }
};
