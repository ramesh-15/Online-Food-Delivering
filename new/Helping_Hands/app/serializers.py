from rest_framework import serializers
from .models import MyUser,Users_donations


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name','username','options','gander' , 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
    
class SignUpVol(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name','username','AreaOfInterest','options','gander' , 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name','username','options','gendar' ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if MyUser.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if MyUser.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance       

# Donations
    
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
    
#profile
# class ViewProfile(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields =['first_name','last_name','username','email']