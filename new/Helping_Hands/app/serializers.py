from rest_framework import serializers


from .models import Users_donations
# class SignUpSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email','options','gender']

# class SetPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'passcode', 'password']
    

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

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