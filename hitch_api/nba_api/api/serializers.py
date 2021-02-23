from rest_framework import serializers
from nba_api.models import Team, College, Position, Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

    def to_representation(self, instance):
        college = instance.college.name if instance.college else None
        return {
            'id': instance.id,
            'full_name': instance.full_name,
            'team': instance.team.name,
            'number': instance.number,
            'position': instance.position.position,
            'age': instance.age,
            'height': instance.height,
            'weight': instance.weight,
            'college': college,
            'salary': instance.salary
        }


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
