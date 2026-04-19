from rest_framework import serializers
from .models import Movie
from datetime import date

class MovieSerializer(serializers.ModelSerializer):
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