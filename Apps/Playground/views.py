from rest_framework.decorators import api_view

from .models import Room
from Apps.User.models import User
from .serializers import PlaygroundSerializer

import random

avilableRoles = ['Detective', 'Doctor', 'Mafia', 'Mafia', 'Citizen', 'Citizen', 'Citizen', 'Mafia', 'Mafia', 'Citizen', 'Citizen', 'Citizen', 'SuicideBomber']


@api_view(['POST',])
def createRoom(request):
    serializer = PlaygroundSerializer(data=request.data, context={'request':request})
    if serializer.is_valid():
        serializer.save()
    else:
        return {serializer.errors}
    return "Room Created Successfully"

@api_view(['POST',])
def joinRoom(request, roomId):
    user = request.user
    room = Room.objects.get(roomId=roomId)
    room.players.add(user)
    return "Joined"

@api_view(['POST',])
def leaveRoom(request, roomId):
    user = request.user
    user.isActive = False
    user.role = ""
    room = Room.objects.get(roomId=roomId)
    room.players.remove(user)
    return "Left"

@api_view(['GET',])
def noOfPlayersInRoom(request, roomId):
    room = Room.objects.get(roomId=roomId)
    return len(room.players)

@api_view(['GET',])
def noOfMafiasInRoom(request, roomId):
    room = Room.objects.get(roomId=roomId)
    return len(room.mafias)

@api_view(['GET',])
def noOfCityInRoom(request, roomId):
    room = Room.objects.get(roomId=roomId)
    return len(room.city)

@api_view(['GET',])
def hasGameEnded(request, roomId):
    room = Room.objects.get(roomId=roomId)
    return len(room.city)-len(room.mafias) < 1

@api_view(['GET',])
def isDoctorAlive(request, roomId):
    room = Room.objects.get(roomId=roomId)
    if room.doctor != None:
        return True
    return False

@api_view(['GET',])
def isDetectiveAlive(request, roomId):
    room = Room.objects.get(roomId=roomId)
    if room.detective != None:
        return True
    return False

@api_view(['GET',])
def killSomeone(request, userId, roomId):
    room = Room.objects.get(roomId=roomId)
    user = User.objects.get(id=userId)
    user.isKilled = True
    return "{} Killed".format(user.username)

@api_view(['GET',])
def saveSomeone(request, userId, roomId):
    room = Room.objects.get(roomId=roomId)
    user = User.objects.get(id=userId)
    
    if user.isKilled == True:
        user.isKilled = False
    else:
        for player in room.players:
            if player.isKilled == True:
                room.players.remove(player)
                
                if player.role == "Mafia":
                    room.mafias.remove(player)
                elif player.role == "Detective":
                    room.detective = None
                    room.city.remove(player)
                elif player.role == "Doctor":
                    room.doctor = None
                    room.city.remove(player)
                else:
                    room.city.remove(player)
                
                player.role = ""
                player.isActive = False
                player.isKilled = False
                break

    return "{} Saved".format(user.username)



@api_view(['GET',])
def voteOut(request, userId, roomID):
    room = Room.objects.get(roomId=roomID)
    user = User.objects.get(id=userId)
    room.players.remove(user)

    if user.role == "Mafia":
        room.mafias.remove(user)
    elif user.role == "Detective":
        room.detective = None
        room.city.remove(user)
    elif user.role == "Doctor":
        room.doctor = None
        room.city.remove(user)
    else:
        room.city.remove(user)
    
    user.role = ""
    user.isActive = False




@api_view(['POST',])
def startGame(request, roomId):
    global avilableRoles
    user = request.user
    room = Room.objects.filter(roomId=roomId)

    if user == room.owner:
        players = room.players
        room.isFilled = True
        room.isStarted = True


        random.shuffle(players)

        room.detective = players[0]
        room.doctor = players[1]

        for i in range(len(players)):
            players[i].role = avilableRoles[i]
            players[i].isActive = True

            if avilableRoles[i] == 'Mafia':
                room.mafias.add(players[i])
            else:
                room.city.add(players[i])

    else:
        return "Only Owner Can Start Game"
    
    return "Game Started"