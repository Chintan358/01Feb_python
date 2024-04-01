from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
   
    path('students/',StudentAPI.as_view())
    # path('addStudent',views.add_student),
    # path('updateStudent/<id>',views.update_student),
    # path('deleteStudent/<id>',views.delete_student)
]

