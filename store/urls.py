from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from core.views import AppUserListCreateView, AppUserDetailView, CustomerListCreateView, CustomerDetailView
from store.views import (
    ProductListView,
    ProductDetailView,
    # Add views for other store models here
)
#from books.views import BookListCreateView, BookDetailView, BookItemListView, BookItemDetailView

router = DefaultRouter()
#router.register(r'books', BookViewSet)  # If you're using viewsets for some models

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # Add URLs for other views
]
