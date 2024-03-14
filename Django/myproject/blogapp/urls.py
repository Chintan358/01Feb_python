from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
   
   path('',views.index,name="index"),
   path('reg',views.registration,name="reg")
]