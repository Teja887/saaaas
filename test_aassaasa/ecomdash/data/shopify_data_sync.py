#Shopify Data
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomboard.settings")
django.setup()
import csv
from datetime import datetime
from .models import SubProductSale, SubProduct

def import_sales_data(file_path):
    with open('/Users/Vasu_1/CODE_2022/Learning_22/pydev2023/ecomboard/ecomdash/Shopify.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            try:
                # Get the sub-product using the SKU from the CSV file
                sub_product = SubProduct.objects.get(sp_sku=row[1])
                sales_channel = "Shopify"
                sales_type = "Order"
                # Create a new product sale instance
                product_sale = SubProductSale(
                    sub_product=sub_product,
                    date_of_sales=datetime.strptime(row[0], '%Y-%m-%d'),  # Parse the date from the CSV file
                    quantity_sold=int(row[4]),
                    sales_channel=sales_channel,
                    sales_type=sales_type
                )
                product_sale.save()  # Save the new instance to the database

            except SubProduct.DoesNotExist:
                print(f"SubProduct with SKU {row[1]} does not exist")


#Shopify Data
# import csv
# with open('/Users/Vasu_1/CODE_2022/Learning_22/pydev2023/ecomboard/ecomdash/Shopify.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)  # Skip the header row
#     for row in csv_reader:
#         try:
#             # Get the sub-product using the SKU from the CSV file
#             # sub_product = SubProduct.objects.get(sp_sku=row[1])
#             sales_channel = "Shopify"
#             sales_type = "Order"
#             quantity_sold=row[4]
#             print(quantity_sold)
#             # Create a new product sale instance
#             # product_sale = ProductSale(
#             #     sub_product=sub_product,
#             #     date_of_sales=datetime.strptime(row[0], '%Y-%m-%d'),  # Parse the date from the CSV file
#             #     quantity_sold=int(row[3]),
#             #     sales_channel=sales_channel,
#             #     sales_type=sales_type
#             # )
#             # product_sale.save()  # Save the new instance to the database

#         except SubProduct.DoesNotExist:
#             print(f"SubProduct with SKU {row[1]} does not exist")