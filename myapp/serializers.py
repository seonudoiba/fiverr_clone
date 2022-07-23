from rest_framework import serializers
from .models import Category, Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'Conditions_allowed', 'Approval_required', 'slug', 'parent')
 
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ('name','slug')        
class ProductSerializer(serializers.ModelSerializer):
    # product_image = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'category', 'date_added', 'price', 
                  'discount_price', 'description', 'available',
                  'featured', 'slug', 'product_type', 'title', 'date_updated','image')
