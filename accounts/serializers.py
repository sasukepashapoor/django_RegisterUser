from rest_framework import serializers



class UserSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    password2 = serializers.CharField(required=True,write_only=True)


    def validatae_username(self,value):
        if value == 'admin' : 
            raise serializers.ValidationError('your name can not be admin! ')

        return value

    def validate(self,data):
        if data['password'] != data['password2'] :
            raise serializers.ValidationError('secound password is not correct!')   
        return data
             










