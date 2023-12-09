from django.contrib import admin
from.models import *
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.


app_models = apps.get_app_config('main_app').get_models()
for model in app_models:
    try:
        # if(model == orders): 
        #     admin.site.register(orders, OrdersAdmin)
        # else:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
