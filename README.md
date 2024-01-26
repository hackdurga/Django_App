# Django Rest API for Task Management 
### Create a RESTful API for a task management system using Django Rest Framework. The API should support CRUD operations (Create, Read, Update, Delete) for tasks.

# Setup Local 

## intall DJango
```shell
$ pip install django
```
## install Django Rest Framework
```shell
$ pip install djangorestframework
```
### After that move to ToDoList directory
```shell
$ cd ToDoList
```
## Run The Django Project Server
```shell
$ python manage.py runserver
```
## After that you have to go to 
(http://127.0.0.1:8000/)

## For API
[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
## For Admin
[ http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

# For CRUD Operation

### Create
[ http://127.0.0.1:8000/](http://127.0.0.1:8000/api/create)http://127.0.0.1:8000/api/create]

### for Delete operation give the id no.
[](http://127.0.0.1:8000/api/delete/1)

### For Update and rename Operations only give the id
[](http://127.0.0.1:8000/api/1/)

# For Unit Test 
```shell
$ python manage.py test
```
# Documentation

## First Install drf-yasg
```
$ pip install drf-yasg
```

### After Running Server you will Find details of This API In the Documentation
[](http://127.0.0.1:8000/swagger/)
### or
[](http://127.0.0.1:8000/redoc/)
