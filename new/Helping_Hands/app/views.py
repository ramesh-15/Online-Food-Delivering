from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics,status

from .models import Users_donations
from .serializers import  GadgetSerializer,FoodSerializer,HealthSerializer,ClothesSerializer,FootwearSerializer,StationarySerializer
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission
from django.conf import settings
from django.core.mail import send_mail
import random
import string
# # Create your views here.
# from .serializers import SignUpSerializer

# def passcode():
#     characters = string.ascii_letters + string.digits
#     password = ''.join(random.choice(characters) for i in range(6))
#     print("Random password is:", password)
#     return password

# class SignUpView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SignUpSerializer
    
#     def post(self, request):
#         print(request.data, 'inside post')
        
#         data = request.data.copy()
#         otp = passcode()
       
        
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         user=serializer.save()  # Add this line to save the record

#         # Update the roles field based on the is_Donar flag
        
#         User.objects.filter(pk=user.pk ).update(passcode=otp)  # Add this line to save the record
     
    
        # smtp passcode
        # subject = 'Passcode Verification code'
        # message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        # sender = settings.EMAIL_HOST_USER
        # send_mail(subject, message, sender, [data['email']])
        
        # return Response({'success': 'Registration Successful !!!'}, status=status.HTTP_200_OK)
    
# class SetPassword(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SetPasswordSerializer
#     def put(self, request):
#         name = request.data.get('username')
#         passcode = request.data.get('passcode')
#         print(request.user)
#         print(name,passcode)
#         obj = User.objects.get(username=name)
#         print(obj)
#         # serializer = SetPasswordSerializer(obj, data=request.data, partial=True)
#         serializer = self.get_serializer(obj,data=request.data,partial = True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
      
#             return Response({"success":'password setup successful...'}, status=status.HTTP_201_CREATED)
#         return Response({"error":'password not setup ...'}, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(generics.CreateAPIView):
   
#     serializer_class = LoginSerializer

#     def post(self, request):
#         print(request.data)
#         username = request.data.get('username')
#         password = request.data.get('password')
#         print('data:',username,password)
#         if not username or not password:
#             return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        
#         user = User.objects.get(username=username, password=password)
#         print('user:->',user)
#         if not user:
#             return Response({'error': 'Invalid email or passcode'}, status)
#         else:
#             return Response({"success":'login successful...'})
        

# Donations

class DonationFood(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DonationClothes(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = ClothesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DonationFootwear(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = FootwearSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DonationStationary(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = StationarySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DonationGadget(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = GadgetSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DonationHealth(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = HealthSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class History(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = HealthSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method \"POST\" not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




#profile

# class DonorProfile(generics.RetrieveAPIView):
#     serializer_class = ViewProfile
#     permission_classes = (IsAuthenticated,)

#     def get_object(self):
#         return self.request.user
