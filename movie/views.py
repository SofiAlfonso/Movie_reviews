from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import matplotlib.pyplot as plt # type: ignore
import matplotlib.pyplot as plt2 # type: ignore
import matplotlib # type: ignore
import io
import urllib, base64


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
def signup(request):
   email= request.GET.get("email")
   return render (request, 'signup.html', {'email':email})

def statistics_view(request):
    matplotlib.use('Agg')
    all_movies = Movie.objects.all()

    movie_counts_by_year = {}
    movie_counts_by_genre={}

    for movie in all_movies:
        genre = movie.genre if movie.genre else "None"
        genre= genre.split(',')[0] #Tomamos sólo el primer género 
        if genre in movie_counts_by_genre:
            movie_counts_by_genre[genre] += 1
        else:
            movie_counts_by_genre[genre] = 1
    
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    #Gráfica 1
    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_year))
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)


    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    #Gráfica 2
    bar_positions2 = range(len(movie_counts_by_genre))
    plt.bar(bar_positions2, movie_counts_by_genre.values(), width=bar_width, align='center')
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions2, movie_counts_by_genre.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    plt.close()

    image_png2 = buffer2.getvalue()
    buffer2.close()
    graphic2 = base64.b64encode(image_png2).decode('utf-8')

    both = {'graphic': graphic, 'graphic2': graphic2}
    return render(request, 'statistics.html', both)

