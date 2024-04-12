from django.shortcuts import render,HttpResponse
from .utils import *
# Create your views here.
def sendmail(request):
    # send_mail_to_client()
    filepath = f"{settings.BASE_DIR}/index.html"
    mail_with_file(filepath)
    return HttpResponse("mail sent...")