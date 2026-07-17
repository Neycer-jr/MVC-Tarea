# Sistema de Gestión de Tareas - Arquitectura MVC

Este proyecto es un sistema básico de gestión de tareas desarrollado en Python implementando el patrón de diseño **Modelo-Vista-Controlador (MVC)**. Permite registrar, consultar y cambiar el estado de las tareas (Pendiente / Completada).

## Estructura del Proyecto

El código está organizado para separar claramente las responsabilidades:
*   **models/**: Contiene las entidades, la lógica de datos y las reglas del sistema.
*   **views/ o templates/**: Contiene la interfaz de usuario y las respuestas visuales.
*   **controllers/**: Gestiona las peticiones del usuario y comunica el Modelo con la Vista.

## Requisitos Previos
*   Tener instalado [Python 3.x](https://www.python.org/).
*   Opcional Entorno virtual configurado.

## Instrucciones de Instalación

1. Clonar el repositorio en su máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd MVC-Tarea
   

Crear y activar un entorno virtual (es opcional pero por si acaso):

En Windows:

python -m venv venv
.\venv\Scripts\activate

Instalar las dependencias necesarias:

pip install -r requirements.txt

Instalar la librería faltante:

pip install flask

Instrucciones de Ejecución
Para iniciar el sistema, ejecute el archivo principal desde la raíz del proyecto:

python app.py