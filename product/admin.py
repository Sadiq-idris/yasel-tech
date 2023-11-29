# django core imports
from django.contrib import admin
from django.utils.html import format_html

# imports from apps
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ["name", "price_naira", "tags"]
    list_filter = ["tags"]
    search_fields = ["name"]

    @admin.display(description="Price")
    def price_naira(self, obj):
        return format_html(f"&#8358;{obj.price}")


admin.site.register(Product, ProductAdmin)

admin.site.site_header = "Yasel Tech"
admin.site.site_title = "Yasel Tech"