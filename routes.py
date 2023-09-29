from flask import render_template, session, redirect, url_for, request, jsonify
from config import app
from controllers.tareas.controllerTarea import ControllerTarea
from controllers.tareas.controllerTareasActivas import ControllerTareasActivas
from controllers.tareas.controllerTareasCompletadas import ControllerTareasCompletadas

listaTareas = []

@app.route('/')
def index():
    # Ruta principal, muestra todas las tareas
    vistaActual = 'todas'  # Establece la vista actual como "todas"
    return render_template('/components/layout.html', vistaActual=vistaActual)

@app.route('/tareas', methods=['GET'])
def tareas():
    # Ruta para mostrar todas las tareas
    vistaActual = 'todas'  # Establece la vista actual como "todas"
    return render_template("tareas/viewTareas.html", listaTareas=ControllerTarea().obtenerLista(), vistaActual=vistaActual)

@app.route('/agregarTarea', methods=['GET', 'POST'])
def agregarTarea():
    # Ruta para agregar una nueva tarea
    vistaActual = 'todas'  # Establece la vista actual como "todas"
    if request.method == 'POST':
        tarea = request.form['tarea']

        controllerTarea = ControllerTarea(tarea)
        controllerTarea.cargarLista()
        listaTareas = controllerTarea.obtenerLista()
        
        return render_template('/tareas/viewTareas.html', listaTareas=listaTareas, vistaActual=vistaActual)

@app.route('/eliminarTarea/<int:tareaId>', methods=['GET'])
def eliminarTarea(tareaId):
    # Ruta para eliminar una tarea por su ID
    vistaActual = 'todas'  # Establece la vista actual como "todas"
    controllerTarea = ControllerTarea()
    controllerTarea.eliminarTarea(tareaId)
    return render_template('tareas/viewTareas.html', listaTareas=controllerTarea.obtenerLista(), vistaActual=vistaActual)

@app.route('/editarTarea', methods=['POST'])
def editarTarea():
    # Ruta para editar una tarea
    vistaActual = 'todas'  # Establece la vista actual como "todas"
    data = request.get_json()
    indice = data['indice']
    nuevaDescripcion = data['nuevaDescripcion']

    controllerTarea = ControllerTarea()
    controllerTarea.actualizarTarea(indice, nuevaDescripcion)

    return jsonify({'descripcion': nuevaDescripcion})

# ------------------------------ Tareas Activas ------------------------------ #
@app.route('/tareasActivas')
def tareasActivas():
    # Ruta para mostrar tareas activas
    vistaActual = 'activas'  # Establece la vista actual como "activas"
    controllerTareasActivas = ControllerTareasActivas()
    listaTareasActivas = controllerTareasActivas.obtenerListaTareasActivas()
    return render_template('tareas/viewTareasActivas.html', listaTareas=listaTareasActivas, vistaActual=vistaActual)

@app.route('/eliminarTareaActiva/<int:tareaId>', methods=['GET'])
def eliminarTareaActiva(tareaId):
    # Ruta para eliminar una tarea activa
    vistaActual = 'activas'  # Establece la vista actual como "activas"
    controllerTarea = ControllerTarea()
    controllerTarea.eliminarTarea(tareaId)
    return render_template('tareas/viewTareasActivas.html', listaTareas=controllerTarea.obtenerLista(), vistaActual=vistaActual)

@app.route('/editarTareaActiva', methods=['POST'])
def editarTareaActiva():
    # Ruta para editar una tarea activa
    vistaActual = 'todas'  # Establece la vista actual como "todas"
    data = request.get_json()
    indice = data['indice']
    nuevaDescripcion = data['nuevaDescripcion']

    controllerTarea = ControllerTarea()
    controllerTarea.actualizarTarea(indice, nuevaDescripcion)

    return jsonify({'descripcion': nuevaDescripcion})

# ---------------------------- Tareas Completadas ---------------------------- #
@app.route('/tareasCompletadas')
def tareasCompletadas():
    # Ruta para mostrar tareas completadas
    controllerTareasCompletadas = ControllerTareasCompletadas()
    listaTareasCompletadas = controllerTareasCompletadas.obtenerListaTareasCompletadas()
    return render_template('tareas/viewTareasCompletadas.html', listaTareas=listaTareasCompletadas)

@app.route('/marcarTareaCompletada/<int:tareaId>', methods=['GET'])
def marcarTareaCompletada(tareaId):
    # Ruta para marcar una tarea como completada
    controllerTareasCompletadas = ControllerTareasCompletadas()
    controllerTareasCompletadas.marcarComoCompletada(tareaId)
    return redirect(url_for('tareasCompletadas'))  # Redirige a la vista de tareas completadas después de marcar una tarea
