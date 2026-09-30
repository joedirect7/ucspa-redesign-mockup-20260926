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

  function show(n) {
    i = (n + slides.length) % slides.length;
    slides.forEach(function (s, idx) {
      s.classList.toggle("is-active", idx === i);
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

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop();
    else start();
  });

  start();
})();
