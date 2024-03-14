from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name+","+self.email+","+self.password

class Product(models.Model):
   name=models.CharField(max_length=100)