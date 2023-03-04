from django.shortcuts import render
import os
from django.http import FileResponse
from . models import Contact
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def start_quiz(request):
    return render(request,'projects/Start_Quiz.html')

def main_quiz(request):
    return render(request,'projects/mainquiz.html')

def cal(request):
    return render(request,'projects/Calculator.html')

def resume(request):
    filepath=os.path.join('home/templates','chin_resume.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def contact(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    if Contact.objects.filter(email=email).exists():
        messages.error(request,'Email Already Registered')
        return render(request,'index.html')
    else:
        Contact.objects.create(name=name,email=email,message=message)
        messages.success(request,'Message Send')
        return render(request,'index.html') 
    
def contact_light(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    if Contact.objects.filter(email=email).exists():
        messages.error(request,'Email Already Registered')
        return render(request,'light.html')
    else:
        Contact.objects.create(name=name,email=email,message=message)
        messages.success(request,'Message Send')
        return render(request,'light.html')     
    

def light(request):
    return render(request,'light.html')    