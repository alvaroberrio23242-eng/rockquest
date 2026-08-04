/**
 * trivia.js
 * ----------
 * Trivia simple: sin puntaje ni guardado, solo feedback inmediato de
 * si la respuesta elegida es correcta o no. Las preguntas vienen
 * embebidas en la pagina (ver #trivia-datos en trivia.html) para no
 * necesitar un endpoint aparte.
 */
(function () {
    const datosEl = document.getElementById('trivia-datos');
    const preguntaEl = document.getElementById('trivia-pregunta');
    const opcionesEl = document.getElementById('trivia-opciones');
    const feedbackEl = document.getElementById('trivia-feedback');
    const siguienteBtn = document.getElementById('trivia-siguiente');
    if (!datosEl || !preguntaEl) return;

    const preguntas = JSON.parse(datosEl.textContent);
    let disponibles = [...preguntas];

    function elegirPregunta() {
        if (disponibles.length === 0) {
            disponibles = [...preguntas]; // ya se vieron todas, se vuelve a barajar
        }
        const idx = Math.floor(Math.random() * disponibles.length);
        return disponibles.splice(idx, 1)[0];
    }

    function mostrarPregunta() {
        const pregunta = elegirPregunta();
        feedbackEl.textContent = '';
        feedbackEl.className = 'trivia-feedback';
        siguienteBtn.style.display = 'none';

        preguntaEl.textContent = pregunta.pregunta;
        opcionesEl.innerHTML = '';

        pregunta.opciones.forEach((opcion, idx) => {
            const btn = document.createElement('button');
            btn.className = 'trivia-opcion-btn hvr-grow';
            btn.textContent = opcion;
            btn.addEventListener('click', () => responder(idx, pregunta.correcta, btn));
            opcionesEl.appendChild(btn);
        });
    }

    function responder(elegida, correcta, btnElegido) {
        // Deshabilita todas las opciones tras responder
        opcionesEl.querySelectorAll('.trivia-opcion-btn').forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === correcta) btn.classList.add('trivia-correcta');
        });

        if (elegida === correcta) {
            feedbackEl.textContent = '¡Correcto! 🎸';
            feedbackEl.className = 'trivia-feedback trivia-feedback-ok';
        } else {
            btnElegido.classList.add('trivia-incorrecta');
            feedbackEl.textContent = 'Incorrecto 😅';
            feedbackEl.className = 'trivia-feedback trivia-feedback-error';
        }

        siguienteBtn.style.display = 'inline-block';
    }

    siguienteBtn.addEventListener('click', mostrarPregunta);
    mostrarPregunta();
})();
