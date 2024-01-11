from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=1000)
    product_image = models.CharField(max_length=1000)
    def __str__(self):
        try:
            return (self.name)
        except:
            return ("Default Category Name")
        
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        try:
            return (self.name)
        except:
            return ("Default Manufacturer Name")
        
class SubProduct(models.Model):
    sp_name = models.CharField(max_length=1000)
    sp_image = models.CharField(max_length=1000)
    sp_leadtime = models.IntegerField(null=True, blank=True)
    sp_manfcost = models.IntegerField(null=True, blank=True)
    sp_sku = models.CharField(max_length=20, unique=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_products')
    packaging_components = models.ManyToManyField(
        'PackagingComponent',
        related_name='sub_products'
    )
    sp_barcode = models.CharField(max_length=200, null=True)
    sp_gst = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    sp_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        try:
            return (self.sp_name)
        except:
            return ("Default Sub Product Name")
        
class Kit(models.Model):
    name = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)  
    sp_sku = models.CharField(max_length=20, unique=True)
    sub_products = models.ManyToManyField(SubProduct, related_name='kits')
    # any other fields that are specific to a Kit

    def __str__(self):
        return self.name
        
class SubProductInventory(models.Model):
    sub_product = models.OneToOneField(SubProduct, on_delete=models.CASCADE, related_name='sub_product_inventory')
    inventory_available = models.IntegerField(default=0)
    last_inventory_checked = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        try:
            return (self.sub_product.sp_name)
        except:
            return ("Default Sub Product Name")


class BatchDetail(models.Model):
    sub_product = models.ManyToManyField(SubProduct, through='BatchProduct')
    batchname = models.CharField(max_length=200, default='DEBatchName')
    manf_date = models.DateField(null=True, blank=True)
    expiry = models.DateField(null=True, blank=True)
    manufacturer = models.CharField(max_length=1000)

    def __str__(self):
        try:
            return (self.batchname)
        except:
            return ("Default Sub Product Name")
        
class BatchProduct(models.Model):
    # Define foreign keys for Product and Batch
    sub_product = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    batchdetail = models.ForeignKey(BatchDetail, on_delete=models.CASCADE)
    # Additional data field for the quantity of each product in a batch
    sub_product_batch_inventory = models.IntegerField()

    class Meta:
        unique_together = ('sub_product', 'batchdetail')


class PackagingComponent(models.Model):
    packaging_component_name = models.CharField(max_length=200)
    packaging_component_id = models.CharField(max_length=200, unique=True)
    packaging_component_category = models.CharField(max_length=100)
    packaging_component_lead_time = models.IntegerField(null=True, blank=True)
    packaging_component_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    packaging_component_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        try:
            return (self.packaging_component_name)
        except:
            return ("Default Sub Product Name")

class PackagingComponentInventory(models.Model):
    packaging_component = models.OneToOneField(PackagingComponent, on_delete=models.CASCADE, related_name='pc_inventory')
    pc_inventory_available = models.IntegerField(default=0)
    pc_last_inventory_checked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        try:
            return (self.packaging_component.packaging_component_name)
        except:
            return ("Default Packaging Component Name")
        
class PackagingComponentInventoryLog(models.Model):
    packaging_component = models.ForeignKey(PackagingComponent, on_delete=models.SET_NULL, related_name='pc_inventory_logs', null=True)
    previous_inventory = models.IntegerField()
    updated_inventory = models.IntegerField()
    quantity_sold = models.IntegerField()
    order_id = models.CharField(max_length=50, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} order inventory updated on {self.date_updated}"
        
class SalesChannel(models.Model):
    sales_channel = models.CharField(max_length=255)
    treat_negative_sales_as_returns = models.BooleanField(default=True)

    def __str__(self):
        try:
            return (self.sales_channel)
        except:
            return ("Default Sales Channel Name")
        

class SalesType(models.Model):
    sales_type = models.CharField(max_length=255)

    def __str__(self):
        try:
            return (self.sales_type)
        except:
            return ("Default Sales Type Name")
    

class AmazonSubProductSale(models.Model):
    amazon_sub_product = models.ForeignKey(SubProduct, on_delete=models.SET_NULL, null=True, related_name='amazonsubproductsales')
    amazon_date_of_sales = models.DateTimeField()
    amazon_quantity_sold = models.IntegerField(default=0)
    amazon_sales_channel = models.ForeignKey(SalesChannel, on_delete=models.SET_NULL, null=True, related_name='sales')
    amazon_sales_type = models.ForeignKey(SalesType, on_delete=models.SET_NULL, null=True)
    amazon_product_return = models.BooleanField(default=False)
    amazon_orderid = models.CharField(max_length=50, default='AMZ101')

    def __str__(self):
        try:
            return (self.amazon_orderid)
        except:
            return ("Default Amazon Order ID")

class ShopifySubProductSale(models.Model):
    shopify_sub_product = models.ForeignKey(SubProduct, on_delete=models.SET_NULL, null=True, related_name='shopifysubproductsales')
    shopify_date_of_sales = models.DateTimeField()
    shopify_quantity_sold = models.IntegerField(default=0)
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.SET_NULL, null=True, related_name='shopifysales')
    sales_type = models.ForeignKey(SalesType, on_delete=models.SET_NULL, null=True)
    shopify_product_return = models.BooleanField(default=False)
    shopify_merchant_ordername = models.CharField(max_length=1000, default='DE101')
    shopify_default_order_id = models.BigIntegerField()
    shopify_gross_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shopify_productsale_taxes = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    shopify_productsale_discount = models.DecimalField(max_digits=8, decimal_places=2, null=True)


    def __str__(self):
        try:
            return (self.shopify_merchant_ordername)
        except:
            return ("Default Sub Product Name")
        
class InventoryLog(models.Model):
    sub_product = models.ForeignKey(SubProduct, on_delete=models.SET_NULL, related_name='inventory_logs', null=True)
    previous_inventory = models.IntegerField()
    updated_inventory = models.IntegerField()
    quantity_sold = models.IntegerField()
    order_id = models.CharField(max_length=1000, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} order inventory updated on {self.date_updated}"

class KitSale(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.SET_NULL, related_name='kitsales', null=True)
    date_of_sale = models.DateTimeField()
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.SET_NULL, null=True, related_name='shopifykitsaleschannel')
    sales_type = models.ForeignKey(SalesType, on_delete=models.SET_NULL, null=True)
    shopify_quantity_sold = models.IntegerField(default=0)
    shopify_default_order_id = models.BigIntegerField(default=0)
    
    def __str__(self):
        return f"{self.kit.name} sold on {self.date_of_sale}"
    
class AmazonKitSale(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.SET_NULL, related_name='amazonkitsales', null=True)
    date_of_sale = models.DateTimeField()
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.SET_NULL, null=True, related_name='amazonkitsaleschannel')
    sales_type = models.ForeignKey(SalesType, on_delete=models.SET_NULL, null=True)
    amazon_quantity_sold = models.IntegerField(default=0)
    amazon_orderid = models.CharField(max_length=50, default='DE101')

    
    def __str__(self):
        return f"{self.kit.name} sold on {self.date_of_sale}"

