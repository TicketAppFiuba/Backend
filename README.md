# Backend TicketAPP


### REQUISITOS

#### Se tiene que tener instalado lo siguiente:

* Docker 
* Docker-Compose


### PARA EJECUTAR LOCALMENTE CON DOCKER (PARA COMPARTIR CÓDIGO Y DEPLOYAR)

#### Cuando se ejecuta por primera vez o se actualiza:

sudo docker-compose up --build

#### Luego ejecutar:

sudo docker-compose up


### PARA EJECUTAR LOCALMENTE SIN DOCKER (SI TODAVÍA NO SE A VA COMPARTIR CÓDIGO NI DEPLOYAR)

#### Para instalar las dependencias:

pip install poetry

poetry install

#### Para correr la aplicación en local:

uvicorn main:app --host 127.0.0.1 --port 8000


### PARA INSTALAR NUEVAS LIBRERÍAS

poetry add "nombreDeLaLibrería"


### WEB HOST EN RENDER

#### URL

https://backend-ticketapp.onrender.com

#### SWAGGER

https://backend-ticketapp.onrender.com/docs
