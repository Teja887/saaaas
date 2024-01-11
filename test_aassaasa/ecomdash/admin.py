from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Manufacturer)
# admin.site.register(SubProduct)
# admin.site.register(SubProductInventory)
# admin.site.register(BatchDetail)
# admin.site.register(PackagingComponent)
# admin.site.register(PackagingComponentInventory)
# admin.site.register(SubProductSale)
# admin.site.register(SalesChannel)
# admin.site.register(SalesType)
# admin.site.register(BatchProduct)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # search_fields = Product.search_fields
    search_fields = ["name"]

@admin.register(Manufacturer)

@admin.register(SubProduct)
class SubProductAdmin(admin.ModelAdmin):
    search_fields = ["sp_sku"]

@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    search_fields = ["sp_sku"]

@admin.register(SubProductInventory)
class SubProductInventoryAdmin(admin.ModelAdmin):
    search_fields = ["sub_product__sp_sku"]

@admin.register(BatchDetail)
class BatchDetailAdmin(admin.ModelAdmin):
    search_fields = ["sub_product__sp_sku"]

@admin.register(BatchProduct)
class BatchProductAdmin(admin.ModelAdmin):
    search_fields = ["sub_product__sp_sku"]

@admin.register(PackagingComponent)
class PackagingComponentAdmin(admin.ModelAdmin):
    search_fields = ["packaging_component_id"]

@admin.register(PackagingComponentInventory)

@admin.register(SalesChannel)
@admin.register(SalesType)

@admin.register(AmazonSubProductSale)
class AmazonSubProductSaleAdmin(admin.ModelAdmin):
    search_fields = ["amazon_sub_product__sp_sku"]

@admin.register(ShopifySubProductSale)
class ShopifySubProductSaleAdmin(admin.ModelAdmin):
    search_fields = ["shopify_merchant_ordername"]

@admin.register(KitSale)
class KitSaleAdmin(admin.ModelAdmin):
    search_fields = ["kit__sp_sku"]

@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    search_fields = ["sub_product__sp_sku"]

@admin.register(AmazonKitSale)
class AmazonKitSaleAdmin(admin.ModelAdmin):
    search_fields = ["kit__sp_sku"]

@admin.register(PackagingComponentInventoryLog)
class PackagingComponentInventoryLogAdmin(admin.ModelAdmin):
    search_fields = ["packaging_component__packaging_component_id"]