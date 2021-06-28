from django.db import models
from Apps.User.models import User

class Room(models.Model):
    roomId = models.CharField(max_length=20)
    players = models.ManyToManyField(User)
    isFilled = models.BooleanField(default=False)
    isStarted = models.BooleanField(default=False)
    winner = models.CharField(max_length=10)