from rest_framework import serializers
from .models import Movie, Genre  # CAMBIO
from datetime import date

# NUEVO
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    # NUEVO
    genres = GenreSerializer(many=True, read_only=True)

    # NUEVO
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source='genres'
    )

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("El título es demasiado corto.")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("La duración debe ser mayor a 0.")
        return value

    def validate_release_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha no puede ser futura.")
        return value