from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Room


@api_view(['POST',])
def createRoom(request):
    pass