
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mood, Genre, Artist, Song

# Create your views here.
def index(request):
    latest_Song_list = Song.objects.order_by('-updated_at')[:5]
    output = ', '.join([s.song_name for s in latest_Song_list])
    return HttpResponse(output)