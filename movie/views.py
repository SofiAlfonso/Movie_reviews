from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return HttpResponse('<center><h1>Welcome to Home Page :)</h1><center>')
   #return render (request,'home.html')
   return render(request,'home.html',{'name':'Ana Sofia A.M'})

def About(request):
    #return HttpResponse('<center><h1>Welcome to About Page :)</h1><center>')
    return render(request,'about.html',{'name':'Ana Sofia A.M'})

# Create your views here.S
