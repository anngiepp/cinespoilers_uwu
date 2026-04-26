from django.db import models

# NUEVO
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duración en minutos")
    created_at = models.DateTimeField(auto_now_add=True)

    # NUEVO
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title