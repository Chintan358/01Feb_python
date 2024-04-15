from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse
# Create your views here.

client = razorpay.Client(auth=("rzp_test_F4JnFLnLJ9pxYE", "2VIMfUGBXZ0YJNkLlAZ4hepM"))

def pay(request,amt):
    amount = int(amt)*100
    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    p = client.order.create(data=data)   
    print(p)
    return JsonResponse(p)
   

def payment(request):
    return render(request,'index.html')
