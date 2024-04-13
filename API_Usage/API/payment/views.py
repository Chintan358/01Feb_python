from django.shortcuts import render
import razorpay
# Create your views here.

client = razorpay.Client(auth=("rzp_test_F4JnFLnLJ9pxYE", "2VIMfUGBXZ0YJNkLlAZ4hepM"))

def pay(request):
    data = { "amount": 50000, "currency": "INR", "receipt": "order_rcptid_11" }
    p = client.order.create(data=data)   
    
    return render(request,'index.html',{'data':p})
