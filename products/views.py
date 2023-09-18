from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .models import Product, ProductImage
from django.template import loader
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ProductSerializer, ProductImageSerializer


# Create your views here.
def products(request):
    my_products = Product.objects.all()  # Query all products
    template = loader.get_template('all_products.html')
    context = {'myproducts': my_products}
    return HttpResponse(template.render(context, request))

def product_details(request, id):
    myproduct = Product.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {'myproduct': myproduct}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]