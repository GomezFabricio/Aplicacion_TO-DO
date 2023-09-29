# Importación de la clase ModelTareaCompletada del módulo models.tareas.modelTareasCompletadas
from models.tareas.modelTareasCompletadas import ModelTareaCompletada

# Definición de la clase ControllerTareasCompletadas
class ControllerTareasCompletadas:
    # Constructor de la clase ControllerTareasCompletadas
    def __init__(self):
        # Creación de una instancia del modelo ModelTareaCompletada
        self.__modelTareaCompletada = ModelTareaCompletada()

    # Método para marcar una tarea como completada
    def marcarComoCompletada(self, tareaPosicion):
        # Llama al método correspondiente del modelo ModelTareaCompletada
        self.__modelTareaCompletada.marcarComoCompletada(tareaPosicion)

    # Método para obtener la lista de tareas completadas desde el modelo
    def obtenerListaTareasCompletadas(self):
        # Obtiene la lista de tareas completadas del modelo ModelTareaCompletada
        return self.__modelTareaCompletada.obtenerListaTareasCompletadas()
