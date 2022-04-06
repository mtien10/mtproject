import time
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view, action
from .constans import PAGE_SIZE
from rest_framework.views import status
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=False, methods=['get'])
    def search(self, request):
        data = request.GET

        name = data.get('name', '')

        start = data.get('start', '')
        start = int(start) if start.isdigit() else 0

        count = data.get('count', '')
        count = int(count) if count.isdigit() else PAGE_SIZE

        categoryList = Category.objects.filter(name__icontains=name).order_by('-id')
        total = categoryList.count()
        items = categoryList[start:start + count]

        data = CategorySerializer(items, many=True).data
        return Response({'items': data, 'total': total})

    @action(detail=True, methods=['get'])
    def get_detail(self, request, pk):
        time.sleep(2)
        category = Category.objects.get(pk=pk)
        data = CategorySerializer(instance=category).data
        return Response(data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@api_view(['GET'])
def search_product(request):
    PAGE_SIZE = 5
    price_ranges = [
        {'max': 10},
        {'min': 10, 'max': 20},
        {'min': 20}
    ]
    data = request.GET
    start = int(data.get('start', 0))
    count = int(data.get('count', PAGE_SIZE))
    categoryId = data.get('categoryId')
    priceRangeId = data.get('priceRangeId')
    keyword = data.get('keyword', '')

    product_list = Product.objects.filter(name__icontains=keyword)
    if categoryId:
        product_list = product_list.filter(category__id=categoryId)

    if priceRangeId and priceRangeId.isdigit():
        price_range = price_ranges[int(priceRangeId) - 1]
        price_min = price_range.get('min')
        price_max = price_range.get('max')

        if price_min:
            product_list = product_list.filter(price__gte=price_min * 1000000)

        if price_max:
            product_list = product_list.filter(price__lte=price_max * 1000000)

    total = product_list.count()
    items = product_list[start:start + count]
    data = ProductSerializer(items, many=True).data
    return Response({'total': total, 'items': data})


@api_view(['POST'])
def order_product(request, id):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        product = Product.objects.get(id=id)
        data = request.data
        order = Order()

        order.product = product
        order.qty = int(data.get('qty'))
        order.priceUnit = product.price
        order.total = order.qty * order.priceUnit
        order.customerName = data.get('customerName')
        order.customerPhone = data.get('customerPhone')
        order.customerAddress = data.get('customerAddress')
        order.orderDate = datetime.now()
        order.status = Order.Status.PENDING
        order.save()
        return Response({'success': True})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def confirm_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.DELIVERED
    order.save()
    return Response({'success': True})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.CANCELLED
    order.save()
    return Response({'success': True})


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Chao mung on web '})
