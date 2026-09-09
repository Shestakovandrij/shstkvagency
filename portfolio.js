/* ==========================================================================
   Портфоліо — самостійний скрипт сторінки.
   Нічого не імпортує з script.js головного сайту.

     1. Прелоадер   — лінія прогресу → світла сцена з лічильником → зсув угору
     2. Інтро       — колаж медіа і словесний знак першого екрана
     3. Меню        — фулскрін-панель
     4. Таби        — фільтр категорій і пагінація по шість кейсів
     5. Розкриття   — GSAP + ScrollTrigger, із запасним IntersectionObserver
     6. Курсор      — кружечок "Перейти" над картками (тільки миша)
     7. Глобус      — SMIL-порт lottie-іконки шаблону

   Анімуються виключно transform та opacity.
   ========================================================================== */

(function () {
  "use strict";

  var root = document.documentElement;
  var body = document.body;

  var REDUCE = false;
  try {
    REDUCE = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) {}

  var SKIP = root.classList.contains("pre-skip");
  var EASE = "cubic-bezier(0.16,1,0.3,1)";

  /* ------------------------------------------------------------------ *
   * 1. ПРЕЛОАДЕР
   * ------------------------------------------------------------------ */

  var MIN_MS = 1100;   // не коротше — навіть із кешу
  var MAX_MS = 2400;   // не довше — навіть на повільному з'єднанні

  function preloaderDone(pre) {
    if (window.__preDone) return;
    window.__preDone = true;
    pre.classList.add("is-done");
    body.classList.remove("is-preloading");
    if (typeof window.__introStart === "function") window.__introStart();
    if (window.ScrollTrigger && window.ScrollTrigger.refresh) window.ScrollTrigger.refresh();
  }

  /* Реальний прогрес: скільки власних скриншотів прелоадера вже декодовано. */
  function trackAssets(images, onProgress) {
    var total = images.length || 1;
    var done = 0;
    function tick() {
      done++;
      onProgress(Math.min(1, done / total));
    }
    images.forEach(function (img) {
      if (img.complete && img.naturalWidth > 0) { tick(); return; }
      img.addEventListener("load", tick, { once: true });
      img.addEventListener("error", tick, { once: true });
    });
    onProgress(Math.min(1, done / total));
  }

  function initPreloader() {
    var pre = document.getElementById("preloader");
    if (!pre) return;

    if (SKIP || REDUCE) { preloaderDone(pre); return; }

    var scene = pre.querySelector("[data-pl-scene]");
    var cover = pre.querySelector("[data-pl-cover]");
    var line = pre.querySelector("[data-pl-line]");
    var logo = pre.querySelector("[data-pl-logo]");
    var fades = pre.querySelectorAll("[data-pl-fade]");
    var count = pre.querySelector("[data-pl-count]");

    var started = Date.now();
    var assetRatio = 0;
    var shown = 0;
    var raf = 0;
    var uncovered = false;

    /* Смуга рахує саме ті кадри, які потрібні першому екрану. */
    trackAssets(
      Array.prototype.slice.call(document.querySelectorAll(".hero-media__item")),
      function (r) { assetRatio = r; }
    );

    var gsap = window.gsap;

    if (gsap) {
      gsap.set(logo, { yPercent: 120, opacity: 0 });
      gsap.set(fades, { opacity: 0, y: 10 });
    }

    /* Етап B: чорне полотно піднімається, сцена оживає. */
    function uncover() {
      if (uncovered) return;
      uncovered = true;

      if (!gsap) {
        cover.style.transition = "transform 0.8s " + EASE;
        cover.style.transform = "translateY(-100%)";
        return;
      }

      gsap.timeline()
        .to(cover, { yPercent: -100, duration: 0.9, ease: "expo.inOut" }, 0)
        .to(logo, { yPercent: 0, opacity: 1, duration: 0.7, ease: "power3.out" }, 0.25)
        .to(fades, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out", stagger: 0.06 }, 0.3);
    }

    /* Етап C: вся сцена їде вгору, відкриваючи сторінку. */
    function exit() {
      if (window.__preExiting) return;
      window.__preExiting = true;

      /* Перший екран стартує вже під сценою, що їде вгору — так шаблонна
         послідовність починається без паузи після прелоадера. */
      if (typeof window.__introStart === "function") window.__introStart();

      if (!gsap) {
        pre.style.transition = "opacity 0.5s " + EASE;
        pre.style.opacity = "0";
        window.setTimeout(function () { preloaderDone(pre); }, 520);
        return;
      }

      gsap.timeline({ onComplete: function () { preloaderDone(pre); } })
        .to(scene, { yPercent: -100, duration: 1.0, ease: "expo.inOut" }, 0);
    }

    function paint() {
      var elapsed = Date.now() - started;
      // Час тримає смугу живою, завантаження задає стелю.
      var byTime = Math.min(1, elapsed / (MIN_MS * 0.55));
      var target = Math.min(byTime, 0.15 + assetRatio * 0.85);
      if (elapsed >= MAX_MS) target = 1;

      shown += (target - shown) * 0.14;
      var pct = Math.round(Math.min(1, shown) * 100);
      if (line) line.style.transform = "scaleX(" + Math.min(1, shown).toFixed(4) + ")";
      if (count) count.textContent = pct < 100 ? ("00" + pct).slice(-3) : "100";

      if (!uncovered && (pct >= 99 || elapsed >= MAX_MS * 0.5)) {
        if (line) line.style.transform = "scaleX(1)";
        if (count) count.textContent = "100";
        uncover();
      }

      if (uncovered && (elapsed >= MIN_MS + 900 || elapsed >= MAX_MS)) {
        window.cancelAnimationFrame(raf);
        exit();
        return;
      }
      raf = window.requestAnimationFrame(paint);
    }

    raf = window.requestAnimationFrame(paint);
  }

  /* ------------------------------------------------------------------ *
   * 2. ІНТРО — послідовність шаблону, крок у крок
   *
   *    A. Шість кадрів колажу по черзі виринають із нуля: 0.70 / 1.10 /
   *       1.50 / 1.90 / 2.30 / 2.70 с, по секунді кожен, із перельотом.
   *    B. На 4.45 с уся сцена підіймається на 35vh і стискається до 0.75 —
   *       колаж іде за верхній край, лишаючи чистий екран.
   *    C. На 4.55 с словесний знак виходить із 8% на повну.
   *    D. Далі: параллакс кадрів за курсором і стиснення знака у слот
   *       навбара на скролі першого екрана.
   * ------------------------------------------------------------------ */

  /* Шаблон піднімає колаж на 35vh — там велетенський знак заввишки у
     пів екрана і колаж мусить піти за верхній край. Наш словесний знак
     удвічі нижчий, тож підйом менший: колаж лишається у верхніх двох
     третинах, як на референсі. */
  var HERO_LIFT_VH = -10;          // підйом колажу наприкінці послідовності
  var HERO_SHRINK = 0.85;          // і його кінцевий масштаб
  var POP = "back.out(1.3)";       // перельот, як у шаблоні
  var POP_AT = [0.7, 1.1, 1.5, 1.9, 2.3, 2.7];

  /* Зсув кожного кадру за курсором: [x, y] у відсотках власного розміру.
     У _2 по X постійний відступ — так само, як у шаблоні. */
  var DRIFT = [
    { x: 20, y: 20 },
    { x: 0, y: 15, offsetX: -15 },
    { x: 10, y: 10 },
    { x: 5, y: 5 },
    { x: 2, y: 2 },
    { x: 14, y: 12 }
  ];

  function initIntro() {
    var hero = document.querySelector(".intro-hero");
    if (!hero) return;

    var media = document.querySelector("[data-hero-media]");
    var items = media ? Array.prototype.slice.call(media.children) : [];
    var mark = hero.querySelector(".intro-hero__mark");
    var loc = hero.querySelector(".intro-hero__loc");
    var word = document.querySelector("[data-intro-word]");
    var gsap = window.gsap;
    var wide = false;
    try {
      wide = window.matchMedia("(min-width: 992px)").matches;
    } catch (e) {}
    var played = false;

    /* Вихідний стан ставимо до показу, щоб перший кадр не блимнув. */
    if (gsap && !REDUCE) {
      gsap.set(items, { scale: wide ? 0 : 1, transformOrigin: "50% 50%" });
      items.forEach(function (el, i) {
        var d = DRIFT[i];
        if (d && d.offsetX) gsap.set(el, { xPercent: d.offsetX });
      });
      if (word) gsap.set(word, { opacity: wide ? 0.08 : 1 });
    }

    function show() {
      if (played) return;
      played = true;

      if (!gsap || REDUCE) {
        items.forEach(function (el) { el.style.transform = "none"; });
        if (word) word.style.opacity = "1";
        return;
      }

      var tl = gsap.timeline();
      tl.from([mark, loc], {
        opacity: 0, y: -14, duration: 0.7, ease: "power3.out", stagger: 0.08
      }, 0);

      if (!wide) {
        tl.to(items, { scale: 1, duration: 0.9, ease: POP, stagger: 0.12 }, 0.25);
        return;
      }

      items.forEach(function (el, i) {
        tl.to(el, { scale: 1, duration: 1, ease: POP }, POP_AT[i] || 0.7 + i * 0.4);
      });

      if (media) {
        tl.to(media, {
          y: (HERO_LIFT_VH * window.innerHeight) / 100,
          duration: 1, ease: "power2.out"
        }, 4.45)
          .to(media, { scale: HERO_SHRINK, duration: 1, ease: "power2.inOut" }, 4.45);
      }
      if (word) tl.to(word, { opacity: 1, duration: 0.5, ease: "power1.inOut" }, 4.55);
    }

    if (window.__preDone) show(); else window.__introStart = show;
    // Навіть якщо прелоадер обірветься нештатно — перший екран не лишиться порожнім.
    window.setTimeout(show, MAX_MS + 1400);

    if (!gsap || REDUCE) return;

    /* --- Параллакс кадрів за курсором (тільки миша й широкий екран) --- */
    if (wide && items.length && window.matchMedia("(hover: hover)").matches) {
      var setters = items.map(function (el, i) {
        var d = DRIFT[i] || { x: 0, y: 0 };
        return {
          d: d,
          x: gsap.quickTo(el, "xPercent", { duration: 0.6, ease: "power2.out" }),
          y: gsap.quickTo(el, "yPercent", { duration: 0.6, ease: "power2.out" })
        };
      });

      hero.addEventListener("pointermove", function (e) {
        var r = hero.getBoundingClientRect();
        var nx = (e.clientX - r.left) / r.width * 2 - 1;   // -1 … 1
        var ny = (e.clientY - r.top) / r.height * 2 - 1;
        setters.forEach(function (s) {
          s.x((s.d.offsetX || 0) + nx * s.d.x);
          s.y(ny * s.d.y);
        });
      }, { passive: true });

      hero.addEventListener("pointerleave", function () {
        setters.forEach(function (s) { s.x(s.d.offsetX || 0); s.y(0); });
      }, { passive: true });
    }

    /* --- Словесний знак: із велетня внизу першого екрана у слот навбара.
           Замір робимо у натуральному стані, далі скрол скрабить дельту.
           Прозорість веде послідовність показу, тут її не чіпаємо. --- */
    if (!word || !window.ScrollTrigger) return;

    var tween = null;

    function layout() {
      if (tween) {
        if (tween.scrollTrigger) tween.scrollTrigger.kill();
        tween.kill();
        tween = null;
      }
      gsap.set(word, { clearProps: "transform" });

      var r = word.getBoundingClientRect();
      if (!r.width) return;

      var heroH = hero.getBoundingClientRect().height;
      var scale = (window.innerWidth * 0.965) / r.width;
      // низ велетня — за 2vh до низу першого екрана, як у шаблоні
      var giantCenterY = heroH * 0.977 - (r.height * scale) / 2;

      tween = gsap.fromTo(word,
        { y: giantCenterY - (r.top + r.height / 2), scale: scale },
        {
          y: 0, scale: 1, ease: "none",
          scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: 0.6 }
        });
    }

    layout();

    var resizeTimer = 0;
    window.addEventListener("resize", function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(layout, 200);
    });
  }

  /* ------------------------------------------------------------------ *
   * 3. ФУЛСКРІН-МЕНЮ
   * ------------------------------------------------------------------ */

  function initMenu() {
    var btn = document.getElementById("menu-btn");
    var menu = document.getElementById("nav-menu");
    if (!btn || !menu) return;

    function open() {
      body.classList.add("menu-open", "is-locked");
      btn.setAttribute("aria-expanded", "true");
      var first = menu.querySelector(".nav-menu__link");
      if (first) window.setTimeout(function () { first.focus(); }, 420);
    }
    function shut() {
      body.classList.remove("menu-open", "is-locked");
      btn.setAttribute("aria-expanded", "false");
    }

    btn.addEventListener("click", function () {
      if (body.classList.contains("menu-open")) shut(); else open();
    });

    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) shut();
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && body.classList.contains("menu-open")) {
        shut();
        btn.focus();
      }
    });
  }

  /* ------------------------------------------------------------------ *
   * 3b. НАВБАР НАД ПЕРШИМ ЕКРАНОМ
   *     Поки видно інтро, шапку несе сам екран: знак ліворуч, локація
   *     праворуч. Навбар проявляється, щойно екран пішов угору.
   * ------------------------------------------------------------------ */

  function initNavReveal() {
    var hero = document.querySelector(".intro-hero");
    if (!hero) return;

    var ticking = false;

    var darkPanel = document.querySelector(".contact__bg");
    var LINE = 56; // висота, на якій читається шапка

    function update() {
      var r = hero.getBoundingClientRect();
      body.classList.toggle("at-intro", r.bottom > 160);

      if (darkPanel) {
        var p = darkPanel.getBoundingClientRect();
        body.classList.toggle("nav-on-dark", p.top <= LINE && p.bottom >= LINE);
      }
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  /* ------------------------------------------------------------------ *
   * 4. ФІЛЬТР КАТЕГОРІЙ І ПАГІНАЦІЯ
   *    На сторінці — шість кейсів; решта ховається за номерами внизу
   *    списку. Зміна табу завжди повертає на першу сторінку.
   * ------------------------------------------------------------------ */

  var PAGE_SIZE = 6;

  function initFilter() {
    var list = document.getElementById("work-list");
    var empty = document.getElementById("work-empty");
    var shownEl = document.querySelector("[data-shown]");
    var totalEl = document.querySelector("[data-total]");
    var tabs = Array.prototype.slice.call(document.querySelectorAll(".tab"));
    if (!list || !tabs.length) return;

    var pager = document.getElementById("work-pager");
    var pageList = pager ? pager.querySelector("[data-page-list]") : null;
    var prevBtn = pager ? pager.querySelector("[data-page-prev]") : null;
    var nextBtn = pager ? pager.querySelector("[data-page-next]") : null;
    var status = pager ? pager.querySelector("[data-page-status]") : null;

    var cards = Array.prototype.slice.call(list.querySelectorAll(".case"));
    var filter = "all";
    var page = 1;
    var pages = 1;
    var first = true;

    function matches(card) {
      if (filter === "all") return true;
      return card.getAttribute("data-cat") === filter;
    }

    /* Картку, яку показує фільтр або нова сторінка, розкриваємо одразу:
       спостерігач розкриття міг її не побачити, поки вона була прихована. */
    function unveil(card) {
      card.style.opacity = "1";
      card.style.transform = "none";
    }

    function paintPager() {
      if (!pager) return;

      pager.hidden = pages < 2;
      if (pages < 2) { if (pageList) pageList.textContent = ""; return; }

      if (prevBtn) prevBtn.disabled = page === 1;
      if (nextBtn) nextBtn.disabled = page === pages;
      if (status) status.textContent = ("0" + page).slice(-2) + " / " + ("0" + pages).slice(-2);

      if (!pageList) return;
      pageList.textContent = "";
      for (var n = 1; n <= pages; n++) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "pager__num" + (n === page ? " is-active" : "");
        b.textContent = ("0" + n).slice(-2);
        b.setAttribute("aria-label", "Сторінка " + n);
        if (n === page) b.setAttribute("aria-current", "page");
        b.setAttribute("data-page", String(n));
        pageList.appendChild(b);
      }
    }

    function render() {
      var visible = cards.filter(matches);

      pages = Math.max(1, Math.ceil(visible.length / PAGE_SIZE));
      if (page > pages) page = pages;
      if (page < 1) page = 1;

      var from = (page - 1) * PAGE_SIZE;
      var to = from + PAGE_SIZE;

      cards.forEach(function (card) {
        card.classList.add("is-hidden");
        card.classList.remove("is-enter");
      });

      visible.forEach(function (card, i) {
        var num = card.querySelector(".case__num");
        if (num) num.textContent = "(" + ("0" + (i + 1)).slice(-2) + ")";
        if (i < from || i >= to) return;

        card.classList.remove("is-hidden");
        card.style.setProperty("--i", i - from);

        if (!first) {
          unveil(card);
          if (!REDUCE) {
            void card.offsetWidth; // reflow перезапускає анімацію входу
            card.classList.add("is-enter");
          }
        }
      });

      if (empty) empty.hidden = visible.length !== 0;
      if (shownEl) shownEl.textContent = Math.min(to, visible.length) - from;
      if (totalEl) totalEl.textContent = visible.length;

      paintPager();

      if (window.ScrollTrigger && window.ScrollTrigger.refresh) window.ScrollTrigger.refresh();
      first = false;
    }

    /* Нова сторінка має починатись від шапки списку, а не від його низу. */
    function scrollToList() {
      var bar = document.querySelector(".cms-work__bar");
      if (!bar) return;
      var top = window.pageYOffset + bar.getBoundingClientRect().top - 90;
      window.scrollTo({ top: Math.max(0, top), behavior: REDUCE ? "auto" : "smooth" });
    }

    function goto(next, scroll) {
      next = Math.min(Math.max(1, next), pages);
      if (next === page) return;
      page = next;
      render();
      if (scroll) scrollToList();
    }

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var next = tab.getAttribute("data-filter");
        if (next === filter) return;
        filter = next;
        page = 1;
        tabs.forEach(function (t) {
          t.classList.remove("is-active");
          t.setAttribute("aria-selected", "false");
        });
        tab.classList.add("is-active");
        tab.setAttribute("aria-selected", "true");
        render();
      });
    });

    if (pageList) {
      pageList.addEventListener("click", function (e) {
        var btn = e.target.closest("[data-page]");
        if (btn) goto(parseInt(btn.getAttribute("data-page"), 10), true);
      });
    }
    if (prevBtn) prevBtn.addEventListener("click", function () { goto(page - 1, true); });
    if (nextBtn) nextBtn.addEventListener("click", function () { goto(page + 1, true); });

    render();
  }

  /* ------------------------------------------------------------------ *
   * 5. РОЗКРИТТЯ ПРИ СКРОЛІ
   * ------------------------------------------------------------------ */

  function revealAllNow() {
    document.querySelectorAll("[data-reveal]").forEach(function (el) {
      el.style.opacity = "1";
      el.style.transform = "none";
    });
    document.querySelectorAll("[data-mask] > img").forEach(function (img) {
      img.style.transform = "none";
    });
  }

  function initRevealFallback() {
    if (!("IntersectionObserver" in window)) { revealAllNow(); return; }

    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        el.style.transition = "opacity 0.9s " + EASE + ", transform 0.9s " + EASE;
        el.style.opacity = "1";
        el.style.transform = "none";
        var img = el.matches("[data-mask]") ? el.querySelector("img") : el.querySelector("[data-mask] > img");
        if (img) {
          img.style.transition = "transform 1.2s " + EASE;
          img.style.transform = "none";
        }
        obs.unobserve(el);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

    document.querySelectorAll("[data-reveal], [data-mask]").forEach(function (el) { obs.observe(el); });
  }

  function initReveal() {
    if (REDUCE) { revealAllNow(); return; }

    body.classList.add("anim");

    if (!window.gsap || !window.ScrollTrigger) { initRevealFallback(); return; }

    var gsap = window.gsap;
    gsap.registerPlugin(window.ScrollTrigger);

    gsap.utils.toArray("[data-reveal]").forEach(function (el) {
      gsap.to(el, {
        opacity: 1, y: 0, duration: 1.1, ease: "expo.out",
        scrollTrigger: { trigger: el, start: "top 92%", once: true }
      });
    });

    gsap.utils.toArray("[data-mask]").forEach(function (wrap) {
      var img = wrap.querySelector("img");
      if (!img) return;
      gsap.to(img, {
        scale: 1, duration: 1.4, ease: "expo.out",
        scrollTrigger: { trigger: wrap, start: "top 95%", once: true }
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * 6. КОНТАКТНА КАРТКА
   *    Повтор поведінки шаблону: тло панелі входить у кадр із 120% до 100%,
   *    портрет нахиляється за мишею в перспективі (rotateY ±30, rotateZ ±10,
   *    rotateX ±10), сама картка й відблиск усередині неї їдуть паралаксом,
   *    а на наведення заголовок гасне до 25%, картка виходить на повну.
   * ------------------------------------------------------------------ */

  function initContactCard() {
    var section = document.querySelector(".contact");
    var wrap = document.querySelector(".contact__wrapper");
    if (!section || !wrap) return;

    /* Тло: 120% → 100% за час входу секції в кадр */
    var bg = section.querySelector(".contact__bg");
    if (bg && !REDUCE && window.gsap && window.ScrollTrigger) {
      window.gsap.fromTo(bg, { scale: 1.2 }, {
        scale: 1, ease: "none",
        scrollTrigger: { trigger: section, start: "top bottom", end: "bottom bottom", scrub: true }
      });
    }

    var fig = wrap.querySelector(".contact__figure");
    if (!fig) return;

    var ratio = fig.querySelector(".contact__ratio");
    var frame = fig.querySelector(".contact__frame");
    var glow = fig.querySelector(".contact__glow-wrap");

    function activate() { wrap.classList.add("is-active"); }
    function release() { wrap.classList.remove("is-active"); }

    fig.addEventListener("pointerenter", activate);
    fig.addEventListener("pointerleave", release);
    fig.addEventListener("focus", activate);
    fig.addEventListener("blur", release);

    var fine = false;
    try { fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
    if (!fine || REDUCE || !ratio || !frame || !glow) return;

    /* Ціль 0..1 у межах зони контакту; 0.5/0.5 — стан спокою */
    var tx = 0.5, ty = 0.5, cx = 0.5, cy = 0.5, raf = 0;

    function paint() {
      cx += (tx - cx) * 0.06;
      cy += (ty - cy) * 0.06;

      ratio.style.transform =
        "rotateX(" + (10 - cy * 20).toFixed(2) + "deg)" +
        "rotateY(" + (cx * 60 - 30).toFixed(2) + "deg)" +
        "rotateZ(" + (cx * 20 - 10).toFixed(2) + "deg)";
      frame.style.transform = "translate(" + (cx * 100 - 50).toFixed(2) + "%," + (cy * 34 - 17).toFixed(2) + "%)";
      glow.style.transform = "translate(" + (cx * 100 - 50).toFixed(2) + "%," + (cy * 100 - 50).toFixed(2) + "%)";

      if (Math.abs(tx - cx) > 0.0004 || Math.abs(ty - cy) > 0.0004) {
        raf = window.requestAnimationFrame(paint);
      } else {
        raf = 0;
      }
    }

    function kick() { if (!raf) raf = window.requestAnimationFrame(paint); }

    fig.addEventListener("pointermove", function (e) {
      var r = fig.getBoundingClientRect();
      if (!r.width || !r.height) return;
      tx = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width));
      ty = Math.min(1, Math.max(0, (e.clientY - r.top) / r.height));
      kick();
    }, { passive: true });

    fig.addEventListener("pointerleave", function () { tx = 0.5; ty = 0.5; kick(); });

    paint();
  }

  /* ------------------------------------------------------------------ *
   * 7. МАГНІТНІ ПОСИЛАННЯ
   *    Текст усередині посилання тягнеться за курсором: ±25% по X,
   *    ±50% по Y власного розміру — як у шаблоні.
   * ------------------------------------------------------------------ */

  function initMagnetic() {
    var items = Array.prototype.slice.call(document.querySelectorAll(".magnetic"));
    if (!items.length || REDUCE) return;

    var fine = false;
    try { fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
    if (!fine) return;

    items.forEach(function (item) {
      var host = item.parentNode;
      var tx = 0, ty = 0, cx = 0, cy = 0, raf = 0;

      function paint() {
        cx += (tx - cx) * 0.18;
        cy += (ty - cy) * 0.18;
        item.style.transform = "translate(" + cx.toFixed(2) + "%," + cy.toFixed(2) + "%)";
        if (Math.abs(tx - cx) > 0.05 || Math.abs(ty - cy) > 0.05) {
          raf = window.requestAnimationFrame(paint);
        } else {
          raf = 0;
        }
      }
      function kick() { if (!raf) raf = window.requestAnimationFrame(paint); }

      host.addEventListener("pointermove", function (e) {
        var r = host.getBoundingClientRect();
        if (!r.width || !r.height) return;
        tx = ((e.clientX - r.left) / r.width) * 50 - 25;
        ty = ((e.clientY - r.top) / r.height) * 100 - 50;
        kick();
      }, { passive: true });

      host.addEventListener("pointerleave", function () { tx = 0; ty = 0; kick(); });
    });
  }

  /* ------------------------------------------------------------------ *
   * 8. КУРСОР "ПЕРЕЙТИ"
   * ------------------------------------------------------------------ */

  function initCursor() {
    var dot = document.getElementById("cursor");
    if (!dot) return;

    var fine = false;
    try { fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches; } catch (e) {}
    if (!fine || REDUCE) { dot.remove(); return; }

    /* Підпис береться з data-cursor елемента; порожнє значення — типовий текст */
    var LABEL = (dot.textContent || "").trim() || "Перейти";
    var x = 0, y = 0, cx = 0, cy = 0, s = 0.4, on = false, raf = 0;

    function loop() {
      cx += (x - cx) * 0.18;
      cy += (y - cy) * 0.18;
      s += ((on ? 1 : 0.4) - s) * 0.2;
      dot.style.transform =
        "translate3d(" + cx.toFixed(1) + "px," + cy.toFixed(1) + "px,0) scale(" + s.toFixed(3) + ")";
      raf = window.requestAnimationFrame(loop);
    }

    document.addEventListener("pointermove", function (e) {
      x = e.clientX;
      y = e.clientY;
      var host = e.target.closest("[data-cursor]");
      if (host) {
        var label = host.getAttribute("data-cursor") || LABEL;
        if (dot.textContent !== label) dot.textContent = label;
      }
      var over = !!host;
      if (over !== on) {
        on = over;
        dot.classList.toggle("is-on", on);
      }
      if (!raf) { cx = x; cy = y; raf = window.requestAnimationFrame(loop); }
    }, { passive: true });

    document.addEventListener("pointerleave", function () {
      on = false;
      dot.classList.remove("is-on");
    });
  }

  /* ------------------------------------------------------------------ *
   * 8b. ГЛОБУС
   *     Меридіани крутить SMIL — CSS його не вимикає, тож режим
   *     зменшеного руху зупиняємо вручну, на першому кадрі.
   * ------------------------------------------------------------------ */

  function initGlobe() {
    if (!REDUCE) return;
    document.querySelectorAll("[data-globe]").forEach(function (svg) {
      if (typeof svg.pauseAnimations === "function") {
        svg.setCurrentTime(0);
        svg.pauseAnimations();
      }
    });
  }

  /* ------------------------------------------------------------------ *
   * 9. Запасний варіант для розбитого скриншота
   * ------------------------------------------------------------------ */

  function initMediaFallback() {
    document.querySelectorAll(".case__media img, .side__photo img").forEach(function (img) {
      function fail() {
        var media = img.parentNode;
        if (!media || media.querySelector(".case__fallback")) return;
        img.style.display = "none";
        var span = document.createElement("span");
        span.className = "case__fallback";
        span.textContent = (img.getAttribute("alt") || "Web Shestakov").split(" — ")[0];
        media.appendChild(span);
      }
      if (img.complete && img.naturalWidth === 0) { fail(); return; }
      img.addEventListener("error", fail);
    });
  }

  /* ------------------------------------------------------------------ *
   * старт
   * ------------------------------------------------------------------ */

  function boot() {
    var steps = [initPreloader, initIntro, initMenu, initNavReveal, initFilter, initReveal,
                 initContactCard, initMagnetic, initCursor, initGlobe, initMediaFallback];
    for (var i = 0; i < steps.length; i++) {
      try { steps[i](); } catch (e) {
        if (window.console) console.error("[pf] крок не виконано:", e);
      }
    }
    // Що б не сталося вище — сторінка не має лишитись прихованою.
    window.setTimeout(function () {
      var pre = document.getElementById("preloader");
      if (pre && !window.__preDone) preloaderDone(pre);
    }, MAX_MS + 1200);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
