from rest_framework import serializers
from Cart.models import Cart, CartItem

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model= CartItem
        fields = ['id', 'product', 'quantity']
        
class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(many=True)
    
    class Mera:
        model = Cart
        fields = ['id', 'user', 'items']