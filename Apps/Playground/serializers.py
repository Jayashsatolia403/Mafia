from rest_framework import serializers

from .models import Room


class PlaygroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['roomId']
    
    def save(self):
        newRoomId = self.validated_data['roomId']

        try:
            Room.objects.get(roomId=newRoomId)
            return "Room Already Exists"
            
        except:
            newRoom = Room(
                roomId = newRoomId
            )

            newRoom.players.add(self.context['request'].user)
            newRoom.owner = self.context['request'].user
            
            
            newRoom.save()
            return newRoom