from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    movie_id = models.ForeignKey('films.Movie', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='com')
    text = models.TextField()
    created_date = models.DateField()

    def __str__(self):
        return self.text
