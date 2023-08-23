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
    return render(request,'index.html')