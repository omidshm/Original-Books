from django.db import models
import uuid
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    #favourite_collections = models.ManyToManyField('Collection', null=True, blank=True, on_delete=models.SET_NULL)

class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    featured_product = models.ForeignKey(Product, related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    full_address = models.TextField()

# The rest of your Store app models can go here if needed.
