from django.contrib import admin
from .models import customersModel, customerAddressModel
# Register your models here.
admin.site.register(customersModel)
admin.site.register(customerAddressModel)
