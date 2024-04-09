from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
   
    path('students/',StudentAPI.as_view()),
    path('products/',ProductAPI.as_view()),
    path("register/",RregisterUser.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('addStudent',views.add_student),
    # path('updateStudent/<id>',views.update_student),
    # path('deleteStudent/<id>',views.delete_student)
    path("books/",BookAPI.as_view(),name="book"),
    path("book-generic/",BookAPIGeneric1.as_view(),name="bookgeneric"),
    path("book-generic/<id>",BookAPIGeneric.as_view(),name="bookgeneric1")
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
