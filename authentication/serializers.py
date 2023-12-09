
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class GroupsSerializer(serializers.ModelSerializer): 
 
 
    class Meta:
        model = Group
        fields = ('name',)



class UserSerializer(serializers.ModelSerializer): 
    groups = GroupsSerializer()
    class Meta:
        model = User
        fields = '__all__'
