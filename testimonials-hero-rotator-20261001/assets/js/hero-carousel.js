(function () {
  function init() {
    var root = document.querySelector(".hero-media--dissolve");
    if (!root) return;
    var slides = Array.prototype.slice.call(root.querySelectorAll(".hero-slide"));
    if (slides.length < 2) return;

    var i = 0;
    var INTERVAL = parseInt(root.getAttribute("data-interval") || "5500", 10);
    if (isNaN(INTERVAL) || INTERVAL < 2000) INTERVAL = 5500;

    var dots = Array.prototype.slice.call(document.querySelectorAll("[data-hero-dot]"));

    slides.forEach(function (s) {
      var img = s.querySelector("img");
      if (!img) return;
      img.loading = "eager";
      img.setAttribute("fetchpriority", "high");
      try {
        if (typeof img.decode === "function") img.decode().catch(function () {});
      } catch (e) {}
      if (!img.complete) {
        var warm = new Image();
        warm.src = img.currentSrc || img.src;
      }
    });

    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, idx) {
        s.classList.toggle("is-active", idx === i);
      });
      dots.forEach(function (d, idx) {
        d.classList.toggle("is-active", idx === i);
      });
      root.setAttribute("data-active", String(i));
    }

    function next() { show(i + 1); }

    show(0);

    // Joe lock: MUST auto-rotate. Do not gate on prefers-reduced-motion.
    // Dual drivers: setInterval + rAF watchdog (GH Pages / background tabs).
    var last = Date.now();
    window.setInterval(function () {
      next();
      last = Date.now();
    }, INTERVAL);

    function watchdog(now) {
      if (now - last >= INTERVAL + 400) {
        next();
        last = now;
      }
      window.requestAnimationFrame(watchdog);
    }
    window.requestAnimationFrame(watchdog);

    document.addEventListener("visibilitychange", function () {
      if (!document.hidden) last = Date.now();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
