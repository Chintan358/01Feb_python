from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
# Create your views here.
def index(request):
    queryset = Student.objects.all()

    paginator = Paginator(queryset, 10)  

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)


    return render(request,'index.html',{"queryset":page_obj})

def marks(request,id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
    total =  queryset.aggregate(total = Sum('marks'))
    return render(request,'card.html',{'queryset':queryset, 'total':total})