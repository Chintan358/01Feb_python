from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):

    if request.method=='POST':
        data = request.POST

        name = data.get('uname')
        email = data.get('email')
        password = data.get('pass')

        Student.objects.create(name=name,email=email,password=password)

    alldata =  Student.objects.all()
    context = {'alldata':alldata}
    return render(request,'home.html',context)

def delete(request,id):
    qryset = Student.objects.get(id=id)
    qryset.delete()
    return redirect('/mysite/home')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
