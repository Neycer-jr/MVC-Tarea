from flask import Flask, render_template, request, redirect
from controllers.tarea_controller import (
    obtener_tareas,
    agregar_tarea,
    eliminar_tarea,
    editar_tarea,
    buscar_tarea,
    cambiar_estado
)

app = Flask(__name__)


@app.route("/")
def inicio():
    tareas = obtener_tareas()
    return render_template("index.html", tareas=tareas)


@app.route("/agregar", methods=["POST"])
def agregar():

    titulo = request.form["titulo"]
    descripcion = request.form["descripcion"]

    if titulo.strip() != "":
        agregar_tarea(titulo, descripcion)

    return redirect("/")


@app.route("/eliminar/<int:id>")
def eliminar(id):

    eliminar_tarea(id)
    return redirect("/")


@app.route("/estado/<int:id>")
def estado(id):

    cambiar_estado(id)
    return redirect("/")


@app.route("/editar/<int:id>")
def editar(id):

    tarea = buscar_tarea(id)

    if tarea is None:
        return redirect("/")

    return render_template("editar.html", tarea=tarea)


@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):

    titulo = request.form["titulo"]
    descripcion = request.form["descripcion"]

    editar_tarea(id, titulo, descripcion)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
    