# Plantilla de Django

Este repositorio de ejemplo contiene la estructura recomendada para un proyecto de Python Django. En este ejemplo, usamos `django` para construir una aplicación web y `unittest` para ejecutar pruebas.

Para un tutorial más detallado, consulta nuestro [tutorial de Django](https://code.visualstudio.com/docs/datascience/data-science-tutorial).

El código en este repositorio sigue las pautas de estilo de Python descritas en [PEP 8](https://peps.python.org/pep-0008/).

## Ejecutando el Ejemplo

Para ejecutar este ejemplo con éxito, recomendamos las siguientes extensiones de VS Code:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 

- Abre la carpeta de la plantilla en VS Code (**Archivo** > **Abrir Carpeta...**)
- Crea un entorno virtual de Python usando el comando **Python: Create Environment** que se encuentra en la Paleta de Comandos (**Ver > Paleta de Comandos**). Asegúrate de instalar las dependencias que se encuentran en el archivo `pyproject.toml`
- Asegúrate de que tu nuevo entorno esté seleccionado usando el comando **Python: Select Interpreter** que se encuentra en la Paleta de Comandos
- Crea e inicializa la base de datos ejecutando `python manage.py migrate` en una terminal activada.
- Ejecuta la aplicación usando la vista Ejecutar y Depurar o presionando `F5`
- Ejecuta las pruebas ejecutando `python manage.py test` en una terminal activada
