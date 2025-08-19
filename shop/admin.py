from django.contrib import admin

# Register your models here.

from shop.models import Tag, Product, ProductOption


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'price')
    search_fields = ('name',)
    ordering = ('product__name', 'name')

    def product(self, obj):
        return obj.product.name if obj.product else None
    product.short_description = 'Product Name'
    product.admin_order_field = 'product__name'  # Allows sorting by product name in