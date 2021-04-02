from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vinyl, StoreTwo
from django.views.generic import ListView
from .forms import ListenForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class VinylList(ListView):
    model = Vinyl

@login_required
def home(request):
  # vinyl = Vinyl.objects.all()
  vinyl = request.user.vinyl_set.all()
  return render(request,'index.html', {'vinyl': vinyl})

def about(request):
  return render(request, 'about.html')

def vinyl_details(request, vinyl_id):
  found_vinyl = Vinyl.objects.get(id=vinyl_id)
  listen_form = ListenForm()
  stores_not_carrying_vinyl = StoreTwo.objects.exclude(id__in = found_vinyl.stores.all().values_list('id'))
  print(stores_not_carrying_vinyl)
  return render(request, 'vinyls/details.html', {
    'vinyl': found_vinyl,
    'listen_form': listen_form,
    'stores_not_carried': stores_not_carrying_vinyl,
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

@login_required
def create(request):
  return render(request, "vinyls/create.html")

@login_required
def create_submit(request):
  vinyl = Vinyl.objects.all()
  Vinyl.objects.create(
    title=request.POST["title"],
    artist=request.POST["artist"],
    release=request.POST["release"],
    description=request.POST["description"],
    user=request.user,
  )
  return redirect('/')

def add_listen(request, vinyl_id):
  form = ListenForm(request.POST)
  if form.is_valid():
    new_listen = form.save(commit=False)
    new_listen.vinyl_id = vinyl_id
    new_listen.save()
  return redirect(f"/{vinyl_id}", vinyl_id=vinyl_id)

def assoc_store(request, vinyl_id, store_id):
  Vinyl.objects.get(id=vinyl_id).stores.add(store_id)
  return redirect(f'/{vinyl_id}')

def stores(request):
  stores = StoreTwo.objects.all()
  return render(request, 'stores.html', {
    'stores': stores,
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)