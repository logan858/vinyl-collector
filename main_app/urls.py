from django.urls import path
from . import views
from main_app.views import VinylList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<int:vinyl_id>/', views.vinyl_details, name="details"),
    path('<int:vinyl_id>/delete/', views.vinyl_delete, name="delete"),
    path('<int:vinyl_id>/edit/', views.vinyl_edit, name="edit"),
    path('<int:vinyl_id>/edit/submit/', views.vinyl_submit, name="submit"),
    path('create/', views.create, name="create"),
    path('create/submit/', views.create_submit, name="create_submit"),
    path('<int:vinyl_id>/add_listen/', views.add_listen, name="add_listen"),
]