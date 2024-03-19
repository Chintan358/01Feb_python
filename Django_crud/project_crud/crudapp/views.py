from django.shortcuts import render,redirect
from .models import Student
import os
# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):

    if request.method=='POST':
        data = request.POST
        uname = data.get('uname')
        email = data.get('email')
        password = data.get('password')
        gender = data.get('gender')
        lang = data.getlist('lng')
        country = data.get('country')
        img = request.FILES.get('img')

        # print(f"{uname} {email} {password} {gender} {country} {img}")
        lng=""
        for i in lang:
            lng=lng+i+","
        print(lng)

        Student.objects.create(uname=uname,email=email,password=password,gender=gender,lang=lng,country=country,img=img)
    
    alldata = Student.objects.all()
    context = {'alldata':alldata}
    return render(request,'reg.html',context)

def delete(request,id):
    std = Student.objects.get(id=id)
    os.remove(std.img.path)
    std.delete()
    return redirect('reg')

def edit(request,id):
    std = Student.objects.get(id=id)

    if request.method=='POST':
            data = request.POST
            std.uname = data.get('uname')
            std.email = data.get('email')
            std.password = data.get('password')
            std.gender = data.get('gender')
            lang = data.getlist('lng')
            std.country = data.get('country')

          
            
            

            if len(request.FILES) !=0 :
                if std.img != "":
                    os.remove(std.img.path)
                    std.img = request.FILES.get('img')
                else:
                    std.img = request.FILES.get('img')
            else:
                std.img=std.img

            lng=""
            for i in lang:
                lng=lng+i+","

            print(lang)
            std.lang = lng
          
            std.save()
            return redirect('reg')

    return render(request,'update.html',{"data":std})