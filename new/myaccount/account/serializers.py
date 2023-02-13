from .models import Users_donations
from rest_framework import serializers

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_donations
        fields = "__all__"