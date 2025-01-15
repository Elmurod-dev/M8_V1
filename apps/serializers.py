from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from apps.models import CustomUsers, Post


# Homework

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = ('id', 'username','password', 'email')

    def create(self, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




