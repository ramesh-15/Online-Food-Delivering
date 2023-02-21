from .models import Users_donations
from rest_framework import serializers
from .models import User

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = "__all__"

class UserSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','username','email']