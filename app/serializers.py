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
        fields = super().get_fields(*args, **kwargs)
        return fields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            "category": {
                "error_messages": {
                    'null': 'Trường này không được bỏ trống  '
                }
            },
            "code": {
                "validators": [
                    UniqueValidator(queryset=Product.objects.all(), message='Mã sản phẩm đã tồn tại')
                ]
            },
            "price": {
                "error_messages": {
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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'qty', 'productName', 'priceUnit', 'total',
                  'customerName', 'customerPhone', 'customerAddress',
                  'orderDate', 'deliverDate', 'status']

    qty = serializers.IntegerField(validators=[MinValueValidator(1)], error_messages={
        'invalid': 'Giá trị không hợp lệ.'
    })

    productName = serializers.CharField(default='', source='product.name')
    priceUnit = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)
    orderDate = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    deliverDate = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    status = serializers.IntegerField(read_only=True)

    def validate_customerPhone(self, phone):
        if phone:
            if phone[0] != '0' or not phone.isdigit():
                raise serializers.ValidationError('Số điện thoại không hợp lệ')

            elif len(phone) != 10 and len(phone) != 11:
                raise serializers.ValidationError('Số điện thoại phải có 10/11 số')
