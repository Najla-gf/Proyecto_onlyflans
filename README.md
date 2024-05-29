# Proyecto OnlyFlans
## Trabajo colaborativo entre Najla Gatica y Jimena Traipe


Este proyecto es una aplicación web para una PYME de venta de pasteles y postres. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.

## 0. Revisión previa de instalaciones (Python y pip)

1. Verificar la versión de Python:
    ```
    python -V
    ```
> Debería mostrar algo similar a: ```Python 3.12.2```

2. Verificar la versión de pip:
    ```
    pip -V
    ```
> Debería mostrar algo similar a: ``` pip 24.0 ```

3. Ver las dependencias instaladas globalmente:
    ```
    pip list
    ```

> Nota: Saltamos la instalación de Django globalmente porque ya está instalado ```pip install django```


## 1. Preparación del entorno de desarrollo

### HITO 1: Creación de entorno virtual (venv)

Entrar a la carpeta del proyecto
```
cd proyecto_onlyflans
```
Preparación del entorno virtual e instalación de dependencias
```
python -m venv onlyflans
```
Activar el entorno virtual (en windows)
```
source onlyflans/Scripts/activate
```

Instalar Django en el entorno virtual
```
pip install django
```

Revisar las dependencias instaladas en el entorno virtual
```
pip list
```

Verificar las dependencias instaladas
```
pip freeze
```

# Crear el proyecto Django
Crear el proyecto Django:
```
django-admin startproject onlyflansPY
```

# Migrar la base de datos
Ingresar a la carpeta del proyecto:
```
cd onlyflansPY
```
Ejecutar las migraciones:
```
python manage.py migrate
```
Ejecutar el servidor de desarrollo
```
python manage.py runserver
```
