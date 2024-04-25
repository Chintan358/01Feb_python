from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
# Create your views here.


global search_data
def index(request):
    
    
   
    queryset = Student.objects.all()


    
    


    if request.GET.get("search"):
        search_data = request.GET.get("search")
        queryset = Student.objects.filter(name__icontains=search_data)
    
   
    paginator = Paginator(queryset, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request,'index.html',{"queryset":page_obj})

def marks(request,id):

    ranks =  Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks')
    i = 1;
    current_rank = 0;
    for rank in ranks:
       
        if rank.student_id.student_id==id:
            
            current_rank = i;
            
        i = i+1;

    
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
    total =  queryset.aggregate(total = Sum('marks'))
    return render(request,'card.html',{'queryset':queryset, 'total':total,'rank':current_rank})