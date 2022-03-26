from rest_framework import serializers
from django.core.validators import MinValueValidator
from rest_framework.validators import UniqueValidator
from .models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

        extra_kwargs = {
            "code": {
                "validators": [
                    UniqueValidator(queryset=Category.objects.all(), message='Mã nhóm đã tồn tại ')
                ]
            },
        }

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields()(*args, **kwargs)
        return fields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            "category": {
                "error_message": {
                    'null': 'Trường này không được bỏ trống  '
                }
            },
            "code": {
                "validators": [
                    UniqueValidator(queryset=Product.objects.all(), message='Mã sản phẩm đã tồn tại')
                ]
            },
            "price": {
                "error_message": {
                    'invalid': 'Giá sản phẩm không hợp lệ.'
                }
            },
            "image": {
                "error_messages": {
                    'invalid': 'Ảnh sản phẩm không hợp lệ.'
                }
            }
        }

        def is_valid(self, *args, **kwargs):
            try:
                result = super().is_valid(*args, **kwargs)
                return result
            except Exception as e:
                raise e

        categoryName = serializers.CharField(read_only=True, default='', source='category.name')
