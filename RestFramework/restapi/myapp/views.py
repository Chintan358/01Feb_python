from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serialzer import *
from rest_framework.views import APIView
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RregisterUser(APIView):
     def post(self,request):
        user = UserSeralizer(data=request.data)
        if not user.is_valid():
                return Response({'status':'202','errors':user.errors,'message':"something went wrong"})
        user.save()
        udata = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(udata)
        
        return Response({"data":user.data, 'refresh': str(refresh),
        'access': str(refresh.access_token),"message":"Student inserted"})



class StudentAPI(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        studentdata = Student.objects.all()
        seralizer = StudentSerealizer(studentdata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            sdata =  StudentSerealizer(data=request.data)
            if not sdata.is_valid():
                return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})
            sdata.save()
            return Response({"data":sdata.data,"message":"Student inserted"})

    def put(self,request):
        try:
            sdata = Student.objects.get(id=request.data['id'])
            sdata =  StudentSerealizer(sdata,request.data)

            if not sdata.is_valid():
                return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})  
            
            sdata.save()
            return Response({"data":sdata.data,"message":"Student Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              sdata = Student.objects.get(id=request.data['id'])
              sdata.delete()
              return Response({"message":"Student Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})


class ProductAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request.user)
        prodata = Product.objects.all()
        seralizer = ProductSerializer(prodata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            prodata =  ProductSerializer(data=request.data)
            if not prodata.is_valid():
                return Response({'status':'202','errors':prodata.errors,'message':"something went wrong"})
            prodata.save()
            return Response({"data":prodata.data,"message":"Product inserted"})

    def put(self,request):
        try:
            pdata = Product.objects.get(id=request.data['id'])
            psdata =  ProductSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Product Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Product.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Product Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})

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

class BookAPI(APIView):
     def get(self,request):
        bookdata = Book.objects.all()
        book_ser = BookSerializer(bookdata,many=True)
        return Response({'bookdata':book_ser.data})
     
     def post(self,request):
            bookdata =  BookSerializer(data=request.data)
            if not bookdata.is_valid():
                return Response({'status':'202','errors':bookdata.errors,'message':"something went wrong"})
            bookdata.save()
            return Response({"data":bookdata.data,"message":"Book inserted"})
     
     def put(self,request):
        try:
            pdata = Book.objects.get(id=request.data['id'])
            psdata =  BookSerializer(pdata,request.data,partial=True)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Book Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

     def delete(self,request):
        try:
              pdata = Book.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Book Delete"})
        except Exception as e:
            print(e)
            return Response({"message":"Id not found"})
    

from rest_framework import generics
class BookAPIGeneric1(generics.ListAPIView,generics.CreateAPIView):
     queryset = Book.objects.all()
     serializer_class=BookSerializer

class BookAPIGeneric(generics.DestroyAPIView,generics.UpdateAPIView):
     queryset = Book.objects.all()
     serializer_class=BookSerializer
     lookup_field='id'
