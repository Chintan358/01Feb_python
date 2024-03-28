# from django.shortcuts import render,redirect
# from .models import Student
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# import os
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# # Create your views here.
# def index(request):
#     return render(request,'index.html')

# @login_required(login_url='/login')
# def registration(request):

#     if request.method=='POST':
#         data = request.POST
#         uname = data.get('uname')
#         email = data.get('email')
#         password = data.get('password')
#         gender = data.get('gender')
#         lang = data.getlist('lng')
#         country = data.get('country')
#         img = request.FILES.get('img')

#         # print(f"{uname} {email} {password} {gender} {country} {img}")
#         lng=""
#         for i in lang:
#             lng=lng+i+","
#         print(lng)

#         Student.objects.create(uname=uname,email=email,password=password,gender=gender,lang=lng,country=country,img=img)
    
#     alldata = Student.objects.all()
#     context = {'alldata':alldata}
#     return render(request,'reg.html',context)

# @login_required(login_url='/login')
# def delete(request,id):
#     std = Student.objects.get(id=id)
#     os.remove(std.img.path)
#     std.delete()
#     return redirect('reg')

# def edit(request,id):
#     std = Student.objects.get(id=id)

#     if request.method=='POST':
#             data = request.POST
#             std.uname = data.get('uname')
#             std.email = data.get('email')
#             std.password = data.get('password')
#             std.gender = data.get('gender')
#             lang = data.getlist('lng')
#             std.country = data.get('country')

          
            
            

#             if len(request.FILES) !=0 :
#                 if std.img != "":
#                     os.remove(std.img.path)
#                     std.img = request.FILES.get('img')
#                 else:
#                     std.img = request.FILES.get('img')
#             else:
#                 std.img=std.img

#             lng=""
#             for i in lang:
#                 lng=lng+i+","

#             print(lang)
#             std.lang = lng
          
#             std.save()
#             return redirect('reg')

#     return render(request,'update.html',{"data":std})

# def userRegistration(request):

#     if request.method=='POST':
#         data = request.POST
#         first_name = data.get('first_name')
#         last_name = data.get('last_name')
#         username = data.get('username')
#         password = data.get('password')

#         if User.objects.filter(username=username).exists():
#              messages.info(request,"User alredy exist !!!")
#              return redirect('/')

#         user = User(first_name=first_name,last_name=last_name,username=username)
#         user.set_password(password)
#         user.save()
#         messages.info(request,"Registration successfully done !!!")
#         return redirect('/')

#     return render(request,'userreg.html')

# def userLogin(request):

#     if request.method=='POST':
#         data = request.POST
#         username = data.get('username')
#         password = data.get('password')

#         if not User.objects.filter(username=username).exists():
#             messages.info(request,"Invalid credentials1")
#             return redirect('/login')

#         user =  authenticate(username=username,password=password)
#         print(user)
#         if user is None:
#             messages.info(request,"Invalid credentials")
#             return redirect('/login')
#         else:
#            login(request,user)
#            return redirect("/reg")


#     return render(request,'userlogin.html')

# def userLogout(request):
#     logout(request)
#     return render(request,'userlogin.html')