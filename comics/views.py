from django.shortcuts import render
from .models import Comic

def index(request):
    comics = Comic.objects.all()
    return render(request, 'comics/index.html', {'comics': comics})

