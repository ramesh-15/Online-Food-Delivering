from .models import Users_donations
from rest_framework import serializers
from .models import DonarUser,Users_donations

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = "__all__"

class UserSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = DonarUser
        fields = ['first_name','last_name','username','email','city','state']