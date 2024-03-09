from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    return HttpResponse("This is myblog home page")

def about(request):
    return HttpResponse("This is myblog about page")

def contact(request):
    return HttpResponse("This is myblog contact page")