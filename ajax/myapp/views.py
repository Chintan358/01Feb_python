from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    user_data = User.objects.all()
    return JsonResponse({"data":list(user_data.values())})

def adduser(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        print(uname)
        User.objects.create(uname=uname,email=email,phone=phone)
    
    return HttpResponse("Data inserted...")