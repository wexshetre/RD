from django.contrib import admin
from .models import Mood, Genre, Artist, Song


admin.site.register(Mood)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
