# Importa la clase ModelTarea desde el módulo correspondiente
from models.tareas.modelTarea import ModelTarea

# Definición de la clase ModelTareaCompletada que hereda de ModelTarea
class ModelTareaCompletada(ModelTarea):
    # Constructor de la clase ModelTareaCompletada
    def __init__(self, descripcionTarea="", estadoTarea="Completada"):
        # Llama al constructor de la clase padre (ModelTarea) con la descripción y el estado proporcionados
        super().__init__(descripcionTarea, estadoTarea)
        
        # Inicializa la lista de tareas completadas
        self.__listaTareasCompletadas = []

    # Método para marcar una tarea como completada
    def marcarComoCompletada(self, tareaPosicion):
        if 0 <= tareaPosicion < len(ModelTarea.obtenerListaTareas()):
            lista = ModelTarea.obtenerListaTareas()
            tareaCompletada = lista[tareaPosicion]
            tareaCompletada.setEstado("Completada")
            
            # Agrega la tarea a la lista de tareas completadas
            self.__listaTareasCompletadas.append(tareaCompletada)

    # Método para obtener la lista de tareas completadas
    def obtenerListaTareasCompletadas(self):
        return self.__listaTareasCompletadas
