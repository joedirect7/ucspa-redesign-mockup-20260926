(function () {
  var nodes = document.querySelectorAll(".reveal");
  if (!nodes.length) return;

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    nodes.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
  );

  nodes.forEach(function (el) { observer.observe(el); });
})();

(function () {
  var root = document.querySelector(".hero__media--rotator");
  if (!root) return;

  var slides = Array.prototype.slice.call(root.querySelectorAll(".hero-slide"));
  var dots = Array.prototype.slice.call(root.querySelectorAll(".hero-slide__dots button"));
  var chip = root.querySelector(".hero-slide__chip");
  if (slides.length < 2) return;

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var i = 0;
  var timer = null;
  var INTERVAL = 5500;

  function show(n) {
    i = (n + slides.length) % slides.length;
    slides.forEach(function (s, idx) {
      s.classList.toggle("is-active", idx === i);
    });
    dots.forEach(function (d, idx) {
      d.classList.toggle("is-active", idx === i);
    });
    if (chip) {
      var label = slides[i].getAttribute("data-label") || "";
      var href = slides[i].getAttribute("data-href") || "#";
      chip.textContent = label;
      chip.setAttribute("href", href);
    }
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

  root.addEventListener("mouseenter", stop);
  root.addEventListener("mouseleave", start);
  root.addEventListener("focusin", stop);
  root.addEventListener("focusout", start);

  show(0);
  start();
})();
