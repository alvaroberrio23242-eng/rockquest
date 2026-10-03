(() => {
  "use strict";

  const mapElement = document.getElementById("ruta-rockera-map");

  if (!mapElement) {
    console.error("Ruta Rockera: no existe #ruta-rockera-map.");
    return;
  }

  if (typeof L === "undefined") {
    console.error("Ruta Rockera: Leaflet no está disponible.");
    return;
  }

  const map = L.map("ruta-rockera-map", {
    center: [6.2442, -75.5812],
    zoom: 12,
    scrollWheelZoom: true
  });

  L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      maxZoom: 19,
      attribution:
        '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap</a> contributors'
    }
  ).addTo(map);

  const markersLayer = L.layerGroup().addTo(map);

  let allPlaces = [];
  let visiblePlaces = [];

  const countElement = document.getElementById("places-count");
  const listElement = document.getElementById("places-list");
  const searchElement = document.getElementById("search-place");
  const typeElement = document.getElementById("filter-type");
  const cityElement = document.getElementById("filter-city");
  const resetElement = document.getElementById("reset-map");
  const statusElement = document.getElementById("map-status");

  function escapeHtml(value) {
    const div = document.createElement("div");
    div.textContent = value ?? "";
    return div.innerHTML;
  }

  function getTypeLabel(place) {
    const labels = {
      current: "Actual",
      historical: "Histórico",
      cultural: "Cultural",
      event: "Evento"
    };
    return labels[place.type] || "Lugar";
  }

  function popupHtml(place) {
    const styles = Array.isArray(place.music_style)
      ? place.music_style.join(", ")
      : "";

    const sourceLinks = Array.isArray(place.sources)
      ? place.sources
          .filter(source => source && source.url)
          .slice(0, 5)
          .map(source => {
            const label = source.name || source.title || "Fuente";
            return `<li><a href="${escapeHtml(source.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(label)}</a></li>`;
          })
          .join("")
      : "";

    return `
      <div class="ruta-popup">
        <div class="ruta-popup-type">${escapeHtml(getTypeLabel(place))}</div>
        <h3>${escapeHtml(place.name)}</h3>
        <p><strong>${escapeHtml(place.city || "")}</strong>${place.neighborhood ? " · " + escapeHtml(place.neighborhood) : ""}</p>
        ${place.address ? `<p><strong>Dirección:</strong> ${escapeHtml(place.address)}</p>` : ""}
        ${place.description ? `<p>${escapeHtml(place.description)}</p>` : ""}
        ${styles ? `<p><strong>Estilos:</strong> ${escapeHtml(styles)}</p>` : ""}
        <p class="ruta-verification"><strong>Estado de evidencia:</strong> ${escapeHtml(place.evidence_status || "NOT_VERIFIED")}</p>
        ${place.website ? `<p><a href="${escapeHtml(place.website)}" target="_blank" rel="noopener noreferrer">Sitio web</a></p>` : ""}
        ${sourceLinks ? `<div><strong>Fuentes:</strong><ul>${sourceLinks}</ul></div>` : ""}
      </div>
    `;
  }

  function createMarker(place) {
    const coordinates = place.coordinates;
    if (!coordinates || typeof coordinates.lat !== "number" || typeof coordinates.lng !== "number") {
      return null;
    }
    const marker = L.marker([coordinates.lat, coordinates.lng]);
    marker.bindPopup(popupHtml(place), { maxWidth: 360 });
    marker.placeId = place.id;
    return marker;
  }

  function renderMarkers(places) {
    markersLayer.clearLayers();
    const bounds = [];
    places.forEach(place => {
      const marker = createMarker(place);
      if (!marker) return;
      marker.addTo(markersLayer);
      bounds.push([place.coordinates.lat, place.coordinates.lng]);
    });

    if (bounds.length > 1) {
      map.fitBounds(bounds, { padding: [40, 40], maxZoom: 14 });
    } else if (bounds.length === 1) {
      map.setView(bounds[0], 15);
    }
  }

  function renderList(places) {
    if (!listElement) return;
    listElement.innerHTML = "";

    if (!places.length) {
      listElement.innerHTML = `<div class="ruta-place-card empty">No hay lugares que coincidan con los filtros.</div>`;
      return;
    }

    places.forEach(place => {
      const card = document.createElement("article");
      card.className = "ruta-place-card";
      card.innerHTML = `
        <strong>${escapeHtml(place.name)}</strong>
        <small>${escapeHtml(place.city || "")}${place.neighborhood ? " · " + escapeHtml(place.neighborhood) : ""}</small>
        <span class="ruta-place-type">${escapeHtml(getTypeLabel(place))}</span>
      `;

      card.addEventListener("click", () => {
        const coordinates = place.coordinates;
        if (!coordinates || typeof coordinates.lat !== "number" || typeof coordinates.lng !== "number") return;
        map.setView([coordinates.lat, coordinates.lng], 16, { animate: true });
        markersLayer.eachLayer(marker => {
          if (marker.placeId === place.id) {
            marker.openPopup();
          }
        });
      });

      listElement.appendChild(card);
    });
  }

  function populateCities(places) {
    if (!cityElement) return;
    const cities = [...new Set(places.map(place => place.city).filter(Boolean))].sort((a, b) => a.localeCompare(b));
    cityElement.innerHTML = '<option value="">Todos</option>';
    cities.forEach(city => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      cityElement.appendChild(option);
    });
  }

  function applyFilters() {
    const search = searchElement ? searchElement.value.trim().toLowerCase() : "";
    const type = typeElement ? typeElement.value : "";
    const city = cityElement ? cityElement.value : "";

    visiblePlaces = allPlaces.filter(place => {
      const searchable = [
        place.name,
        place.city,
        place.neighborhood,
        place.address,
        ...(Array.isArray(place.music_style) ? place.music_style : [])
      ].filter(Boolean).join(" ").toLowerCase();

      if (search && !searchable.includes(search)) return false;
      if (type && place.type !== type) return false;
      if (city && place.city !== city) return false;
      return true;
    });

    if (countElement) countElement.textContent = visiblePlaces.length;
    renderMarkers(visiblePlaces);
    renderList(visiblePlaces);
  }

  async function loadPlaces() {
    try {
      if (statusElement) statusElement.textContent = "Cargando lugares verificados...";
      const response = await fetch("/api/ruta-rockera", {
        headers: { Accept: "application/json" }
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const payload = await response.json();
      allPlaces = Array.isArray(payload.places) ? payload.places : [];

      populateCities(allPlaces);
      applyFilters();

      if (statusElement) {
        statusElement.textContent = `${allPlaces.length} lugares verificados disponibles`;
      }
    } catch (error) {
      console.error("Ruta Rockera:", error);
      if (statusElement) {
        statusElement.textContent = "No fue posible cargar los lugares.";
      }
    }
  }

  if (searchElement) searchElement.addEventListener("input", applyFilters);
  if (typeElement) typeElement.addEventListener("change", applyFilters);
  if (cityElement) cityElement.addEventListener("change", applyFilters);
  if (resetElement) {
    resetElement.addEventListener("click", () => {
      if (searchElement) searchElement.value = "";
      if (typeElement) typeElement.value = "";
      if (cityElement) cityElement.value = "";
      applyFilters();
    });
  }

  loadPlaces();
})();
