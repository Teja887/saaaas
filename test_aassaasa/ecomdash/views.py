from django.shortcuts import render
from ecomdash.models import SubProduct, SubProductInventory, PackagingComponentInventory, PackagingComponent, AmazonSubProductSale, ShopifySubProductSale, KitSale, AmazonKitSale
from datetime import datetime, timedelta
from django.db.models import Sum



def inventory_view(request):
    # Query the DB for all SubProductInventory objects, ordered by inventory_available in ascending order
    inventories = SubProductInventory.objects.order_by('inventory_available')
    return render(request, 'inventory.html', {'inventories': inventories})


def pc_inventory_view(request):
    # Query the database to get all PackagingComponentInventory objects, ordered by pc_inventory_available
    inventory_list = PackagingComponentInventory.objects.order_by('pc_inventory_available')

    # Pass this data to the template
    context = {'inventory_list': inventory_list}
    return render(request, 'pcinventory.html', context)

def inventoryalert_view(request):
    cutoff_date = datetime.now() - timedelta(days=30)
    
    sub_products = SubProduct.objects.all()

    # data to be sent to the template
    data = []
    total_last_30_days_sales = 0
    total_inventory_available = 0
    total_projected_sales = 0


    for sp in sub_products:

        # get inventory details
        inventory = SubProductInventory.objects.get(sub_product=sp).inventory_available

        # Get sales for the past 30 days
        amazon_sales = AmazonSubProductSale.objects.filter(amazon_sub_product=sp, amazon_date_of_sales__gte=cutoff_date).aggregate(total_sales=Sum('amazon_quantity_sold'))['total_sales'] or 0
        shopify_sales = ShopifySubProductSale.objects.filter(shopify_sub_product=sp, shopify_date_of_sales__gte=cutoff_date).aggregate(total_sales=Sum('shopify_quantity_sold'))['total_sales'] or 0
        kitsale_sales = 0
        
        for kit in sp.kits.all():
            sales = KitSale.objects.filter(kit=kit, date_of_sale__gte=cutoff_date).aggregate(total_sales=Sum('shopify_quantity_sold'))['total_sales'] or 0
            kitsale_sales += sales * kit.sub_products.count()

        amazonkitsale_sales = 0
        for kit in sp.kits.all():
            sales = AmazonKitSale.objects.filter(kit=kit, date_of_sale__gte=cutoff_date).aggregate(total_sales=Sum('amazon_quantity_sold'))['total_sales'] or 0
            amazonkitsale_sales += sales * kit.sub_products.count()
        
        # sum all sales
        
        total_sales = amazon_sales + shopify_sales + kitsale_sales + amazonkitsale_sales
        total_last_30_days_sales += total_sales
        total_inventory_available += inventory        

        # project sales for next 3 months
        projected_sales = total_sales * 3
        total_projected_sales += projected_sales

        # check if projected sales is greater than inventory
        if projected_sales > inventory:
            status = "low inventory"
            color = "red"
        else:
            status = "enough inventory"
            color = "green"

        data.append({
            'sp_name': sp.sp_name,
            'last_30_days_sales': total_sales,
            'inventory_available': inventory,
            'projected_sales': projected_sales,
            'status': status,
            'color': color
        })

        totals = {
        'total_last_30_days_sales': total_last_30_days_sales,
        'total_inventory_available': total_inventory_available,
        'total_projected_sales': total_projected_sales
    }


    return render(request, 'inventoryalert.html', {**{'data': data}, **{'totals': totals}})
