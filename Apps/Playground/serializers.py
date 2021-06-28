from rest_framework import serializers

from .models import Room


class PlaygroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['roomId']
    
    def save(self):
        newRoom = Room(
            roomId = self.validated_data['roomId']
        )

        newRoom.players.add(self.context['request'].user)
        
        
        newRoom.save()
        return newRoom