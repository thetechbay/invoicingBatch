
from django.urls import path
from .views import *


urlpatterns = [
    path('gettoken/',CustomAuthToken.as_view()),
]