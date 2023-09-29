import logging
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

logger = logging.getLogger(__name__)
# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer