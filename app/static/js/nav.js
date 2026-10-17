(() => {
  "use strict";
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.getElementById("nav-menu");
  if (!toggle || !menu) return;
  const groups = [...menu.querySelectorAll(".nav-group")];
  const setGroup = (g, open) => {
    g.classList.toggle("open", open);
    g.querySelector(".nav-group-btn").setAttribute("aria-expanded", String(open));
  };
  const closeGroups = except => groups.forEach(g => { if (g !== except) setGroup(g, false); });
  const closeAll = () => {
    closeGroups();
    menu.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
  };
  toggle.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  groups.forEach(g => {
    g.querySelector(".nav-group-btn").addEventListener("click", e => {
      e.stopPropagation();
      const open = !g.classList.contains("open");
      closeGroups(g);
      setGroup(g, open);
    });
  });
  menu.addEventListener("click", e => { if (e.target.closest("a")) closeAll(); });
  document.addEventListener("click", e => { if (!e.target.closest(".navbar")) closeAll(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") closeAll(); });
  window.matchMedia("(min-width: 901px)").addEventListener("change", closeAll);
})();