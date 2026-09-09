/* ============================================================================
   tracking.js — Meta Pixel + GA4 для shstkv-digital.com

   Що робить:
   1. Запам'ятовує, звідки прийшла людина (utm, fbclid, реферер) — на всю сесію.
   2. Вантажить піксель і GA4 тільки після згоди на куки ("accepted").
   3. Шле події: перегляд, скрол, які секції читали, кліки в Telegram/Instagram/
      телефон, відкриття форми, початок заповнення, зміна мови, час на сторінці.
   4. Дає глобальну функцію window.wsTrack(name, params) — нею стріляємо Lead
      з script.js після успішної відправки заявки.
   ========================================================================== */

(function () {
  "use strict";

  var META_ID     = "1374423121079785";
  var GA_ID       = "G-XXXXXXXXXX";      // ← підставити свій Measurement ID
  var CONSENT_KEY = "ws-cookie";          // "accepted" | "essential"
  var SOURCE_KEY  = "ws-src";

  var loaded = false;
  var queue  = [];

  /* ---------------------------------------------------------------- джерело */

  // Визначає, звідки людина прийшла. Запам'ятовує ПЕРШЕ джерело в сесії,
  // щоб перехід між сторінками не перезаписав його на "прямий".
  function captureSource() {
    var saved = null;
    try { saved = sessionStorage.getItem(SOURCE_KEY); } catch (e) {}
    if (saved) { try { return JSON.parse(saved); } catch (e) {} }

    var q = new URLSearchParams(window.location.search);
    var ref = document.referrer || "";
    var host = "";
    try { host = ref ? new URL(ref).hostname.replace(/^www\./, "") : ""; } catch (e) {}

    var src = q.get("utm_source") || "";
    var medium = q.get("utm_medium") || "";

    // Якщо міток немає — вгадуємо джерело за реферером і клік-айді
    if (!src) {
      if (q.get("fbclid")) { src = "meta"; medium = "paid"; }
      else if (q.get("gclid")) { src = "google"; medium = "paid"; }
      else if (/facebook|instagram/.test(host)) { src = host.split(".")[0]; medium = "social"; }
      else if (/t\.me|telegram/.test(host)) { src = "telegram"; medium = "messenger"; }
      else if (/google|bing|duckduckgo|yandex/.test(host)) { src = host.split(".")[0]; medium = "organic"; }
      else if (host) { src = host; medium = "referral"; }
      else { src = "direct"; medium = "none"; }
    }

    var data = {
      source: src,
      medium: medium,
      campaign: q.get("utm_campaign") || "",
      content: q.get("utm_content") || "",
      term: q.get("utm_term") || "",
      referrer: host,
      landing: window.location.pathname + window.location.hash
    };
    try { sessionStorage.setItem(SOURCE_KEY, JSON.stringify(data)); } catch (e) {}
    return data;
  }

  var SRC = captureSource();
  window.wsSource = SRC;

  /* ----------------------------------------------------------------- згода */

  function consent() {
    try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; }
  }

  /* ------------------------------------------------- завантаження скриптів */

  function loadMeta() {
    if (window.fbq) return;
    /* eslint-disable */
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    /* eslint-enable */
    window.fbq("init", META_ID);
  }

  function loadGA() {
    if (window.gtag || !GA_ID || GA_ID.indexOf("XXXX") > -1) return;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_ID, {
      campaign_source: SRC.source,
      campaign_medium: SRC.medium,
      campaign_name: SRC.campaign
    });
  }

  function boot() {
    if (loaded) return;
    if (consent() !== "accepted") return;
    loaded = true;
    loadMeta();
    loadGA();
    fire("PageView", {});
    while (queue.length) { var q = queue.shift(); fire(q[0], q[1]); }
  }

  /* ----------------------------------------------------------------- події */

  // Стандартні події Meta. Усе інше піде як trackCustom.
  var META_STANDARD = ["PageView", "ViewContent", "Lead", "Contact", "CompleteRegistration"];

  function fire(name, params) {
    params = params || {};
    params.src = SRC.source;
    params.med = SRC.medium;
    if (SRC.campaign) params.camp = SRC.campaign;

    try {
      if (window.fbq) {
        if (META_STANDARD.indexOf(name) > -1) window.fbq("track", name, params);
        else window.fbq("trackCustom", name, params);
      }
    } catch (e) {}

    try {
      if (window.gtag) {
        // GA4 любить snake_case: ViewContent -> view_content
        var gaName = name.replace(/([a-z0-9])([A-Z])/g, "$1_$2").toLowerCase();
        window.gtag("event", gaName, params);
      }
    } catch (e) {}
  }

  // Публічна функція — нею стріляємо Lead із script.js
  function track(name, params) {
    if (loaded) fire(name, params);
    else queue.push([name, params]);   // згоди ще нема — притримаємо
  }
  window.wsTrack = track;

  /* -------------------------------------------------------------- слухачі */

  function onConsentClick() {
    document.addEventListener("click", function (e) {
      var btn = e.target.closest && e.target.closest("[data-cookie]");
      if (btn) window.setTimeout(boot, 50);
    }, true);
  }

  // Глибина скролу: 25 / 50 / 75 / 100
  function initScroll() {
    var marks = [25, 50, 75, 100];
    var done = {};
    var tick = false;

    function check() {
      tick = false;
      var h = document.documentElement.scrollHeight - window.innerHeight;
      if (h <= 0) return;
      var pct = Math.round((window.scrollY / h) * 100);
      marks.forEach(function (m) {
        if (pct >= m && !done[m]) { done[m] = true; track("Scroll", { depth: m }); }
      });
    }

    window.addEventListener("scroll", function () {
      if (!tick) { tick = true; window.requestAnimationFrame(check); }
    }, { passive: true });
  }

  // Які секції людина реально доглянула (мінімум 40% блока у в'юпорті)
  function initSections() {
    if (!("IntersectionObserver" in window)) return;
    var seen = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var id = en.target.id;
        if (!id || seen[id]) return;
        seen[id] = true;
        // Портфоліо й тарифи — найважливіші, шлемо їх як ViewContent
        if (id === "cases" || id === "tariffs") track("ViewContent", { section: id });
        else track("SectionView", { section: id });
      });
    }, { threshold: 0.4 });

    document.querySelectorAll("section[id]").forEach(function (s) { io.observe(s); });
  }

  // Кліки в Telegram, Instagram, телефон
  function initContacts() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest("a[href]");
      if (!a) return;
      var href = a.getAttribute("href") || "";
      var ch = "";
      if (href.indexOf("t.me") > -1) ch = "telegram";
      else if (href.indexOf("instagram.com") > -1) ch = "instagram";
      else if (href.indexOf("tel:") === 0) ch = "phone";
      else if (href.indexOf("mailto:") === 0) ch = "email";
      if (ch) track("Contact", { channel: ch });
    }, true);
  }

  // Чи видно елемент. Попап на цьому сайті — position: fixed і ховається
  // через visibility, тож offsetParent тут не показник: у фіксованих
  // елементів він завжди null. Дивимось на обчислені стилі.
  function isVisible(el) {
    if (!el || el.hidden) return false;
    var cs;
    try { cs = window.getComputedStyle(el); } catch (e) { return false; }
    if (!cs) return false;
    return cs.display !== "none" && cs.visibility !== "hidden" && cs.opacity !== "0";
  }

  // Форма: відкриття попапа, початок заповнення
  function initForms() {
    var started = {};

    document.addEventListener("focusin", function (e) {
      var form = e.target.closest && e.target.closest(".form");
      if (!form) return;
      var id = form.id || "form";
      if (started[id]) return;
      started[id] = true;
      track("FormStart", { form_id: id });
    }, true);

    // Попап-форма: ловимо момент, коли її показали
    var popup = document.getElementById("popup-form");
    if (popup && "MutationObserver" in window) {
      var box = popup.closest(".popup, .modal, [hidden]") || popup.parentElement;
      if (box) {
        new MutationObserver(function () {
          if (isVisible(box) && !started._popup) {
            started._popup = true;
            track("FormOpen", { form_id: "popup-form" });
          }
        }).observe(box, { attributes: true, attributeFilter: ["hidden", "class", "style"] });
      }
    }
  }

  // Перемикання мови — видно, хто читає українською, а хто польською
  function initLang() {
    document.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("[data-lang]");
      if (b) track("LangSwitch", { lang: b.getAttribute("data-lang") });
    }, true);
  }

  // Час на сторінці: 30 і 60 секунд — відсіює випадкові заходи
  function initTime() {
    [30, 60].forEach(function (sec) {
      window.setTimeout(function () { track("TimeOnPage", { seconds: sec }); }, sec * 1000);
    });
  }

  /* ------------------------------------------------------------------ init */

  function init() {
    onConsentClick();
    boot();              // якщо згода вже була раніше — стартуємо одразу
    initScroll();
    initSections();
    initContacts();
    initForms();
    initLang();
    initTime();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
