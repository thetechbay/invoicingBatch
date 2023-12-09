from django.conf import settings
from rest_framework import serializers
from .models import *

from authentication.serializers import UserSerializer



class companiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = companies
        fields = '__all__'

class clientsSerializer(serializers.ModelSerializer):
    company = companiesSerializer()
    class Meta:
        model = clients
        fields = '__all__'


class salesSerializer(serializers.ModelSerializer):
    client = clientsSerializer()
    company = companiesSerializer()
    class Meta:
        model = sales
        fields = '__all__'


class salesItemSerializer(serializers.ModelSerializer):
    # sale = salesSerializer()
    class Meta:
        model = salesItem
        fields = '__all__'