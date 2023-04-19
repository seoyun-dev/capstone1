import os
import django
import csv

# 환경변수 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone1.settings")
django.setup()

# 환경변수 설정 후 model import
from products.models  import Product, ProductImage

with open('products.csv') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        for row in data_reader:
            name            = row[0]
            description     = row[1]
            content_url     = row[2]
            price           = row[3]
            stock           = row[4]
            sold            = row[5]
            release_date    = row[6]
            sub_category_id = row[7]

            Product.objects.create(name=name, description=description, content_url=content_url, price=price, stock=stock, sold=sold, release_date=release_date, sub_category_id=sub_category_id)

with open('product_images.csv') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        for row in data_reader:
            image_url       = row[0]
            product_id      = row[1]

            ProductImage.objects.create(image_url=image_url, product_id=product_id)
