// Obtén una referencia a los elementos de lista
const listaGeneral = document.getElementById('listaGeneral');
const listaCompletadas = document.getElementById('listaCompletadas');
const listaActivas = document.getElementById('listaActivas');

// Obtén una referencia al elemento de título
const titulo = document.querySelector('.listTitle');

// Función para actualizar la clase activa y el título
function actualizarEstadoSeleccionado(elemento) {
    const elementosLista = [listaGeneral, listaCompletadas, listaActivas];

    // Elimina la clase 'active' de todos los elementos de la lista
    elementosLista.forEach((el) => {
        el.classList.remove('active');
    });

    // Agrega la clase 'active' al elemento seleccionado
    elemento.classList.add('active');

    // Actualiza el título según el elemento seleccionado
    titulo.textContent = elemento.textContent;
}

// Agrega eventos de clic a los elementos de lista
listaGeneral.addEventListener('click', (e) => {
    actualizarEstadoSeleccionado(listaGeneral);
});

listaCompletadas.addEventListener('click', (e) => {
    actualizarEstadoSeleccionado(listaCompletadas);
});

listaActivas.addEventListener('click', (e) => {

    actualizarEstadoSeleccionado(listaActivas);
});

