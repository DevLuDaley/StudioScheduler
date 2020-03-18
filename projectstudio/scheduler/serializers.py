from rest_framework import serializers

from scheduler.models import Artist, Studio, Engineer, Session


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = ['name', 'location']
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        # fields = ('appointment_date', 'status', 'duration', 'studio', 'artist', 'engineer'
        #          )
        fields = '__all__'
