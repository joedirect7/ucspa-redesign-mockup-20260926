(function () {
  var root = document.querySelector(".hero-media--dissolve");
  if (!root) return;
  var slides = Array.prototype.slice.call(root.querySelectorAll(".hero-slide"));
  if (slides.length < 2) return;

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var i = 0;
  var timer = null;
  var INTERVAL = parseInt(root.getAttribute("data-interval") || "7000", 10);
  if (isNaN(INTERVAL) || INTERVAL < 3000) INTERVAL = 7000;

  var labelEl = document.querySelector("[data-hero-label]");
  var dots = Array.prototype.slice.call(document.querySelectorAll("[data-hero-dot]"));

  function show(n) {
    i = (n + slides.length) % slides.length;
    slides.forEach(function (s, idx) {
      s.classList.toggle("is-active", idx === i);
    });
    var label = slides[i].getAttribute("data-label") || "";
    if (labelEl) labelEl.textContent = label;
    dots.forEach(function (d, idx) {
      var on = idx === i;
      d.classList.toggle("is-active", on);
      d.setAttribute("aria-current", on ? "true" : "false");
    });
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
})();
