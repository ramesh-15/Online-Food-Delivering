from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import LoginSerializer,SetPasswordSerializer,SetPasswordSerializer,AuthSerializer, GadgetSerializer,SignUpSerializer,FoodSerializer,HealthSerializer,ClothesSerializer,FootwearSerializer,StationarySerializer
from .models import DonarUser,Users_donations,LoginDetials
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission
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
    queryset = User.objects.all()
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
        # subject = 'Passcode Verification code'
        # message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        # sender = settings.EMAIL_HOST_USER
        # send_mail(subject, message, sender, [data['email']])
        
        return Response({'success': 'Registration Successful !!!'}, status=status.HTTP_200_OK)



class LoginView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('new_password')
        print('data:',username,passcode)
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(username=username, new_password=password)
        print('user:->',user)
        if not user:
            return Response({'error': 'Invalid email or passcode'}, status)
        else:
            return Response({"success":'login successful...'})

#main login for all
class SetPassword(APIView):
    def put(self, request):
        name = request.data.get('username')
        passcode = request.data.get('passcode')
        print(request.user)
        print(name,passcode)
        obj = DonarUser.objects.get(username=name)
        print(obj)
        serializer = SetPasswordSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":'password setup successful...'}, status=status.HTTP_201_CREATED)
        return Response({"error":'password not setup ...'}, status=status.HTTP_400_BAD_REQUEST)

#custome permissions
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.username == request.data.get('username') and \
           user.password == request.data.get('new_password'):
            return True
        return False

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


#authentication
# class DonorAuthenticate():
#     def post(self, request):
#         print(request.data)
#         username = request.data.get('username')
#         password = request.data.get('new_password')
#         print('data:',username,passcode)
#         if not username or not password:
#             return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        
#         user = DonarUser.objects.get(username=username, new_password=password)
#         print('user:->',user)
#         if not user:
#             return Response({'error': 'Invalid email or passcode'}, status)
#         else:
#             LoginDetials['username']=username
#             LoginDetials.save()
#             return Response({"success":'Authentication successful...'})

# User Profile

from .serializers import ViewProfile,ProfileUpdate
class DonorProfile(generics.RetrieveAPIView):
    serializer_class = ViewProfile
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
    

class ProfileUpdate(generics.UpdateAPIView):
    serializer_class = ProfileUpdate
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        # logout the user and clear their session data
        request.session.flush()
        return Response({"message": "Logout successful"})















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

        

#retrieve  data
# class History(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self,request,id=None,format=None):
#         id = request.data.get('id')
#         if id:
#             obj = Users_donations.objects.get(id = id)
#             serializer = FoodSerializer(obj)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         obj = Users_donations.objects.all()
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




# class DonarCart(ModelViewSet):
    
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     # print(request.user)
#     queryset = Users_donations.objects.filter( )