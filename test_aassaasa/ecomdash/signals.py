# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F, Case, When, Value
from .models import SubProductInventory, ShopifySubProductSale, AmazonSubProductSale, KitSale, InventoryLog, AmazonKitSale, PackagingComponentInventory, PackagingComponentInventoryLog


@receiver(post_save, sender=ShopifySubProductSale)
@receiver(post_save, sender=AmazonSubProductSale)
def update_inventory(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, ShopifySubProductSale):
            sub_product = instance.shopify_sub_product
            quantity_sold = instance.shopify_quantity_sold
            order_id = instance.shopify_default_order_id
            sales_channel = instance.sales_channel
        else:  # AmazonSubProductSale
            sub_product = instance.amazon_sub_product
            quantity_sold = instance.amazon_quantity_sold
            order_id = instance.amazon_orderid
            sales_channel = instance.amazon_sales_channel

        if sales_channel.treat_negative_sales_as_returns and quantity_sold < 0:
            quantity_sold = abs(quantity_sold)

        try:
            inventory = SubProductInventory.objects.get(sub_product=sub_product)
            previous_inventory = inventory.inventory_available
            inventory.inventory_available = Case(
            When(inventory_available__gte=quantity_sold, then=F('inventory_available') - quantity_sold),
            default=Value(0)
        )
            inventory.save()

            # Reload the instance to get the updated value from the database
            inventory.refresh_from_db()

            if inventory.inventory_available == 0:
                print(f"Inventory went to zero for {sub_product.sp_sku} with order ID {order_id}")

            # Create a log
            InventoryLog.objects.create(
                sub_product=sub_product,
                previous_inventory=previous_inventory,
                updated_inventory=inventory.inventory_available,
                quantity_sold=quantity_sold,
                order_id=str(order_id)
            )
        except SubProductInventory.DoesNotExist:
            print(f"No inventory record for {sub_product.sp_sku}")
        
        # get subproduct's related packaging components
        for packaging_component in sub_product.packaging_components.all():
            try:
                pc_inventory = PackagingComponentInventory.objects.get(packaging_component=packaging_component)
                previous_pc_inventory = pc_inventory.pc_inventory_available
                pc_inventory.pc_inventory_available = Case(
                    When(pc_inventory_available__gte=quantity_sold, then=F('pc_inventory_available') - quantity_sold),
                    default=Value(0)
                )
                pc_inventory.save()

                # Reload the instance to get the updated value from the database
                pc_inventory.refresh_from_db()

                if pc_inventory.pc_inventory_available == 0:
                    print(f"Packaging component inventory went to zero for {packaging_component.packaging_component_id} with order ID {order_id}")

                # Create a log
                PackagingComponentInventoryLog.objects.create(
                    packaging_component=packaging_component,
                    previous_inventory=previous_pc_inventory,
                    updated_inventory=pc_inventory.pc_inventory_available,
                    quantity_sold=quantity_sold,
                    order_id=str(order_id)
                )
            except PackagingComponentInventory.DoesNotExist:
                print(f"No inventory record for {packaging_component.packaging_component_id}")



@receiver(post_save, sender=KitSale)
def update_inventory_for_kit(sender, instance, created, **kwargs):
    if created:
        kit = instance.kit
        quantity_sold = instance.shopify_quantity_sold
        order_id = instance.shopify_default_order_id
        sales_channel = instance.sales_channel

        if sales_channel.treat_negative_sales_as_returns and quantity_sold < 0:
            quantity_sold = abs(quantity_sold)


        for sub_product in kit.sub_products.all():
            try:
                inventory = SubProductInventory.objects.get(sub_product=sub_product)
                previous_inventory = inventory.inventory_available
                inventory.inventory_available = Case(
                    When(inventory_available__gte=quantity_sold, then=F('inventory_available') - quantity_sold),
                    default=Value(0)
                )
                inventory.save()

                inventory.refresh_from_db()

                if inventory.inventory_available == 0:
                    print(f"Inventory went to zero for {sub_product.sp_sku} with order ID {order_id}")


                # Create a log
                InventoryLog.objects.create(
                    sub_product=sub_product,
                    previous_inventory=previous_inventory,
                    updated_inventory=inventory.inventory_available,
                    quantity_sold=quantity_sold,
                    order_id=str(order_id)
                )
            except SubProductInventory.DoesNotExist:
                print(f"No inventory record for {sub_product.sp_sku}")

            # get subproduct's related packaging components
            for packaging_component in sub_product.packaging_components.all():
                try:
                    pc_inventory = PackagingComponentInventory.objects.get(packaging_component=packaging_component)
                    previous_pc_inventory = pc_inventory.pc_inventory_available
                    pc_inventory.pc_inventory_available = Case(
                        When(pc_inventory_available__gte=quantity_sold, then=F('pc_inventory_available') - quantity_sold),
                        default=Value(0)
                    )
                    pc_inventory.save()

                    # Reload the instance to get the updated value from the database
                    pc_inventory.refresh_from_db()

                    if pc_inventory.pc_inventory_available == 0:
                        print(f"Packaging component inventory went to zero for {packaging_component.packaging_component_id} with order ID {order_id}")

                    # Create a log
                    PackagingComponentInventoryLog.objects.create(
                        packaging_component=packaging_component,
                        previous_inventory=previous_pc_inventory,
                        updated_inventory=pc_inventory.pc_inventory_available,
                        quantity_sold=quantity_sold,
                        order_id=str(order_id)
                    )
                except PackagingComponentInventory.DoesNotExist:
                    print(f"No inventory record for {packaging_component.packaging_component_id}")




@receiver(post_save, sender=AmazonKitSale)
def update_inventory_for_amazon_kit(sender, instance, created, **kwargs):
    if created:
        kit = instance.kit
        quantity_sold = instance.amazon_quantity_sold
        order_id = instance.amazon_orderid
        sales_channel = instance.sales_channel

        if sales_channel.treat_negative_sales_as_returns and quantity_sold < 0:
            quantity_sold = abs(quantity_sold)


        for sub_product in kit.sub_products.all():
            try:
                inventory = SubProductInventory.objects.get(sub_product=sub_product)
                previous_inventory = inventory.inventory_available
                inventory.inventory_available = Case(
                    When(inventory_available__gte=quantity_sold, then=F('inventory_available') - quantity_sold),
                    default=Value(0)
                )
                inventory.save()

                inventory.refresh_from_db()

                if inventory.inventory_available == 0:
                    print(f"Inventory went to zero for {sub_product.sp_sku} with order ID {order_id}")

                # Create a log
                InventoryLog.objects.create(
                    sub_product=sub_product,
                    previous_inventory=previous_inventory,
                    updated_inventory=inventory.inventory_available,
                    quantity_sold=quantity_sold,
                    order_id=str(order_id)
                )
            except SubProductInventory.DoesNotExist:
                print(f"No inventory record for {sub_product.sp_sku}")

            for packaging_component in sub_product.packaging_components.all():
                try:
                    pc_inventory = PackagingComponentInventory.objects.get(packaging_component=packaging_component)
                    previous_pc_inventory = pc_inventory.pc_inventory_available
                    pc_inventory.pc_inventory_available = Case(
                        When(pc_inventory_available__gte=quantity_sold, then=F('pc_inventory_available') - quantity_sold),
                        default=Value(0)
                    )
                    pc_inventory.save()

                    # Reload the instance to get the updated value from the database
                    pc_inventory.refresh_from_db()

                    if pc_inventory.pc_inventory_available == 0:
                        print(f"Packaging component inventory went to zero for {packaging_component.packaging_component_id} with order ID {order_id}")

                    # Create a log
                    PackagingComponentInventoryLog.objects.create(
                        packaging_component=packaging_component,
                        previous_inventory=previous_pc_inventory,
                        updated_inventory=pc_inventory.pc_inventory_available,
                        quantity_sold=quantity_sold,
                        order_id=str(order_id)
                    )
                except PackagingComponentInventory.DoesNotExist:
                    print(f"No inventory record for {packaging_component.packaging_component_id}")




