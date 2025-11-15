from django.urls import path
from .views import *


app_name= 'app1'

urlpatterns=[
    path("",plant_list,name="plant_list"),
    path("insert/",plant_insert,name="plant_insert"),
    path("detail/<int:id>/",plant_detail,name="plant_detail"),
    path("update/<int:id>/",plant_update,name="plant_update"),
    path("delete/<int:id>/",plant_delete,name="plant_delete"),
    
    path('register/',register,name="register"),
    path('login/',login_user,name="login_user")
]