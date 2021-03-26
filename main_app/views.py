from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

vinyl_albums = ['12" of the month club: nofx', 'the decline on clear vinyl: nofx']
class Vinyl:  
  def __init__(self, name, artist, year, description):
    self.name = name
    self.artist = artist
    self.year = year
    self.description = description

vinyl = [
  Vinyl('HOFX', 'nofx', 1995, 'marble vinyl EP'),
  Vinyl('The Decline', 'nofx', 1999, 'clear-vinyl EP'),
  Vinyl('Days of Rage', 'the rebel spell', 2007, 'black vinyl LP')
]


def home(request):
  return render(request,'index.html', {'vinyl': vinyl})

def about(request):
  return render(request, 'about.html')