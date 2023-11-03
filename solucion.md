Creamos el entorno virtual 
```bash
python -m venv myvenv 
```
Y lo activamos 
```bash
myvenv\Scripts\activate 
```
Lo metemos en el .gitignore para no tener que subir todos los archivos.

Actualizamos el pip dentro del entorno con el comando 
```bash
python -m pip install --upgrade pip
```
Creamos el fichero requierements.txt con el texto 
```text
Django
```

Ejecutamos este comando para instalar la version de Django indicada en el requierements.txt, al escribir Django son indicar la version se instala la ultima.
```bash
pip install -r requierements.txt
```
Iniciamos el projecto task 
```bash 
django-admin.exe startproject task .
```

En el fichero task/settngs.py configuramos el idioma del codigo, 
```python
LANGUAGE_CODE = 'es-es'
```
la zona horaria
```python
TIME_ZONE = 'Europe/Berlin'
```
y añadimos debajo de ESTATIC_URL lo siguiente:
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```
Añadimos en el mismo fichero lo siguiente:
```python
ALLOWED_HOSTS = ['localhost','127.0.0.1']
```

Y antes de iniciar el servidor creamos una base de datos para task:
```bash
python manage.py migrate
```

Ahora si podemos iniciar el servidor: 
```bash
python manage.py runserver
```

Creamos una aplicacion llamada todolist:
```bash
python manage.py startapp todolist
```

