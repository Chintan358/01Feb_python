


from django.conf import settings
from django.core.mail import send_mail,EmailMessage


def send_mail_to_client():
    subject = 'Test'
    message = "Testing..mial"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
    send_mail( subject, message, email_from, recipient_list )


def mail_with_file(filepath):
    subject = 'Test'
    message = "Testing..mial"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
    user = EmailMessage(subject=subject,body=message,from_email=email_from,to=recipient_list)
    user.attach_file(filepath)
    user.send()