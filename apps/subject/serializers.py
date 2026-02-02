from rest_framework import serializers
from .models import Subject, Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']

class SubjectSerializer(serializers.ModelSerializer):
    class_name = ClassSerializer(read_only=True) 
    class Meta:
        model = Subject
        fields = ['id', 'class_name', 'name']

