(function () {
  function init() {
    var root = document.querySelector(".hero-media--dissolve");
    if (!root) return;
    var slides = Array.prototype.slice.call(root.querySelectorAll(".hero-slide"));
    if (slides.length < 2) return;

    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var i = 0;
    var timer = null;
    var INTERVAL = parseInt(root.getAttribute("data-interval") || "6000", 10);
    if (isNaN(INTERVAL) || INTERVAL < 2500) INTERVAL = 6000;

    var dots = Array.prototype.slice.call(document.querySelectorAll("[data-hero-dot]"));

    // Eager-decode all slide images so hidden slides are ready when they fade in
    slides.forEach(function (s) {
      var img = s.querySelector("img");
      if (!img) return;
      img.loading = "eager";
      img.setAttribute("fetchpriority", "high");
      try {
        if (typeof img.decode === "function") img.decode().catch(function () {});
      } catch (e) {}
      // Force network fetch even if currently opacity:0
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
        var on = idx === i;
        d.classList.toggle("is-active", on);
        d.setAttribute("aria-current", on ? "true" : "false");
      });
      root.setAttribute("data-active", String(i));
    }

    function next() { show(i + 1); }

    function start() {
      if (reduce) return;
      stop();
      timer = window.setInterval(next, INTERVAL);
    }

    function stop() {
      if (timer) {
        window.clearInterval(timer);
        timer = null;
      }
    }

    dots.forEach(function (d, idx) {
      d.addEventListener("click", function () {
        show(idx);
        start();
      });
    });

    document.addEventListener("visibilitychange", function () {
      if (document.hidden) stop();
      else start();
    });

    show(0);
    start();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
