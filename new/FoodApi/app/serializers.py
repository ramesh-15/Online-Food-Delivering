from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import DonarUser,Users_donations,LoginDetials
from django.contrib.auth.models import User


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
#     # def update(self,validated_data):


# class FoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users_donations
#         fields = ['name','food_type','quantity','exp','pick_up','contact']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonarUser
        fields = ['username', 'new_password']

class SetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonarUser
        fields = ['username', 'passcode','new_password','confirm_password']
    

# class DonateFoodSerializer(serializers.ModelSerializer):
#     # donar_name = serializers.CharField(allow_null=True, required=False)
#     class Meta:
#         model = Users_donations
    
class FoodSerializer(serializers.ModelSerializer):
    # donar_name = serializers.CharField(allow_null=True, required=False)
    class Meta:
        model = Users_donations
        fields = ['name','food_type','quantity','exp','pick_up','contact','pincode' ]

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user, 'requestdata ......')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = ['name','quantity','exp','contact','pick_up','pincode']  
    def create(self,validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
class FootwearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = ['name','quantity','exp','contact','pick_up','pincode']  
    def create(self,validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
class StationarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = ['name','quantity','exp','contact','pick_up','pincode']  
    def create(self,validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = ['name','quantity','exp','contact','pick_up','pincode']  
    def create(self,validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
    
class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = ['name','quantity','exp','contact','pick_up','pincode']  
    def create(self,validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        instance.donar_name = request.user
        instance.save()
        return instance
# class DonarCartSerializer(serializers.ModelSerializer):
#     status = serializers.CharField()
#     class Meta:
#         model = Users_donations
#         fields = ['id', 'food_name','food_type','quantity']

# Authentication
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonarUser
        fields = "__all__"


# userprofile
class ViewProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name','last_name','username','email']

class ProfileUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name','last_name','username','email']

