from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from .models import Product, ProductImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name',
                 'description',
                 'price', 
                 'status', 
                 'category', 
                 'created', 
                 'updated', 
                 'stock', 
                ]

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']


    