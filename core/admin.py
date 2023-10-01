from django.contrib import admin
from .models import AppUser
from store.models import Customer
# Register your models here.
class CustomerInline(admin.TabularInline):  # You can also use admin.StackedInline for a different display style
    model = Customer
    can_delete = False
    

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    inlines = [CustomerInline]