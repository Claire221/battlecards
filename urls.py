
from django.urls import path
from . import views

app_name = 'battlecards'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('select/card/<int:card_id>/', views.select_card, name='select_card'),
]
