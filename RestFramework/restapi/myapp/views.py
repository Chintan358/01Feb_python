from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serialzer import *
from rest_framework.views import APIView
# Create your views here.



class StudentAPI(APIView):
    def get(self,request):
        studentdata = Student.objects.all()
        seralizer = StudentSerealizer(studentdata,many=True)
        return Response({'apidata':seralizer.data})


# @api_view(['GET'])
# def index(request):
#     studentdata = Student.objects.all()
#     seralizer = StudentSerealizer(studentdata,many=True)
#     return Response({'apidata':seralizer.data})

# @api_view(['POST'])
# def add_student(request):
#     data = request.data 
#     sdata =  StudentSerealizer(data=request.data)

#     if not sdata.is_valid():
#         return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})
    
#     sdata.save()
    
#     return Response({"data":sdata.data,"message":"Student inserted"})

# @api_view(['PUT'])
# def update_student(request,id):
#     sdata = Student.objects.get(id=id)
#     sdata =  StudentSerealizer(sdata,request.data)

#     if not sdata.is_valid():
#         return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})  
    
#     sdata.save()
#     return Response({"data":sdata.data,"message":"Student Updated"})

# @api_view(['DELETE'])
# def delete_student(request,id):
#       sdata = Student.objects.get(id=id)
#       sdata.delete()
#       return Response({"message":"Student Updated"})