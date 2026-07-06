/* ==========================================================================
   STKV Preloader — "Digital Signal Ignition"
   --------------------------------------------------------------------------
   Master GSAP timeline (full variant):
     scan      0.10 → 0.80   coral scanline sweeps, dots blink on its path
     assemble  0.55 → 1.20   fragments converge into the centre
     mark      0.85 → 1.50   monogram mask-reveal (bottom → top)
     wordmark  1.10 → 1.60   STKV wipe (left → right) + micro-flicker
     status    1.60 → 2.85   DESIGN / CODE / MOTION / LAUNCH roller
     ignition  2.70 → 3.10   scale pop + coral pulse rings
     exit      2.95 → 4.00   panel wipes up, logo flies to the header,
                             header + hero reveal underneath

   Where to tweak:
     - Timings/durations .......... the T object below (seconds)
     - Colors ..................... styles.css :root (--bg, --accent, --ink)
     - Logo size .................. --logo-h on .preloader in styles.css
     - Status words ............... .preloader__status-word spans in index.html
   Plays on every page load. Skip it: index.html?pre-skip
   Debug: freeze at a given second — index.html?pre-seek=1.2
   ========================================================================== */
(function () {
  "use strict";

  var pre = document.getElementById("preloader");
  if (!pre) return;

  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* --- Manual skip for debugging: index.html?pre-skip ---------------------- */
  if (document.documentElement.classList.contains("pre-skip")) {
    pre.classList.add("is-done");
    window.__preDone = true;
    return;
  }

  document.body.classList.add("is-preloading");

  var hero = document.querySelector(".hero > .container");
  var header = document.getElementById("header");
  var headerLogo = document.querySelector(".header__logo img");

  function finish() {
    pre.classList.add("is-done");
    document.body.classList.remove("is-preloading");
    window.__preDone = true; // disarms the inline head failsafe
  }

  /* --- Static path: reduced motion or GSAP failed to load ---------------- */
  function runStatic() {
    pre.classList.add("is-static"); // full logo, no scan/particles/status
    window.setTimeout(function () {
      pre.style.opacity = "0";
      window.setTimeout(finish, 550);
    }, reduced ? 700 : 900);
  }

  if (reduced || !window.gsap) { runStatic(); return; }

  var gsap = window.gsap;

  /* --- Decorative geometry (seeded PRNG — same layout every visit) ------- */
  function mulberry32(seed) {
    var a = seed | 0;
    return function () {
      a = (a + 0x6d2b79f5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  var rand = mulberry32(0x57534b56); // "WSKV"

  /* Dots that blink along the scanline path. data-t = position on the sweep. */
  var dotsHost = pre.querySelector("[data-pl-dots]");
  var dots = [];
  for (var i = 0; i < 11; i++) {
    var t = 0.06 + rand() * 0.88;
    var y = 14 + rand() * 72;
    var s = 2 + Math.round(rand() * 2);
    var dot = document.createElement("span");
    dot.className = "pl-dot";
    dot.dataset.t = String(t);
    dot.style.left = (t * 100) + "%";
    dot.style.top = y + "%";
    dot.style.width = s + "px";
    dot.style.height = s + "px";
    dotsHost.appendChild(dot);
    dots.push(dot);
  }

  /* Dots + line segments that converge into the brand mark. */
  var fragsHost = pre.querySelector("[data-pl-frags]");
  var frags = [];
  for (var j = 0; j < 14; j++) {
    var angle = rand() * Math.PI * 2;
    var dist = 120 + rand() * 180;
    var len = j % 3 === 0 ? 0 : Math.round(10 + rand() * 20); // 0 → dot
    var frag = document.createElement("span");
    frag.className = len === 0 ? "pl-frag-dot" : "pl-frag-seg";
    frag.dataset.dx = String(Math.round(Math.cos(angle) * dist * 1.4));
    frag.dataset.dy = String(Math.round(Math.sin(angle) * dist));
    frag.dataset.rot = String(Math.round(-35 + rand() * 70));
    if (len !== 0) frag.style.width = len + "px";
    fragsHost.appendChild(frag);
    frags.push(frag);
  }

  /* --- Timeline ----------------------------------------------------------- */
  var T = {
    scan: 0.1,
    scanDur: 0.7,
    assemble: 0.55,
    mark: 0.85,
    word: 1.1,
    flicker: 1.62,
    status: 1.6,
    statusStep: 0.34,
    ignite: 2.7,
    exit: 2.95
  };
  var EXIT_EASE = "power4.inOut";

  var panel = pre.querySelector("[data-pl-panel]");
  var brand = pre.querySelector("[data-pl-brand]");
  var lockup = pre.querySelector("[data-pl-lockup]");
  var markClip = pre.querySelector("[data-pl-mark-clip]");
  var wordClip = pre.querySelector("[data-pl-word-clip]");
  var grid = pre.querySelector("[data-pl-grid]");
  var scan = pre.querySelector("[data-pl-scan]");
  var edge = pre.querySelector("[data-pl-edge]");
  var status = pre.querySelector("[data-pl-status]");
  var statusInner = pre.querySelector("[data-pl-status-inner]");
  var rings = pre.querySelectorAll("[data-pl-ring]");

  /* Hero handoff start state (set before first frame to avoid a flash) */
  if (hero) gsap.set(hero, { y: 24, autoAlpha: 0, filter: "blur(8px)" });
  if (header) gsap.set(header, { autoAlpha: 0 });

  /* finish() is called by the exit timeline (built at runtime below) */
  var tl = gsap.timeline();

  /* 1 — texture breathes in */
  tl.to(grid, { opacity: 0.75, duration: 0.5, ease: "power1.out" }, 0.05);

  /* 2 — signal scan */
  tl.fromTo(
    scan,
    { x: "-4vw", opacity: 1 },
    { x: "104vw", duration: T.scanDur, ease: "power2.inOut" },
    T.scan
  ).set(scan, { opacity: 0 });

  /* dots blink exactly when the scanline passes them */
  dots.forEach(function (dot) {
    var at = T.scan + parseFloat(dot.dataset.t) * T.scanDur;
    tl.fromTo(
      dot,
      { opacity: 0, scale: 0.4 },
      { opacity: 0.9, scale: 1, duration: 0.1, ease: "power1.out" },
      Math.max(0, at - 0.05)
    ).to(dot, { opacity: 0, duration: 0.3, ease: "power1.in" }, at + 0.12);
  });

  /* 3 — fragments converge into the centre */
  frags.forEach(function (frag, idx) {
    var dx = parseFloat(frag.dataset.dx);
    var dy = parseFloat(frag.dataset.dy);
    var rot = parseFloat(frag.dataset.rot);
    var at = T.assemble + idx * 0.02;
    tl.fromTo(
      frag,
      { x: dx, y: dy, rotation: rot, opacity: 0 },
      { x: dx * 0.06, y: dy * 0.06, rotation: 0, opacity: 1, duration: 0.5, ease: "power3.in" },
      at
    ).to(frag, { opacity: 0, scale: 0.4, duration: 0.16 }, at + 0.5);
  });

  /* 4 — brand assembly: monogram wipes up, wordmark wipes right */
  tl.to(markClip, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.62, ease: "expo.out" }, T.mark)
    .fromTo(
      brand,
      { scale: 0.94, transformOrigin: "50% 50%" },
      { scale: 1, duration: 0.62, ease: "expo.out" },
      T.mark
    )
    .to(wordClip, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.5, ease: "power3.inOut" }, T.word);

  /* micro-flicker — one tasteful blink, then solid */
  tl.to(lockup, { opacity: 0.45, duration: 0.05, ease: "steps(1)" }, T.flicker)
    .to(lockup, { opacity: 1, duration: 0.05, ease: "steps(1)" })
    .to(lockup, { opacity: 0.75, duration: 0.04, ease: "steps(1)" })
    .to(lockup, { opacity: 1, duration: 0.04 });

  /* 5 — status roller: DESIGN / CODE / MOTION / LAUNCH */
  tl.fromTo(
    status,
    { opacity: 0, y: 8 },
    { opacity: 1, y: 0, duration: 0.3, ease: "power2.out" },
    T.status
  );
  for (var k = 1; k < 4; k++) {
    tl.to(statusInner, { yPercent: -25 * k, duration: 0.22, ease: "power3.inOut" }, T.status + T.statusStep * k);
  }

  /* 6 — ignition: pop + coral pulse rings */
  tl.to(brand, { scale: 1.05, duration: 0.16, ease: "power2.in" }, T.ignite)
    .to(brand, { scale: 1, duration: 0.4, ease: "back.out(2.2)" });

  rings.forEach(function (ring, idx) {
    tl.fromTo(
      ring,
      { scale: 0.25, opacity: 0.85 },
      { scale: 2.7, opacity: 0, duration: 0.75, ease: "expo.out", immediateRender: false },
      T.ignite + 0.1 + idx * 0.12
    );
  });

  tl.to(status, { opacity: 0, y: -6, duration: 0.25, ease: "power1.in" }, T.exit - 0.15)
    .to(grid, { opacity: 0, duration: 0.4 }, T.exit - 0.2);

  /* 7 — exit, built lazily so the header logo is measured against the
     current viewport (even after a resize during the intro) */
  function buildExit() {
    var exit = gsap.timeline({ onComplete: finish });

    // The overlay must never block interaction once it starts leaving.
    gsap.set(pre, { pointerEvents: "none" });

    // The brand lockup flies onto the header logo slot, then crossfades.
    var flies = false;
    if (brand && headerLogo) {
      var from = brand.getBoundingClientRect();
      var to = headerLogo.getBoundingClientRect();
      if (to.height > 0) {
        flies = true;
        exit.to(
          brand,
          {
            x: to.left - from.left,
            y: to.top - from.top,
            scale: to.height / from.height,
            transformOrigin: "left top",
            duration: 0.95,
            ease: EXIT_EASE
          },
          0
        );
      }
    }

    exit
      .to(panel, { clipPath: "inset(0% 0% 100% 0%)", duration: 0.95, ease: EXIT_EASE }, 0)
      .fromTo(
        edge,
        { y: 0, opacity: 1 },
        { y: function () { return -window.innerHeight; }, duration: 0.95, ease: EXIT_EASE },
        0
      )
      .to(edge, { opacity: 0, duration: 0.12 }, 0.86);

    /* Header + hero reveal underneath, as one connected move */
    if (header) exit.to(header, { autoAlpha: 1, duration: 0.7, ease: "power2.out" }, 0.55);
    if (hero) {
      exit.to(
        hero,
        { y: 0, autoAlpha: 1, filter: "blur(0px)", duration: 1, ease: "power3.out", clearProps: "filter,transform" },
        0.35
      );
    }

    /* Invisible swap: flown lockup ↔ real header logo (same geometry) */
    if (flies) exit.to(brand, { opacity: 0, duration: 0.12 }, 0.9);

    return exit;
  }

  tl.call(function () { buildExit(); }, [], T.exit);

  /* Debug hook: freeze the timeline at a given second — index.html?pre-seek=1.2 */
  var seek = /[?&]pre-seek=([\d.]+)/.exec(window.location.search);
  if (seek) tl.pause(parseFloat(seek[1]));
})();
