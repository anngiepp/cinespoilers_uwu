from django.contrib import admin
from .models import Movie, Genre  # CAMBIO

# IMPORTANTE
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration')
    filter_horizontal = ('genres',)  # NUEVO


# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)