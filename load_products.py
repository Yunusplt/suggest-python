import json
import os
import django

# set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from suggest.models import Products

# read the JSON file
with open("suggest/fixtures/top-1000-products.json", encoding="utf-8") as f:
    products = json.load(f)

# add products to the database
for item in products:
    Products.objects.create(
        product_name=item["name"],
        category=item["category"],
        price=item["price"]
    )

print(f"✅ {len(products)} products loaded into the database.")
