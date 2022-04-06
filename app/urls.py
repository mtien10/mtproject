from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello', hello),
    path('search-product', search_product),
    path('order-product/<id>', order_product)
]

# Category
router = DefaultRouter()
router.register('category', CategoryViewSet)
urlpatterns += router.urls

# Product
router = DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns += router.urls
