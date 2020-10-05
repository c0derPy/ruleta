SIMULADOR DE RULETA:

Esta API desarrollada en Python3 Flask contiene la logica de un simulador de ruleta de apuestas.

Rutas:
- /api/ruleta <GET>
Inicia una ronda de apuestas en la ruleta y retorna un JSON con los resultados de la apuesta.

- /api/jugadores <GET>
Retorna una lista con todos los jugadores activos del casino

- /api/jugador/<id> <GET>
Retorna el detalle de un jugador indicado

- /api/jugador/registro <POST>
Almacena la informacion de un nuevo jugador

- /api/jugador/editar/<id> <PUT>
Actualiza la informacion de un jugador indicado


DEPLOYMENT:

Para el deployment de la API se utiliza Docker, y usamos Heroku para publicar la API.

Realizar los siguientes pasos para publicar la API en Heroku:

1. Crear una cuenta en Heroku.
2. Instalar Heroku CLI.
3. En una terminal linux escribir los siguientes comandos:
   - heroku login
   - heroku create <nombre-app>
   - clonar este repositorio de GitHub
   - acceder al directorio clonado
   - heroku git:remote -a <nombre-app>
   - git push heroku master

Con los pasos mencionados tendriamos la API corriendo en Heroku utilizando Docker.


INICIAR APLICACION:

Para realizar pruebas de la API en una interfaz grafica web, descargamos el repositorio: https://github.com/c0derPy/ruleta_app.git
y abrimos el archivo index.html en un navegador preferiblemente google chrome.