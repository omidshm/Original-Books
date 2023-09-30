import logging
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .pagination import ProductPagination
from .models import Product, Category, ShoppingCart
from .serializers import ProductSerializer, CategorySerializer, ShoppingCartSerializer

logger = logging.getLogger(__name__)
# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

class ShoppingCartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = ShoppingCart.objects.prefetch_related('cartitem_set__product').all()
    serializer_class = ShoppingCartSerializer