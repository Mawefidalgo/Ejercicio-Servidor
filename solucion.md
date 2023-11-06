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

En el fichero task/settings.py en las aplicaciones instaladas añadimos la aplicacion nueva:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todolist',
]
```

Agregamos el modelo a la base de datos con el comando:
```bash
python manage.py makemigrations todolist
python manage.py migrate todolist
```

Registramos nuestro modelo en el fichero admin 
```python
admin.site.register(Task)
```

Creamos un super usuario para poder acceder con el comando 
```bash
python manage.py createsuperuser
```

Agregamos la url de nuestra aplicacion todolist
```python
path('',include('todolist.urls)),
```

Creamos un fichero urls.py dentro de la carpeta todolist y le agregamos lo siguiente:
```python
urlpatterns = [
    path('task/', views.task_list, name='task_list'),
]
```

En el fichero views.py creamos una vista y añadimos la siguiente mini-vista:
```python
def task_list(request):
    task = Task.objects.all()
    return render(request, 'todolist/task_list.html', {"task":task})
```

Creamos una carpeta templates dentro de todolist y dentro de templates creamos otra carpeta llamada tambien todolist, posteriormente creamos un fichero dentro de esta llamado task_list.HTML

En el fichero task_list.HTML le ponemos el titulo To do list y agregamos el codigo:
```python
<html>
        <head>
            <title>Task List</title>
        </head>
        <body>
            <h1>Lista de Tareas</h1>
            <ul>
                {% for task in tasks %}
                <li>
                    <h2>{{ task.title }}</h2>
                    <p>{{ task.description }} - {% if task.completed %} Sí {% else %} No {% endif %}</p>
                </li>
                {% empty %}
                <p>No hay tareas disponibles.</p>
                {% endfor %}
            </ul>
        </body>
    </html>
```
