# Trabajo colaborativo entre Najla Gatica y Jimena Traipe

# Proyecto OnlyFlans

Este proyecto es una aplicación web para una PYME de venta de pasteles y postres. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.

## 0. Revisión previa de instalaciones (Python y pip)

1. Verificar la versión de Python:
    ```bash
    python -V
    ```
    Debería mostrar algo similar a:
    ```
    Python 3.12.2
    ```

2. Verificar la versión de pip:
    ```bash
    pip -V
    ```
    Debería mostrar algo similar a:
    ```
    pip 24.0
    ```

3. Ver las dependencias instaladas globalmente:
    ```bash
    pip list
    ```

> Nota: Saltamos la instalación de Django globalmente porque ya está instalado.

## 1. Preparación del entorno de desarrollo

### 1.0 Etapa 0: Entrar a la carpeta del proyecto
```bash
cd onlyflans_proyecto

1.1 Etapa 1: Preparación del entorno virtual e instalación de dependencias
python -m venv onlyflans

1.2 etapa 2: Activar el entorno virtual (en windows)

onlyflans\Scripts\activate

- (en MacOS/Linux)
source onlyflans/bin/activate

1.3 Etapa 3: Instalar Django en el entorno virtual
pip install django

1.4 Revisar las dependencias instaladas en el entorno virtual
pip list

1.5 Verificar las dependencias instaladas
pip freeze

Crear y configurar el proyecto Django
Ingresar a la carpeta del entorno virtual
cd onlyflans

Crear el proyecto Django:
django-admin startproject onlyflansApp

Migrar la base de datos:
Ingresar a la carpeta del proyecto:
cd onlyflansApp

Preparar las migraciones (opcional, generalmente automático, aún no lo ocupamos porque estamos en el hito 1):
python manage.py makemigrations

Ejecutar las migraciones:
python manage.py migrate

Ejecutar el servidor de desarrollo
python manage.py runserver









