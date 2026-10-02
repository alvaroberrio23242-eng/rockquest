/**
 * video-bg.js
 * ------------
 * Hace rotar varios clips de video como fondo de pantalla completo.
 * Si un clip falla al reproducir, salta al siguiente en vez de
 * romper la pagina o dejar la pantalla en negro.
 * (mismo patron que usa SalsaQuest en su propio video-bg.js)
 */
(function () {
    const video = document.getElementById('video-bg');
    if (!video) return;

    const baseUrl = video.dataset.baseUrl || '';

    const clips = [
        'rock-1.mp4',
        'rock-2.mp4',
        'rock-3.mp4',
    ];

    let indice = 0;
    let intentosFallidos = 0;

    function reproducirClip(i) {
        video.src = baseUrl + clips[i];
        video.load();
        const promesa = video.play();
        if (promesa && typeof promesa.catch === 'function') {
            promesa.catch(() => {
                // Autoplay bloqueado por el navegador, o el archivo no
                // sirve: probamos con el siguiente clip.
                irAlSiguiente();
            });
        }
    }

    function irAlSiguiente() {
        intentosFallidos += 1;
        if (intentosFallidos >= clips.length) {
            // Ya probamos todos los clips: nos quedamos con el
            // poster/color de respaldo definido en el CSS.
            return;
        }
        indice = (indice + 1) % clips.length;
        reproducirClip(indice);
    }

    video.addEventListener('ended', function () {
        intentosFallidos = 0;
        indice = (indice + 1) % clips.length;
        reproducirClip(indice);
    });

    video.addEventListener('error', irAlSiguiente);

    if (clips.length > 0) {
        reproducirClip(indice);
    }
})();
