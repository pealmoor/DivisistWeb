// Seleccionar elementos
const userAvatar = document.querySelector('.user-avatar');
const userDropdown = document.querySelector('.user-dropdown');

// Mostrar/ocultar el menú desplegable al hacer clic en el avatar
userAvatar.addEventListener('click', (event) => {
    event.stopPropagation(); // Prevenir que el evento se propague al documento
    userDropdown.classList.toggle('hidden'); // Alternar la clase "hidden"
});

// Cerrar el menú si se hace clic fuera de él
document.addEventListener('click', (event) => {
    if (!userDropdown.contains(event.target) && !userAvatar.contains(event.target)) {
        userDropdown.classList.add('hidden'); // Asegurar que el menú se oculte
    }
});
