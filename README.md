# Creación de 5 Proyectos Usando Docker

Este proyecto tiene como objetivo la creación de cinco aplicaciones independientes, cada una utilizando un lenguaje de programación diferente. Los lenguajes utilizados son **Flask (Python)**, **Go**, **Ruby**, **Java**, y **JavaScript (Node.js)**. Cada uno de estos proyectos está dockerizado para ser ejecutado dentro de un contenedor Docker.

## Tabla de Contenido

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación y Configuración Local](#instalación-y-configuración-local)

## Descripción del Proyecto

Este repositorio contiene cinco proyectos separados, cada uno construido utilizando un lenguaje de programación diferente. El objetivo principal es crear aplicaciones ligeras y microservicios con diferentes tecnologías, todas gestionadas por contenedores Docker para facilitar el despliegue y la ejecución. Además, estos proyectos sirven como ejemplos de cómo crear aplicaciones web sencillas y APIs RESTful usando diversos lenguajes de programación.

## Características

- **5 Proyectos Independientes**: Cada uno en un contenedor Docker.
- **Uso de Diversos Lenguajes**: Python (Flask), Go, Ruby (Sinatra), Java (Spring Boot), JavaScript (Node.js).
- **Dockerización**: Cada proyecto está completamente dockerizado para facilitar su ejecución en cualquier entorno.
- **Aplicaciones RESTful**: Todos los proyectos exponen una API RESTful simple.

## Requisitos

Para ejecutar este proyecto localmente, necesitarás los siguientes requisitos:

- [Docker](https://www.docker.com/get-started): Para crear y gestionar los contenedores.
- [Docker Compose](https://docs.docker.com/compose/): Para facilitar la gestión de múltiples contenedores.
- [Git](https://git-scm.com/): Para clonar el repositorio.

## Instalación y Configuración Local

### 1. Clonar el Repositorio

Primero, clona el repositorio a tu máquina local:

git clone [https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio](https://github.com/Fernan52/Individual-practice-on-containers-and-serverless2.git)
### 2. Construir y Ejecutar los Contenedores
Una vez clonado el repositorio, puedes construir y ejecutar los contenedores de los proyectos con Docker Compose. Para hacerlo, ejecuta el siguiente comando:
Codigo: docker-compose up --build
### 3. Acceder a las aplicaciones
Una vez que los contenedores estén en funcionamiento, podrás acceder a la aplicacion a través del siguiente puerto local: http://127.0.0.1:5000
### 4. Detener los contenedores
Cuando hayas terminado de trabajar, puedes detener los contenedores ejecutando el siguiente comando en la terminal: docker-compose down

