DIVISIT WEB
Pedro Alejandro Molina Ortiz 1151714
Luis Alejandro Fonseca Cadena 1151725
Santiago Rozo Sepulveda 1152324


CONEXION BASE DE DATOS A POSTGRESQL

archivo: web/settings.py
codigo: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql.psycopg2',
        'NAME': 'webdatabase',
        'USER': 'admin',
        'PASSWORD': 'UFPS2024',
        'HOST': '129.146.249.153',
        'PORT': '5442',

    }
}

explicacion:
Vamos por partes:

DATABASES: Aquí se guardan las configuraciones de las bases de datos.
'default': Esto es el nombre de la base de datos principal que usarás.
'ENGINE': Dice que vas a usar PostgreSQL, específicamente con el driver psycopg2.
'NAME': El nombre de la base de datos es webdatabase.
'USER': El usuario que se usará para acceder a la base de datos es admin.
'PASSWORD': La contraseña para ese usuario es UFPS2024.
'HOST': La dirección donde está la base de datos es 129.146.249.153, que probablemente es un servidor remoto.
'PORT': El puerto que se usa para conectarse es 5442, que no es el predeterminado (5432).
