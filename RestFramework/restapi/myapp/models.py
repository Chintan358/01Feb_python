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


class Author(models.Model):
    aname = models.CharField(max_length=20)

   

class Publication(models.Model):
    pname = models.CharField(max_length=20)

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE,default=1)
    bname = models.CharField(max_length=20)
    image = models.ImageField(upload_to='my_image',default="img")

