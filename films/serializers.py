from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from films.models import Actor, Movie, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, value):
        if value.year < 1950:
            raise ValidationError(detail='Year must be higher than 1950')
        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "movie_id", "text", "created_date")
