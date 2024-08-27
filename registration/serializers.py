from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'create_login', 'password', 'repet_password', 'phone', 'email',]




        def validate(self, data):
            if data['password'] != data['repet_password']:
                raise serializers.ValidationError("Пароли не совподают")
            return data