from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('products/details/<int:id>', views.product_details, name='details'),
    # path('testing/', views.testing, name='testing'),
]