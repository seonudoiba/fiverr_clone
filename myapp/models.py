from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(verbose_name=("Category"),help_text=('Required and Unique'), max_length=50, unique=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    Conditions_allowed = models.CharField(max_length=255)
    Approval_required = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    class MPTTMeta:
        order_insertion_by = ['name']   
        
    def get_absolute_url(self):
        return reverse('category_detail', args={'slug': self.slug})
    def __str__(self):
        return self.name
    
#product Type
class ProductType(models.Model):
    name = models.CharField(verbose_name=("Product Type"),help_text=('Required and Unique'), max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"
        
    def __str__(self): # __unicode__ on Python 2 
        return self.name
    
#Product Specification
class ProductSpecification(models.Model):
    name = models.CharField(verbose_name=("Product Specification"),help_text=('Required and Unique'), max_length=50, unique=True, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True)
   
    class Meta:
        verbose_name = "Product Specification"
        verbose_name_plural = "Product Specifications"
        
    def __str__(self): # __unicode__ on Python 2
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/', null=True )
    slug = models.SlugField(max_length=50, null=True, blank=True, default='hello')
    title = models.CharField(max_length=50, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    date_added = models.DateField(auto_now_add=True )
    date_updated = models.DateField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-date_added']
        
    def get_absolute_url(self):
        return reverse('Product', args=[self.slug])
    
    def __str__(self):
        return self.title 
    
class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   
    specification = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Product Specification Value'
        verbose_name_plural = 'Product Specification Values'
    
    def __str__(self):
        return self.value
    
# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', null=True )
#     alt_text = models.CharField(max_length=50, null=True),
#     is_featured = models.BooleanField(default=False)
#     date_added = models.DateField(auto_now_add=True)
#     date_updated = models.DateField(auto_now_add=True, editable=False)
    
#     class Meta:
#         verbose_name = 'Product Image'
#         verbose_name_plural = 'Product Images'