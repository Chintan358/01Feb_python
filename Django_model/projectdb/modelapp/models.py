from django.db import models

# Create your models here.

class Department(models.Model):
    deptname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.deptname

class Employee(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=30)
    salary=models.IntegerField(default=0)

    