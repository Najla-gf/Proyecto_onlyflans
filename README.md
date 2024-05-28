# Proyecto OnlyFlans
# Trabajo colaborativo entre Najla Gatica y Jimena Traipe

Este proyecto es una aplicación web para una PYME de venta de pasteles y postres. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.



OnlyFlans
Este proyecto describe cómo configurar y ejecutar un proyecto de Django llamado onlyflans en Windows.

Requerimientos
1. Crear y activar un entorno virtual
Primero, crea un entorno virtual llamado onlyflans y actívalo:
python -m venv onlyflans
onlyflans\Scripts\activate

A continuación, comprueba que la versión de Python usada es Python 3:
python --version

2. Instalar Django
Instala Django 3.2.4 dentro del entorno virtual onlyflans:
pip install django==3.2.4

Verifica que Django haya sido instalado exitosamente utilizando el comando pip freeze. Deberías ver una salida similar a:
Django==3.2.4

3. Generar y configurar el proyecto Django
Usa django-admin para generar un proyecto llamado onlyflans:
django-admin startproject onlyflans

Ingresa a la carpeta del proyecto recién creado:
cd onlyflans

Aplica las migraciones iniciales para configurar la base de datos:
python manage.py migrate

Inicia el servidor de desarrollo de Django:
python manage.py runserver

Abre tu navegador y dirígete a http://127.0.0.1:8000/ para ver la página de bienvenida de Django.

