from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

def home(request):
   # return HttpResponse('<center><h1>Welcome to Home Page :)</h1><center>')
   #return render (request,'home.html')
   #return render(request,'home.html',{'name':'Ana Sofia A.M'})
   searchTerm= request.GET.get('searchMovie')
   if searchTerm:
    movies= Movie.objects.filter(title__icontains=searchTerm)
   else:
    movies= Movie.objects.all()
   return render(request,'home.html', {'searchterm':searchTerm, 'movies':movies})


def About(request):
    #return HttpResponse('<center><h1>Welcome to About Page :)</h1><center>')
    return render(request,'about.html',{'name':'Ana Sofia A.M'})

# Create your views here.S
