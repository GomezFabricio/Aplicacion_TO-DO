# Definición de la clase ModelTarea
class ModelTarea:
    # Variable de clase privada para almacenar todas las tareas
    __listaTareas = []

    # Constructor de la clase ModelTarea
    def __init__(self, descripcionTarea, estadoTarea="Activa"):
        # Atributos privados para descripción y estado de la tarea
        self.__descripcionTarea = descripcionTarea
        self.__estadoTarea = estadoTarea
        
    # Método para agregar la tarea actual a la lista de tareas
    def cargarLista(self):
        ModelTarea.__listaTareas.append(self)

    # Método getter para obtener la descripción de la tarea
    def getDescripcion(self):
        return self.__descripcionTarea

    # Método setter para establecer la descripción de la tarea
    def setDescripcion(self, descripcion):
        self.__descripcionTarea = descripcion

    # Método getter para obtener el estado de la tarea
    def getEstado(self):
        return self.__estadoTarea

    # Método setter para establecer el estado de la tarea
    def setEstado(self, estado):
        self.__estadoTarea = estado

    # Método estático para obtener la lista de tareas
    @staticmethod
    def obtenerListaTareas():
        return ModelTarea.__listaTareas

    # Método para eliminar una tarea específica por su índice
    def eliminarTarea(self, idTarea): 
        if idTarea < len(ModelTarea.__listaTareas):
            ModelTarea.__listaTareas.pop(idTarea)

    # Método para actualizar una tarea por su índice y nueva descripción
    def actualizarTarea(self, indice, nuevaDescripcion):
        nuevaTarea = ModelTarea(nuevaDescripcion)  
        ModelTarea.__listaTareas[int(indice)] = nuevaTarea
