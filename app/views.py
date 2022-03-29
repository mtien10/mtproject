from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view, action
from .constans import PAGE_SIZE


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


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Chao mung on web '})
