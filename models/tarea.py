class Tarea:
    def __init__(self, id, titulo, descripcion, estado="Pendiente"):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado