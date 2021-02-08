from django.db import models
from django.contrib.auth.models import AbstractUser


class Mood(models.Model):

    mood_name = models.CharField(max_length=50)
    mood_des = models.CharField(max_length=150, default="This is a Dummy Mood!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.mood_name


class Genre(models.Model):

    genre_name = models.CharField(max_length=50)
    genre_des = models.CharField(max_length=150, default="This is a Popular Genre!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.genre_name



class Artist(models.Model):

    artist_name = models.CharField(max_length=50)
    artist_des = models.CharField(max_length=150, default="A Popular Artist!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.artist_name


class Song(models.Model):

    song_name = models.CharField(max_length=50)
    song_des = models.CharField(max_length=150, default="This is a Popular Song!")

    song_length = models.CharField(max_length=10)

    #song_file = models.FileField(upload_to='songs/')

    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    mood_name = models.ForeignKey(Mood, on_delete=models.CASCADE)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.song_name


class CustomUser(AbstractUser):

	name = models.CharField(max_length=20, default='UserName')

	email = models.EmailField(max_length=254, unique=True)

	username = None

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []

	usr_phone = models.CharField(max_length=20)

	usr_gender = models.CharField(max_length=10)


# Create your models here.
class playlist_user(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return f'Username = {self.username}, Liked Songs = {list(self.playlist_song_set.all())}'


class playlist_song(models.Model):
    user = models.ForeignKey(playlist_user, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    song_youtube_id =  models.CharField(max_length=20)
    song_albumsrc = models.CharField(max_length=255)
    song_dur = models.CharField(max_length=7)
    song_channel = models.CharField(max_length=100)
    song_date_added = models.CharField(max_length=12)

    def __str__(self):
      return f'Title = {self.song_title}, Date = {self.song_date_added}'
