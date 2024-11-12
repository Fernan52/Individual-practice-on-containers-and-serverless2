# Creation of 5 Projects Using Docker

This project aims to create five independent applications, each using a different programming language. The languages used are **Flask (Python)**, **Go**, **Ruby**, **Java**, and **JavaScript (Node.js)**. Each of these projects is dockerized to run inside a Docker container.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation and Local Configuration](#install-and-configure-local)

## Project Description

This repository contains five separate projects, each built using a different programming language. The main goal is to create lightweight applications and microservices with different technologies, all managed by Docker containers for ease of deployment and execution. In addition, these projects serve as examples of how to create simple web applications and RESTful APIs using various programming languages.

## Features.

- 5 Independent Projects**: Each in a Docker container.
- Use of several languages**: Python (Flask), Go, Ruby (Sinatra), Java (Spring Boot), JavaScript (Node.js).
- Dockerization**: Each project is fully dockerized to facilitate its execution in any environment.
- RESTful applications**: All projects expose a simple RESTful API.

## Requirements

To run this project locally, you will need the following requirements:

- [Docker](https://www.docker.com/get-started): To create and manage containers.
- Docker Compose](https://docs.docker.com/compose/): To facilitate the management of multiple containers.
- Git](https://git-scm.com/): To clone the repository.

## Local Installation and Configuration

### 1. Clone the Repository

git clone [https://github.com/tu-usuario/nombre-del-repositorio.git
cd repository-name](https://github.com/Fernan52/Individual-practice-on-containers-and-serverless2.git)
### 2. Build and Run the Containers
Once the repository is cloned, you can build and run the project containers with Docker Compose. To do this, run the following command:
Code: docker-compose up --build.
### 3. Accessing the applications
Once the containers are up and running, you will be able to access the application through the following local port: http://127.0.0.1:5000
### Stop the containers
When you are done working, you can stop the containers by running the following command in the terminal: docker-compose down

