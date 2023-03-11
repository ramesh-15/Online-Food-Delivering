from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import User,Users_donations

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'password', 'first_name', 'last_name','is_Donar','is_NGO']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_Donar=validated_data.get('is_Donar', ''),
            is_NGO=validated_data.get('is_NGO', ''),
            username=validated_data.get('username'),


        )
        return user
    # def update(self,validated_data):


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
      
        username = data.get('username')
        password = data.get('password')
        # print(email,' ',password)

        if username and password:

            user = authenticate(username=username, password=password)
            print(user)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                data['user'] = user
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return data
    
class DonateFoodSerializer(serializers.ModelSerializer):
    # donar_name = serializers.CharField(allow_null=True, required=False)
    class Meta:
        model = Users_donations
        fields = ['food_name','food_type','quantity','donar_contact','food_pick_up','pincode', ]

    def create(self, validated_data):
        request = self.context.get('request')
        print(request, 'requestdata......')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
    

class DonarCartSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    class Meta:
        model = Users_donations
        fields = ['id', 'food_name','food_type','quantity', 's']

