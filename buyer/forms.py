from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'shipping_address']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity', 'price']
