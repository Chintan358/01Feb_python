from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        data =  User.objects.filter(username=username,password=password)
        
        if len(data) > 0 :
           for dt in data:
            role = dt.role.role_name
            if role == 'Principal':
               return render(request,"principal.html")
            elif role == 'Teacher':
               return render(request,"teacher.html")
            else:
               return render(request,"student.html",{"name":dt.username})
        else:
            return render(request,"index.html",{"msg":"Invalid credentials"})


    return render(request,"index.html")

def reg(request):

    role_object = Roles.objects.all()
    if request.method == 'POST':
        id = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']
        role_data = Roles.objects.get(id = id)
        User.objects.create(role = role_data,username=username,password=password)

       
        return render(request,"reg.html",{"role":role_object})

   
    return render(request,"reg.html",{"role":role_object})