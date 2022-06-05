# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer



# @api_view([ 'POST'])
# def create(request):
#     ser_data = UserSerializer(data=request.POST)
#     if ser_data.is_valid():
#         User.objects.creata_user(
#             username = ser_data.validated_data['username'],
#            # email = ser_data.validated_data['email'],
#             password = ser_data.validated_data['password'],
#         ) 

#         return Response (ser_data.data)
#     else:
#         return Response( ser_data.errors)

class register_user (APIView):
    def post(self,request):
        ser_data = UserSerializer(data=request.POST)

        if ser_data.is_valid():
            User.objects.creata_user(
                username = ser_data.validated_data['username'],
                email = ser_data.validated_data['email'],
                password = ser_data.validated_data['password'],
                password2 = ser_data.validated_data['password']
            ) 
            return Response (ser_data.data)

        else:
            return Response( ser_data.errors)

