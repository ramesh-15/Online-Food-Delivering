from .models import Users_donations
from rest_framework import serializers
from .models import * #User,ApplicantsModel,MedicalCamp_event,Bloodcamp_event


class McampSerializer(serializers.ModelSerializer):
    class Meta:
        model =MedicalCamp_event
        fields = '__all__'

    def validate(self, data):
        Organiser_name = data.get('Organiser_name')
        place = data.get('place')
        city = data.get('city')
        if len(Organiser_name) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact_no(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value

class Bloodcamp_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Bloodcamp_event
        fields = '__all__'
    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value
class SCampserializer(serializers.ModelSerializer):
    class Meta:
        model =ForScribersModel
        fields = '__all__'

    def validate(self, data):
        Scribename = data.get('Scribename')
        place = data.get('place')
        city = data.get('city')
        if len(Scribename) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class AnimalCampSerializer(serializers.ModelSerializer):
    class Meta:
        model =AnimalCampModel
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value

class CB_Event_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model =CBEmodel
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value

class Educational_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Educational_event
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value




























class McampSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCamp_event
        fields = '__all__'

    def validate(self, data):
        Organiser_name = data.get('Organiser_name')
        place = data.get('place')
        city = data.get('city')
        if len(Organiser_name) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact_no(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class Bcampserializer(serializers.ModelSerializer):
    class Meta:
        model = Bloodcamp_event
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class Ecampserializer(serializers.ModelSerializer):
    class Meta:
        model = Educational_event
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class CBEserializer(serializers.ModelSerializer):
    class Meta:
        model = CBEmodel
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class ACampserializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalCampModel
        fields = '__all__'

    def validate(self, data):
        Organisername = data.get('Organisername')
        place = data.get('place')
        city = data.get('city')
        if len(Organisername) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class SCampserializer(serializers.ModelSerializer):
    class Meta:
        model = ForScribersModel
        fields = '__all__'

    def validate(self, data):
        Scribename = data.get('Scribename')
        place = data.get('place')
        city = data.get('city')
        if len(Scribename) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(place) < 3:
            raise serializers.ValidationError('Place should be at least 3 characters long')
        if data['camp_starts_at'] == data['camp_ends_at']:
            raise serializers.ValidationError('End time must be after start time.')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value


class APCampserializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantsModel
        fields = '__all__'

    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        state = data.get('state')

        if len(name) <= 2:
            raise serializers.ValidationError("Given chars should be morethan 2")
        if len(city) < 3:
            raise serializers.ValidationError('City should be at least 3 characters long')
        if len(state) < 3:
            raise serializers.ValidationError('State should be at least 3 characters long')
        return data

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should be numeric.")
        if len(value) != 10:
            raise serializers.ValidationError("Contact number should be 10 digits.")
        return value

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Enter proper Email(should be end with @gmail.com)")
        return value