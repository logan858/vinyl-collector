from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<int:vinyl_id>/', views.vinyl_details, name="details")
]