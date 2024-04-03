from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class StudentSerealizer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields='__all__'
        # fields = ['name','email']
        # exclude = ['age']
    
    def validate(self, data):

        if data['age']<18:
           raise serializers.ValidationError("Age must be more than 18")
        
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model=Product
        fields='__all__'
        # depth=1
    
    def to_representation(self, instance):
       self.fields['category'] =  CategorySerializer(read_only=True)
       return super(ProductSerializer, self).to_representation(instance)
    
class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user