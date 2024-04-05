from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
   
    path('students/',StudentAPI.as_view()),
    path('products/',ProductAPI.as_view()),
    path("register/",RregisterUser.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    # path('addStudent',views.add_student),
    # path('updateStudent/<id>',views.update_student),
    # path('deleteStudent/<id>',views.delete_student)
]

