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

pip install -r requirements.txt

export PYTHONPATH="$PYTHONPATH:$PWD"   (La primera vez que se instala en la máquina)


#### Para correr la aplicación en local:

uvicorn main:app --host 127.0.0.1 --port 8000


#### Para ejecutar los tests

pytest


### PARA INSTALAR NUEVAS LIBRERÍAS EN LOCAL

pip install "nombreDeLaLibrería"


### WEB HOST EN RENDER

#### URL

https://backend-ticketapp.onrender.com

#### SWAGGER

https://backend-ticketapp.onrender.com/docs
