from django.contrib import admin

from products.models import Basket, Product, ProductCategori

admin.site.register(ProductCategori)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',
                    'quantity', 'category',)
    fields = (('name', 'category'),
              'description', 'price',
              'quantity', 'image')
    readonly_fields = ('name', 'category')
    search_fields = ('name',)
    ordering = ('-price',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
