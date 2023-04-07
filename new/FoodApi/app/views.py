from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import LoginSerializer, SignUpSerializer,FoodSerializer
from .models import DonarUser,Users_donations
from django.contrib.auth import login
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail
import random
import string
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Q

def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password

class SignUpView(generics.CreateAPIView):
    queryset = DonarUser.objects.all()
    serializer_class = SignUpSerializer
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        otp = passcode()
        data['passcode'] = otp
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Add this line to save the record
    
        # smtp passcode
        subject = 'Passcode Verification code'
        message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        sender = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender, [data['email']])
        
        return Response({'success': 'Registration Successful !!!'}, status=status.HTTP_200_OK)




class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        passcode = request.data.get('passcode')
        print('data:',username,passcode)
        if not username or not passcode:
            return Response({'error': 'Please provide both email and passcode'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = DonarUser.objects.get(username=username, passcode=passcode)

        if not user:
            return Response({'error': 'Invalid email or passcode'}, status)
        else:
            return Response({"success":'login successful...'})
        
class DonationFood(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class DonationFood(GenericAPIView,ListModelMixin,CreateModelMixin):
#     permission_classes = [IsAuthenticated]
#     queryset = Users_donations.objects.all()
#     serializer_class = FoodSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         print("into generic:",request.user)
#         return self.create(request,*args,**kwargs)
    
# class DonationGet(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

        


# Donar 
# class Donation(APIView):
#     permissions = [IsAuthenticated]
#     def get(self,request,pk=None,format=None):
#         id = request.data.get('id')
#         if id:
#             obj = Food.objects.get(id = id)
#             serializer = FoodSerializer(obj)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         obj = Food.objects.all()
#         serializer = FoodSerializer(obj,many = True)
#         return Response(serializer.data,status = status.HTTP_200_OK)

#     def post(self,request,format=None):
#         serializer = FoodSerializer(data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'food Donated successfully ...'}
#             return Response(res,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# # class DonarFoodView(ModelViewSet):
# #     queryset = Users_donations.objects.all()
# #     serializer_class = DonateFoodSerializer
# #     authentication_classes = [SessionAuthentication]
# #     # permission_classes = [IsDonarUserAuthenticated]

# #     def create(self, request, *args, **kwargs):
# #         data = request.data
# #         serializer = self.serializer_class(data=data, context={'request': request})
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)




class DonarCart(ModelViewSet):
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # print(request.user)
    queryset = Users_donations.objects.filter( )

