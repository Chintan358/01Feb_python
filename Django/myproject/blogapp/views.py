from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("""<h1>hello pythonb</h1>
    #                         <h2>Hello tops</h2>
    #                     """)
    namelist = [
            {"name":"jatin","email":"jatin@gm,ail.com"},
            {"name":"Khushi","email":"khushi@gmail.com"}]
    return render(request,'index.html',{"names":namelist})

def registration(request):
    
    data = request.POST
    name = data.get('name')
    email = data.get('email')



    
    return render(request,'reg.html')