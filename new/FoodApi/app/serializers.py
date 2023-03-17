from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import DonarUser,Users_donations


# User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DonarUser
        fields = [ 'first_name', 'last_name','username','email', 'city','state','passcode']

    def create(self, validated_data):
        user = DonarUser.objects.create(
            email=validated_data['email'],
            state=validated_data['state'],
            city=validated_data['city'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data.get('username'),
            passcode=validated_data.get('passcode'),

        )
        return user
    # def update(self,validated_data):


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    passcode = serializers.CharField()

    def validate(self, data):
      
        username = data.get('username')
        passcode = data.get('passcode')
        # print(email,' ',password)

        if username and passcode:

            user = authenticate(username=username, passcode=passcode)
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

