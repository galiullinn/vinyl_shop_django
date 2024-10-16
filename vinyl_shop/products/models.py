from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artist_image', null=True, blank=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artist_image', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Album(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    year_release = models.DateField()
    image = models.ImageField(upload_to='album_image', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    label = models.ForeignKey(to=Label, on_delete=models.CASCADE)
    artist = models.ManyToManyField(to=Artist)
    genre = models.ManyToManyField(to=Genre)

    def __str__(self):
        genres_names = ", ".join([genre.name for genre in self.genres.all()])
        return f"{self.title} - {genres_names} by {self.artist.name}"
    

class Track(models.Model):
    title = models.CharField(max_length=256)
    duration = models.TimeField()
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.album.title}"
