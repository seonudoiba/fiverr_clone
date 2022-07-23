from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductType, ProductSpecification, ProductSpecificationValue

# Register your models here.
admin.site.register(Category, MPTTModelAdmin)

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductSpecificationInline]
    
# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue
    
@admin.register(Product)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductSpecificationValueInline]

    