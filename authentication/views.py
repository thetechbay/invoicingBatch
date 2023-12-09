

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# from main_app.models import companies, userInformation
from main_app.serializers import *

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,**kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user= Token.objects.get(key=token.key).user
        group = GroupsSerializer(user.groups.all(),many=True,context={'request':None})
        sinfo = UserSerializer(user, context={'request': None})
        loda = {
            'token': token.key,
            'info':sinfo.data,
            'group' : group.data,

        }
        return Response(loda)