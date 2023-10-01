from django.contrib import admin
from .models import Category, Product, Order, Customer, OrderItem, Address
from django.conf import settings


class OrderItemInline(admin.TabularInline):  # You can also use admin.StackedInline for a different display style
    model = OrderItem
    extra = 0  # Number of empty forms to display


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_product')
    autocomplete_fields = ('featured_product',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'inventory', 'last_updated')
    autocomplete_fields = ('category',)
    list_filter = ('category', 'last_updated')
    search_fields = ('title', 'category__title')
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'placed_at', 'payment_status')
    list_filter = ('placed_at', 'payment_status')
    search_fields = ('customer__user__username', 'customer__user__email')
    date_hierarchy = 'placed_at'
    inlines = (OrderItemInline,)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date','phone')
    search_fields = ('user__username', 'user__email')
    inlines = (AddressInline,)