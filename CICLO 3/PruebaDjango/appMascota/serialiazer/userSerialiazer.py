from rest_framework import serializers
from appMascota.models import  User


class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model  = User
    fields = ['id', 'username', 'password', 'name', 'email']

  #recibe un json y lo convierte a objetos
  def create(self, validated_data):
    userInstance = User.objects.create(**validated_data)
    return userInstance

  #recibe un objeto y lo convierte a json
  def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email
      
      }