# admin.py

from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Product, ProductImage
from django.utils.html import format_html

class ProductImagesInline(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    def first_image(self, obj):
        first_image = obj.productimage_set.first()
        if first_image:
            return format_html('<img src="{}" width="50" height="50" />', first_image.image.url)
        else:
            return "No Image"
        
    first_image.short_description = 'Image'

    list_display = ['first_image','name','price', 'description', 'category', 'status','stock']
    list_filter = ['status', 'price', 'name', 'category']
    # list_editable = ['price', 'category', 'status']
    inlines = [ProductImagesInline]

# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ['product', 'image']

admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductImage, ProductImageAdmin)

