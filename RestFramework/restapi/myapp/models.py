from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email =  models.CharField(max_length=20)
    age = models.IntegerField()


class Category(models.Model):
    catname = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.catname

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()

