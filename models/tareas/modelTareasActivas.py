# Importa la clase ModelTarea desde el módulo correspondiente
from models.tareas.modelTarea import ModelTarea

# Definición de la clase ModelTareasActivas que hereda de ModelTarea
class ModelTareasActivas(ModelTarea):
    # Constructor de la clase ModelTareasActivas
    def __init__(self, descripcionTarea="", estadoTarea="Activa"):
        # Llama al constructor de la clase padre (ModelTarea) con la descripción y el estado proporcionados
        super().__init__(descripcionTarea, estadoTarea)
        
        # Inicializa la lista de tareas activas
        self.__listaTareasActivas = []

    # Método para cargar la lista de tareas activas
    def cargarLista(self):
        tareasActivas = []

        # Itera a través de la lista de tareas obtenida de la clase padre (ModelTarea)
        for tarea in ModelTarea.obtenerListaTareas():
            if tarea.getEstado() == 'Activa':
                tareasActivas.append(tarea)

        # Asigna la lista de tareas activas al atributo privado
        self.__listaTareasActivas = tareasActivas

    # Método para obtener la lista de tareas activas
    def obtenerListaTareasActivas(self):
        return self.__listaTareasActivas
