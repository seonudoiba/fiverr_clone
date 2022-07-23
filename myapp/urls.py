from django.urls import path
from .views import categories, products, product, category, home
urlpatterns = [
path("", home, name="list_view"),
path("categories/", categories, name="list_view"),
path("category/<int:pk>/", category, name="list_id"),
path("products/", products, name="product_view"),
path("product/<int:pk>/", product, name="product"),
]