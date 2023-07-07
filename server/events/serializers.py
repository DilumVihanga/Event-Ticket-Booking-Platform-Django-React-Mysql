from rest_framework import serializers
from .models import Event, Admin, Organizer, User   

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'          


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'        