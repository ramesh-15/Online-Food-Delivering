from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics,status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from .utils import get_tokens_for_user
from .models import Users_donations,MyUser
from .serializers import  GadgetSerializer,FoodSerializer,HealthSerializer,ClothesSerializer,FootwearSerializer,StationarySerializer
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework_simplejwt.exceptions import InvalidToken,AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from django.core.mail import send_mail
import random
import string
# # Create your views here.
from .serializers import SignUpSerializer,LoginSerializer,ChangePasswordSerializer,UpdateUserSerializer,SignUpVol,DonationSerializer

def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password

class SignUpView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = SignUpSerializer
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Add this line to save the record

        # Update the roles field based on the is_Donar flag
        
        # user.objects.filter(pk=user.pk ).update( AreaOfInterest='True')  # Add this line to save the record
     
    
        # smtp passcode
        # subject = 'Passcode Verification code'
        # message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        # sender = settings.EMAIL_HOST_USER
        # send_mail(subject, message, sender, [data['email']])
        
        return Response({'success': 'Registration Successful !!!'}, status=status.HTTP_200_OK)


# volunteer
class SignUpViewVol(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = SignUpVol
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Add this line to save the record

        # Update the roles field based on the is_Donar flag
        
        # user.objects.filter(pk=user.pk ).update( AreaOfInterest='True')   # Add this line to save the record
     
    
        # smtp passcode
        # subject = 'Passcode Verification code'
        # message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        # sender = settings.EMAIL_HOST_USER
        # send_mail(subject, message, sender, [data['email']])
        
        return Response({'success': 'Registration Successful !!!'}, status=status.HTTP_200_OK)


class LoginView(generics.CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ChangePasswordView(generics.UpdateAPIView):

    queryset = MyUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer       


class UpdateProfileView(generics.UpdateAPIView):

    queryset = MyUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
   

class LogoutView(generics.CreateAPIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
# Donations

class DonationFood(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'food donated Successful !!!'}, status=status.HTTP_200_OK)



class DonationClothes(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = ClothesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Clothes donated Successful !!!'}, status=status.HTTP_200_OK)


class DonationFootwear(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = FootwearSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'footwear donated Successful !!!'}, status=status.HTTP_200_OK)


class DonationStationary(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = StationarySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'stationary donated Successful !!!'}, status=status.HTTP_200_OK)

class DonationGadget(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = GadgetSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'gadget donated Successful !!!'}, status=status.HTTP_200_OK)

class DonationHealth(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = HealthSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        # otp = passcode()
       
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'health donated Successful !!!'}, status=status.HTTP_200_OK)


class DonarHistory(generics.RetrieveAPIView):
    queryset = Users_donations.objects.all()
    serializer_class = DonationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        print(user)
        queryset = Users_donations.objects.filter(donar_name=user)
        print(queryset)
        return queryset
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)


  

#profile

# class DonorProfile(generics.RetrieveAPIView):
#     serializer_class = ViewProfile
#     permission_classes = (IsAuthenticated,)

#     def get_object(self):
#         return self.request.user


# admin 

from .models import MedicalCamp_event,Bloodcamp_event,Educational_event,CBEmodel,AnimalCampModel,ForScribersModel
from .serializers import McampSerializer,BloodSerializer,EducationSerializer,CBESerializer,AnimalSerializer,ScribeSerializer
from rest_framework.permissions import IsAdminUser

class MedicalCamp(generics.CreateAPIView):
    queryset = MedicalCamp_event.objects.all()
    serializer_class = McampSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        print(request.data, 'inside post')     
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Registered  Successfully for Medical Camp !!!'}, status=status.HTTP_200_OK)
    
class BloodCamp(generics.CreateAPIView):
    queryset = Bloodcamp_event.objects.all()
    serializer_class = BloodSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        print(request.data, 'inside post')     
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Registered  Successfully for Blood Camp !!!'}, status=status.HTTP_200_OK)

class EducationCamp(generics.CreateAPIView):
    queryset = Educational_event.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        print(request.data, 'inside post')     
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Registered  Successfully for Education Camp !!!'}, status=status.HTTP_200_OK)

class CBECamp(generics.CreateAPIView):
    queryset = CBEmodel.objects.all()
    serializer_class = CBESerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        print(request.data, 'inside post')     
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Registered  Successfully for Community Build  Camp !!!'}, status=status.HTTP_200_OK)
    
class AnimalCamp(generics.CreateAPIView):
    queryset = AnimalCampModel.objects.all()
    serializer_class = AnimalSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        print(request.data, 'inside post')     
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Registered  Successfully for Animal Camp !!!'}, status=status.HTTP_200_OK)

class ScribesCamp(generics.CreateAPIView):
    queryset = ForScribersModel.objects.all()
    serializer_class = ScribeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        print(request.data, 'inside post')     
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': 'Registered  Successfully for Animal Camp !!!'}, status=status.HTTP_200_OK)
    
