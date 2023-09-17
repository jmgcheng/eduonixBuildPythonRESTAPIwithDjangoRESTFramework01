# eduonixBuildPythonRESTAPIwithDjangoRESTFramework01

Python 3.11.0
pip 22.3 

In requirements.txt
```
pip freeze > requirements
pip install -r requirements.txt
```
asgiref==3.7.2
Django==4.2.5
djangorestframework==3.14.0
pytz==2023.3.post1
sqlparse==0.4.4
tzdata==2023.3




## Setup - Step 1

Go to desktop
```
cd desktop
```

Create project folder
desktop
```
mkdir projName01
```

Go in your project folder
desktop
```
cd projName01
```

Create environment named venv
desktop/projName01
```
python -m venv venv
```

Activate environment
desktop/projName01
```
venv\Scripts\activate.bat
```

Install django
(venv) desktop/projName01
```
python -m pip install Django
```

Start project
(venv) desktop/projName01
```
django-admin startproject core
```

cd in your project
(venv) desktop/projName01
```
cd core
```

IDE
- drag outer core folder in your IDE(visual studio code)
OR
(venv) desktop/projName01/core
```
code .
```

## Setup - Step 2

1. Create app
```python
python manage.py startapp backend
pip install djangorestframework
```

2. setup settings.py

3. setup models.py

5. setup admin.py

6. setup signals.py, apps.py

7. setup serializers.py

8. setup permissions.py

9. setup urls.py for core, app

10. Migrations, Super user, Run server
```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
