## Warung Makan - Django

### Demo Project
* _https://warungmakan-django.herokuapp.com_

![Current Result WarungMakan - Django](https://github.com/antheiz/WarungMakan-django/blob/master/static/img/Mockup%20Warung%20Makan%20Django.png)

#### How to run This Project 

* git clone https://github.com/antheiz/WarungMakan-django.git
* cd WarungMakan-django
* python -m venv env-django
* source env-django/bin/activate/
* pip install -r requirements.txt
* python manage.py runserver
* open your favorite browser and typing _localhost:8000_

### How to run with Docker
* git clone git clone https://github.com/antheiz/WarungMakan-django.git
* cd WarungMakan-django
* docker build --tag warungmakan:1.0
* docker container create --name app1 -p 8000:8000 warungmakan:1.0
* docker container start app1
* open your favorite browser and type _localhost:8000_

### Thank You
* Build by Theis Andatu


