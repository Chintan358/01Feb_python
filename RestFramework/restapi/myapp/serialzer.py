from rest_framework import serializers
from .models import *


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