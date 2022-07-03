from django.db import models


class Actor(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(max_length=10, choices=CHOICES)
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
