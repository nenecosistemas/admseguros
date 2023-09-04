# admseguros

DJANGO - PYTHON

1) Instalar  python desde www.python.org/download
2) Verificar en "variables de entorno" de windows que esten las carpetas
3) crear una carpeta para Django
4) Creamos un entorno virtual  para implementar django
   py -m venv (nombre enviroment "neneco")
5) Activamos nuestro enviroment
   neneco\Script\activate
6) Instalamos Django 
   (neneco) c:\usr\edu\django\pip install django==2.2.6
7) Verificamos todo lo instalado
   pip freeze
8) creamos un proyecto
   django-admin startproject "nombre del proyecto"
9) creamos una app
   python manage.py startapp "nombre de la app"
10) Instalar Mysqlclient
    pip install mysqlclient
11) corremos el servidor
    python manage.py runserver 
12) Una vez generado el modelo de datos
    python manage.py migrate    
    python manage.py createsuperuser
    python manage.py makemigrations
    python manage.py migrate
