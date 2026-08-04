console.log('RockQuest cargado');

// Inicializa las capas de parallax decorativas del fondo (ver
// #parallax-bg en base.html). Cada capa se mueve a distinta
// velocidad al hacer scroll, dando sensacion de profundidad.
// El propio plugin ya respeta 'prefers-reduced-motion' via CSS
// (display:none en .parallax-layer), asi que no hace falta chequearlo aca.
$(function () {
    if (typeof $.fn.parallax !== 'function') return;

    $('.parallax-glow-magenta').parallax('50%', 0.2);
    $('.parallax-glow-cyan').parallax('50%', 0.4);
});
