# Importación de la clase ModelTarea del módulo models.tareas.modelTarea
from models.tareas.modelTarea import ModelTarea
# Importación de la función flash del módulo flask para mostrar mensajes flash en la aplicación web

# Definición de la clase ControllerTarea
class ControllerTarea:
    # Constructor de la clase ControllerTarea
    def __init__(self, descripcionTarea=""):
        # Inicialización de la descripción de la tarea proporcionada
        self.__descripcionTarea = descripcionTarea
        # Creación de una instancia del modelo ModelTarea con la descripción proporcionada
        self.__modelTarea = ModelTarea(self.__descripcionTarea)

    # Método para cargar la lista de tareas en el modelo
    def cargarLista(self):
        # Llama al método cargarLista del modelo ModelTarea
        self.__modelTarea.cargarLista()

    # Método para obtener la lista de tareas desde el modelo
    def obtenerLista(self):
        # Obtiene la lista de tareas del modelo ModelTarea
        listaTareas = self.__modelTarea.obtenerListaTareas()
        return listaTareas

    # Método para eliminar una tarea por su ID
    def eliminarTarea(self, idTarea):
        # Llama al método eliminarTarea del modelo ModelTarea
        self.__modelTarea.eliminarTarea(idTarea)

    # Método para actualizar una tarea por su índice y nueva descripción
    def actualizarTarea(self, indice, nuevaDescripcion):
        # Llama al método actualizarTarea del modelo ModelTarea
        self.__modelTarea.actualizarTarea(indice, nuevaDescripcion)
