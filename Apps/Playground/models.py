from django.db import models
from Apps.User.models import User

class Room(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner', null = True, blank=True)
    roomId = models.CharField(max_length=20)
    players = models.ManyToManyField(User, related_name='players')
    mafias = models.ManyToManyField(User, related_name='mafias')
    detective = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detective', null=True, blank=True)
    doctor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor', null=True, blank=True)
    city = models.ManyToManyField(User, related_name='city')
    isFilled = models.BooleanField(default=False)
    isStarted = models.BooleanField(default=False)
    winner = models.CharField(max_length=10)
    noOfPlayers = models.IntegerField(null=True, blank=True)