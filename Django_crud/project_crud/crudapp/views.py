from django.shortcuts import render
from .models import Student
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