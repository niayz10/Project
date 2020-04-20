from rest_framework import serializers

from user.models import User, Skill


class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.CharField()
    email = serializers.CharField()
    gender = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'name', 'availability', 'reviews', 'email', 'gender', 'age', 'skill', 'status', 'rait')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'description', 'category', 'raiting', 'status')
