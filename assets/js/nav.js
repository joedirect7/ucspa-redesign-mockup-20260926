(function () {
  var toggle = document.querySelector(".nav-toggle");
  var panel = document.querySelector(".nav-mobile");
  if (!toggle || !panel) return;

  toggle.addEventListener("click", function () {
    var open = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!open));
    panel.classList.toggle("is-open", !open);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && panel.classList.contains("is-open")) {
      toggle.setAttribute("aria-expanded", "false");
      panel.classList.remove("is-open");
      toggle.focus();
    }
  });
})();
