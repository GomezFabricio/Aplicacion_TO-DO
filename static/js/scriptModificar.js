const botonesEdicion = document.querySelectorAll('.editButton');

botonesEdicion.forEach(function(boton) {
    boton.addEventListener('click', function() {
        const indice = boton.getAttribute('dataIndex');
        const descripcionActual = boton.getAttribute('dataDescription');
        const nuevaDescripcion = prompt('Editar tarea:', descripcionActual);

        if (nuevaDescripcion !== null) {
            const url = boton.getAttribute('dataUrl');

            // Crear un objeto con los datos a enviar al servidor
            const datos = {
                indice: indice,
                nuevaDescripcion: nuevaDescripcion
            };

            // Realizar una solicitud POST al servidor usando Fetch
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            })
            .then(response => {
                if (response.ok) {
                    // La solicitud se realizó correctamente
                    return response.json();
                } else {
                    throw new Error('Error al actualizar la tarea');
                }
            })
            .then(data => {
                // Actualiza la descripción de la tarea en la vista
                const taskDescription = document.querySelector(`label[for="tarea-${indice}"]`);
                taskDescription.textContent = data.descripcion; // Actualiza la descripción
                console.log('Datos actualizados:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});
