from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from core.views import AppUserListCreateView, AppUserDetailView, CustomerListCreateView, CustomerDetailView
from store.views import (
    ProductViewSet,
    CategoryViewSet,
    ShoppingCartViewSet
    # Add views for other store models here
)
#from books.views import BookListCreateView, BookDetailView, BookItemListView, BookItemDetailView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'carts', ShoppingCartViewSet)

#router.register(r'books', BookViewSet)  # If you're using viewsets for some models

urlpatterns = router.urls
