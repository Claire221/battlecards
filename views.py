from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache



@never_cache
def home(request, template="battlecards/home.html"):
    print("home")
    return render(request, template)
    
