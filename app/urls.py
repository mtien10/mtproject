from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('search-product', search_product),
    path('order-product/<pk>', order_product),
    path('confirm_order/<pk>', confirm_order),
    path('cancel_order/<pk>', cancel_order)
]

# Category
router = DefaultRouter()
router.register('category', CategoryViewSet)
urlpatterns += router.urls

# Product
router = DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns += router.urls
