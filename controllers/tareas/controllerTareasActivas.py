# Importación de la clase ModelTareasActivas del módulo models.tareas.modelTareasActivas
from models.tareas.modelTareasActivas import ModelTareasActivas

# Definición de la clase ControllerTareasActivas
class ControllerTareasActivas:
    # Constructor de la clase ControllerTareasActivas
    def __init__(self):
        # Creación de una instancia del modelo ModelTareasActivas
        self.__modelTareasActivas = ModelTareasActivas()
        # Carga la lista de tareas activas desde el modelo
        self.__modelTareasActivas.cargarLista()

    # Método para obtener la lista de tareas activas desde el modelo
    def obtenerListaTareasActivas(self):
        # Obtiene la lista de tareas activas del modelo ModelTareasActivas
        return self.__modelTareasActivas.obtenerListaTareasActivas()
