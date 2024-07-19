# views.py
from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .serializers import UserInfoSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            # Sending email with form data
            subject = 'New Form Submission'
            message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            sender_email = settings.EMAIL_HOST_USER  # Use your email as sender
            recipient_list = ['VishwakarmaArpita1219@gmail.com']  # Replace with recipient's email address

            try:
                send_mail(subject, message_body, sender_email, recipient_list, fail_silently=False)
                return redirect('thank_you')
            except Exception as e:
                messages.error(request, f'Something went wrong! Error: {e}')
                return redirect('Home')
        else:
            messages.error(request, 'Invalid form submission. Please check the form.')
    else:
        form = UserInfoForm()
    
    return render(request, 'index.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
