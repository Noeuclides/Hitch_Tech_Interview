from rest_framework import serializers
from nba_api.models import Team, College, Position, Player

class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    college = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = '__all__'

class PlayerCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'