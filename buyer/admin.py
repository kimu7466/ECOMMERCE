from django.contrib import admin
from .models import ContactUSModel, cartModel,Order,OrderItem
# Register your models here.

class ContactUSModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'status', 'first_name', 'last_name', 'email', 'message']
    list_filter = ['status']
    search_fields = ['phone', 'email']
    list_display_links = ['phone', 'email']
    list_editable = ['status']
    list_per_page = 10

admin.site.register(ContactUSModel,ContactUSModelAdmin)

admin.site.register(cartModel)
admin.site.register(Order)
admin.site.register(OrderItem)


