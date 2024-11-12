# Creación de 5 Proyectos Usando Docker

Este proyecto tiene como objetivo la creación de cinco aplicaciones independientes, cada una utilizando un lenguaje de programación diferente. Los lenguajes utilizados son **Flask (Python)**, **Go**, **Ruby**, **Java**, y **JavaScript (Node.js)**. Cada uno de estos proyectos está dockerizado para ser ejecutado dentro de un contenedor Docker.

## Tabla de Contenido

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación y Configuración Local](#instalación-y-configuración-local)
5. [Uso de Cada Lenguaje](#uso-de-cada-lenguaje)
    - [Flask (Python)](#flask-python)
    - [Go](#go)
    - [Ruby (Sinatra)](#ruby-sinatra)
    - [Java (Spring Boot)](#java-spring-boot)
    - [JavaScript (Node.js)](#javascript-nodejs)

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

```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
