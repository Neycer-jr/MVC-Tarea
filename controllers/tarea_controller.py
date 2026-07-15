from models.tarea import Tarea

tareas = []

def obtener_tareas():
    return tareas

def agregar_tarea(titulo, descripcion):
    if titulo.strip() == "":
        return

    nueva = Tarea(
        len(tareas) + 1,
        titulo,
        descripcion
    )

    tareas.append(nueva)

def buscar_tarea(id):
    for tarea in tareas:
        if tarea.id == id:
            return tarea
    return None

def editar_tarea(id, titulo, descripcion):
    tarea = buscar_tarea(id)
    if tarea:
        tarea.titulo = titulo
        tarea.descripcion = descripcion

def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t.id != id]

def cambiar_estado(id):
    tarea = buscar_tarea(id)

    if tarea:
        if tarea.estado == "Pendiente":
            tarea.estado = "Completada"
        else:
            tarea.estado = "Pendiente"