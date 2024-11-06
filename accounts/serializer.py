from typing import Any, Dict
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id']=user.id
        token['name'] = user.name
        token['place'] = user.place
        token['email'] = user.email

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        user=self.user
        data['id']=user.id
        data['name'] = user.name
        data['place'] = user.place
        data['email'] = user.email

        return data
    
    
class Registration(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id=serializers.ReadOnlyField()
    class Meta:
        model=CustomUser
        fields=['id','name','phone','place','pincode','email','password']
        
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    
class ProfileSer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','name','email','phone','place','pincode']
        
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class ProductSer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name','description','price','stock','category','image']
        
class ProductSer2(serializers.ModelSerializer):
    image_url=serializers.SerializerMethodField()
    class Meta:
        model=Products
        fields=['id','name','description','price','stock','category','image_url']
        
    def get_image_url(self, obj):
        return obj.get_image_url()
 