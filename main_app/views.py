from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vinyl
from django.views.generic import ListView
from .forms import ListenForm
# Create your views here.

class VinylList(ListView):
    model = Vinyl

def home(request):
  vinyl = Vinyl.objects.all()
  return render(request,'index.html', {'vinyl': vinyl})

def about(request):
  return render(request, 'about.html')

def vinyl_details(request, vinyl_id):
  found_vinyl = Vinyl.objects.get(id=vinyl_id)
  listen_form = ListenForm()
  return render(request, 'vinyls/details.html', {
    'vinyl': found_vinyl,
    'listen_form': listen_form,
  })

def vinyl_delete(request, vinyl_id):
  found_vinyl = Vinyl.objects.get(id=vinyl_id)
  found_vinyl.delete()
  return redirect("/")
  
def vinyl_edit(request, vinyl_id):
  found_vinyl = Vinyl.objects.get(id=vinyl_id)
  return render(request, 'vinyls/edit.html', {
    'vinyl': found_vinyl,
  })

def vinyl_submit(request, vinyl_id):
  found_vinyl = Vinyl.objects.get(id=vinyl_id)
  print(found_vinyl)
  found_vinyl.title = request.POST["title"]
  found_vinyl.artist = request.POST["artist"]
  found_vinyl.release = request.POST["release"]
  found_vinyl.description = request.POST["description"]
  found_vinyl.save()
  return redirect(f'/{vinyl_id}/')

def create(request):
  return render(request, "vinyls/create.html")

def create_submit(request):
  vinyl = Vinyl.objects.all()
  Vinyl.objects.create(
    title=request.POST["title"],
    artist=request.POST["artist"],
    release=request.POST["release"],
    description=request.POST["description"],
  )
  return redirect('/')

def add_listen(request, vinyl_id):
  form = ListenForm(request.POST)
  if form.is_valid():
    new_listen = form.save(commit=False)
    new_listen.vinyl_id = vinyl_id
    new_listen.save()
  return redirect(f"/{vinyl_id}", vinyl_id=vinyl_id)