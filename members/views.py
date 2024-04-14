from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def member(request):
    #will display(response)the message(string)
    return HttpResponse("Hello World!") 
# def member1(request):
#     return render(request,'html')  
##will return(render the ) file

def home(request):
    return render(request,'index1.html')
def index(request):
    return render(request,'index.html')
def forms(request):
    return render(request,'forms.html')
def icons(request):
    return render(request,'icons.html')
def calendar(request):
    return render(request,'calendar.html')
def icons(request):
    return render(request,'icons.html')
def profile(request):
    return render(request,'profile.html')
def tables(request):
    return render(request,'tables.html')

def meet(request):
    return render(request,'meet.html')
def meeting(request):
    return render(request,'WEB_UIKITS.html')

from django.http import HttpResponse
def wish(request):
    message="<h1>helllo glorysherin</h1>"
    return HttpResponse(message)
