from django.shortcuts import render
from django.http import HttpResponse
from .models import Vinyl
# Create your views here.

# vinyl_albums = ['12" of the month club: nofx', 'the decline on clear vinyl: nofx']
# class Vinyl:  
#   def __init__(self, name, artist, year, description):
#     self.name = name
#     self.artist = artist
#     self.year = year
#     self.description = description

# vinyl = [
#   Vinyl('HOFX', 'nofx', 1995, 'marble vinyl EP'),
#   Vinyl('The Decline', 'nofx', 1999, 'clear-vinyl EP'),
#   Vinyl('Days of Rage', 'the rebel spell', 2007, 'black vinyl LP')
# ]


def home(request):
  vinyl = Vinyl.objects.all()
  return render(request,'index.html', {'vinyl': vinyl})

def about(request):
  return render(request, 'about.html')

def vinyl_details(request, vinyl_id):
  found_vinyl = Vinyl.objects.get(id=vinyl_id)
  return render(request, 'vinyls/details.html', {
    'vinyl': found_vinyl
  })
