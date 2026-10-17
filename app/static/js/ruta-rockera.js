(() => {
  "use strict";

  const mapElement = document.getElementById("ruta-rockera-map");
  if (!mapElement) return;
  if (typeof L === "undefined") { console.error("Ruta Rockera: Leaflet no esta disponible."); return; }

  const LAYERS = {
    rock: { color: "#ff2e4d" },
    culture: { color: "#19e6ff" },
    history: { color: "#ffc400" }
  };
  const TYPES = {
    ROCK_BAR: { layer: "rock", label: "Bar de rock" },
    METAL_BAR: { layer: "rock", label: "Bar de metal" },
    LIVE_MUSIC_BAR: { layer: "rock", label: "M\u00fasica en vivo" },
    MUSEUM: { layer: "culture", label: "Museo" },
    CULTURAL_VENUE: { layer: "culture", label: "Escenario cultural" },
    HISTORICAL_SITE: { layer: "history", label: "Sitio hist\u00f3rico" }
  };
  const EVIDENCE = {
    VERIFIED_PRIMARY: "Verificado \u00b7 fuente primaria",
    VERIFIED_SECONDARY: "Verificado \u00b7 fuente secundaria",
    HISTORICAL_DOCUMENTED: "Hist\u00f3rico documentado",
    NOT_VERIFIED: "No verificado"
  };

  const $ = id => document.getElementById(id);
  const listEl = $("places-list"), countEl = $("places-count"), countLabelEl = $("places-count-label");
  const searchEl = $("search-place"), resetEl = $("reset-map"), statusEl = $("map-status");
  const typeChipsEl = $("type-chips"), cityChipsEl = $("city-chips"), heroCountEl = $("hero-count");
  const wrapEl = mapElement.parentElement;
  const stacked = window.matchMedia("(max-width: 900px)");

  const map = L.map(mapElement, { center: [6.2442, -75.5812], zoom: 12, scrollWheelZoom: false });
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '\u00a9 <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap</a> contributors'
  }).addTo(map);
  // En una pagina larga, la rueda solo hace zoom despues de un clic en el mapa.
  map.on("click", () => map.scrollWheelZoom.enable());
  mapElement.addEventListener("mouseleave", () => map.scrollWheelZoom.disable());
  if (typeof ResizeObserver !== "undefined") new ResizeObserver(() => map.invalidateSize()).observe(mapElement);

  const clusterIcon = cluster => L.divIcon({ className: "rq-cluster-wrap", html: '<span class="rq-cluster">' + cluster.getChildCount() + "</span>", iconSize: [38, 38] });
  const markersLayer = (typeof L.markerClusterGroup === "function"
    ? L.markerClusterGroup({ maxClusterRadius: 28, spiderfyOnMaxZoom: true, showCoverageOnHover: false, iconCreateFunction: clusterIcon })
    : L.layerGroup()).addTo(map);
  const markers = new Map(), cards = new Map();
  let allPlaces = [];
  const state = { layer: "", city: "", q: "" };

  const esc = v => String(v == null ? "" : v).replace(/[&<>"']/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
  const safeUrl = u => (/^https?:\/\//i.test(String(u || "")) ? String(u) : "");
  const norm = s => String(s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  const hasCoords = p => !!(p.coordinates && typeof p.coordinates.lat === "number" && typeof p.coordinates.lng === "number");
  const typeInfo = p => TYPES[p.type] || { layer: "rock", label: p.type ? String(p.type).replace(/_/g, " ").toLowerCase() : "Lugar" };
  const where = p => [p.city, p.neighborhood].filter(Boolean).join(" \u00b7 ");
  const routeUrl = p => "https://www.google.com/maps/dir/?api=1&destination=" + p.coordinates.lat + "," + p.coordinates.lng;
  const pinIcon = layer => L.divIcon({
    className: "rq-pin-wrap",
    html: '<span class="rq-pin" style="--c:' + LAYERS[layer].color + '"></span>',
    iconSize: [22, 22], iconAnchor: [11, 11], popupAnchor: [0, -12]
  });

  function popupHtml(p) {
    const info = typeInfo(p);
    const styles = Array.isArray(p.music_styles) ? p.music_styles.join(", ") : "";
    const links = (Array.isArray(p.sources) ? p.sources : [])
      .map(s => ({ u: safeUrl(s && s.url), n: (s && (s.name || s.title)) || "Fuente" }))
      .filter(s => s.u).slice(0, 5)
      .map(s => '<li><a href="' + esc(s.u) + '" target="_blank" rel="noopener noreferrer">' + esc(s.n) + "</a></li>").join("");
    const site = safeUrl(p.website);
    const ev = EVIDENCE[p.evidence_status] || (p.evidence_status ? String(p.evidence_status).replace(/_/g, " ") : "NO VERIFICADO");
    return '<div class="rr-popup" style="--c:' + LAYERS[info.layer].color + '">'
      + '<span class="rr-tag" style="--c:' + LAYERS[info.layer].color + '">' + esc(info.label) + "</span>"
      + "<h3>" + esc(p.name) + "</h3>"
      + '<p class="rr-popup-where">' + esc(where(p)) + "</p>"
      + (p.address ? "<p>" + esc(p.address) + "</p>" : "")
      + (p.description ? "<p>" + esc(p.description) + "</p>" : "")
      + (styles ? "<p><b>Estilos:</b> " + esc(styles) + "</p>" : "")
      + '<p class="rr-evidence">' + esc(ev) + "</p>"
      + '<p class="rr-popup-actions"><a class="rr-btn" href="' + esc(routeUrl(p)) + '" target="_blank" rel="noopener noreferrer">C\u00f3mo llegar</a>'
      + (site ? ' <a class="rr-btn ghost" href="' + esc(site) + '" target="_blank" rel="noopener noreferrer">Sitio web</a>' : "") + "</p>"
      + (links ? '<details class="rr-sources"><summary>Fuentes</summary><ul>' + links + "</ul></details>" : "")
      + "</div>";
  }

  function hot(key, on) {
    const m = markers.get(key), el = m && m.getElement && m.getElement();
    if (el) el.classList.toggle("rq-pin-hot", on);
  }

  function setActive(key, scrollCard) {
    cards.forEach((c, k) => c.classList.toggle("is-active", k === key));
    const c = cards.get(key);
    if (scrollCard && c && c.isConnected) listEl.scrollTo({ top: Math.max(0, c.offsetTop - 8), behavior: "smooth" });
  }

  function focusPlace(p) {
    const m = markers.get(p._k);
    if (!m) return;
    setActive(p._k, false);
    if (stacked.matches) wrapEl.scrollIntoView({ behavior: "smooth", block: "center" });
    let opened = false;
    const open = () => { if (opened) return; opened = true; if (typeof markersLayer.zoomToShowLayer === "function") { markersLayer.zoomToShowLayer(m, () => m.openPopup()); } else { m.openPopup(); } };
    map.once("moveend", open);
    setTimeout(open, 1000);
    map.flyTo(m.getLatLng(), Math.max(map.getZoom(), 15), { duration: 0.8 });
  }

  function build(places) {
    places.forEach((p, i) => {
      p._k = p.id || ("p" + i);
      const info = typeInfo(p);
      p._hay = norm([p.name, p.city, p.neighborhood, p.address, info.label].concat(p.music_styles || [], p.tags || []).filter(Boolean).join(" "));
      if (hasCoords(p)) {
        const m = L.marker([p.coordinates.lat, p.coordinates.lng], { icon: pinIcon(info.layer), riseOnHover: true });
        m.bindPopup(popupHtml(p), { maxWidth: 340 });
        m.bindTooltip(p.name, { direction: "top", offset: [0, -10], className: "rq-tip" });
        m.on("click", () => setActive(p._k, true));
        markers.set(p._k, m);
      }
      const card = document.createElement("article");
      card.className = "rr-card";
      card.dataset.layer = info.layer;
      card.tabIndex = 0;
      card.innerHTML = '<span class="rr-tag">' + esc(info.label) + "</span><h3>" + esc(p.name) + "</h3><p>" + esc(where(p)) + "</p>"
        + (hasCoords(p) ? '<div class="rr-actions"><a class="rr-btn" href="' + esc(routeUrl(p)) + '" target="_blank" rel="noopener noreferrer">C\u00f3mo llegar</a></div>' : "");
      card.addEventListener("click", e => { if (e.target.closest("a")) return; focusPlace(p); });
      card.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); focusPlace(p); } });
      card.addEventListener("mouseenter", () => hot(p._k, true));
      card.addEventListener("mouseleave", () => hot(p._k, false));
      cards.set(p._k, card);
    });
  }

  function buildCityChips() {
    const cities = [...new Set(allPlaces.map(p => p.city).filter(Boolean))].sort((a, b) => a.localeCompare(b, "es"));
    cityChipsEl.textContent = "";
    [""].concat(cities).forEach(c => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "rr-chip"; b.dataset.city = c; b.textContent = c || "Todos";
      cityChipsEl.appendChild(b);
    });
  }

  function updateCounts() {
    typeChipsEl.querySelectorAll(".rr-chip").forEach(b => {
      const layer = b.dataset.layer || "";
      const n = allPlaces.filter(p => !layer || typeInfo(p).layer === layer).length;
      const em = b.querySelector(".rr-n");
      if (em) em.textContent = "(" + n + ")";
    });
  }

  function syncChips() {
    typeChipsEl.querySelectorAll(".rr-chip").forEach(b => {
      const on = (b.dataset.layer || "") === state.layer;
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", String(on));
    });
    cityChipsEl.querySelectorAll(".rr-chip").forEach(b => {
      const on = (b.dataset.city || "") === state.city;
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", String(on));
    });
  }

  function matches(p) {
    if (state.layer && typeInfo(p).layer !== state.layer) return false;
    if (state.city && p.city !== state.city) return false;
    if (state.q && !p._hay.includes(norm(state.q))) return false;
    return true;
  }

  function fit(vis) {
    const pts = vis.filter(hasCoords).map(p => [p.coordinates.lat, p.coordinates.lng]);
    map.invalidateSize();
    if (!pts.length) return;
    if (pts.length === 1) map.setView(pts[0], 15);
    else map.fitBounds(L.latLngBounds(pts).pad(0.15), { maxZoom: 15 });
  }

  function render(refit) {
    const vis = allPlaces.filter(matches);
    markersLayer.clearLayers();
    listEl.textContent = "";
    vis.forEach(p => {
      const m = markers.get(p._k);
      if (m) markersLayer.addLayer(m);
      listEl.appendChild(cards.get(p._k));
    });
    if (!vis.length) {
      const e = document.createElement("p");
      e.className = "rr-empty";
      e.textContent = "Nada por aqu\u00ed. Prueba otro filtro / try another one.";
      listEl.appendChild(e);
    }
    countEl.textContent = vis.length;
    countLabelEl.textContent = vis.length === 1 ? "spot" : "spots";
    statusEl.textContent = vis.length + " de " + allPlaces.length + " lugares \u00b7 toca un pin o una tarjeta";
    syncChips(); if (resetEl) resetEl.hidden = !(state.layer || state.city || state.q); const cityNow = $("city-now"); if (cityNow) cityNow.textContent = state.city || "Todos";
    if (refit) fit(vis);
  }

  typeChipsEl.addEventListener("click", e => {
    const b = e.target.closest(".rr-chip"); if (!b) return;
    state.layer = b.dataset.layer || ""; render(true);
  });
  cityChipsEl.addEventListener("click", e => {
    const b = e.target.closest(".rr-chip"); if (!b) return;
    state.city = b.dataset.city || ""; render(true);
  });
  let searchTimer = null;
  searchEl.addEventListener("input", () => {
    state.q = searchEl.value.trim();
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => render(true), 200);
  });
  resetEl.addEventListener("click", () => {
    state.layer = ""; state.city = ""; state.q = ""; searchEl.value = "";
    map.closePopup(); render(true);
  });

  async function load() {
    try {
      statusEl.textContent = "Cargando lugares verificados...";
      const response = await fetch("/api/ruta-rockera", { headers: { Accept: "application/json" } });
      if (!response.ok) throw new Error("HTTP " + response.status);
      const payload = await response.json();
      allPlaces = Array.isArray(payload.places) ? payload.places : [];
      build(allPlaces);
      buildCityChips();
      updateCounts();
      render(true);
      if (heroCountEl && allPlaces.length) heroCountEl.textContent = String(allPlaces.length);
    } catch (error) {
      console.error("Ruta Rockera:", error);
      statusEl.textContent = "No fue posible cargar los lugares.";
    }
  }

  load();
})();