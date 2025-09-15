
from django.urls import path
from . import views

app_name = 'battlecards'

urlpatterns = [
    path('home/', views.home, name='home'),
]
