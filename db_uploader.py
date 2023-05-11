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
            id              = row[0]
            name            = row[1]
            description     = row[2]
            content_url     = row[3]
            price           = row[4]
            release_date    = row[5]
            sub_category_id = row[6]

            Product.objects.create(id=id, name=name, description=description, content_url=content_url, price=price, release_date=release_date, sub_category_id=sub_category_id)

# with open('product_images.csv') as in_file:
#         data_reader = csv.reader(in_file)
#         next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
#         for row in data_reader:
#             image_url       = row[0]
#             product_id      = row[1]

#             ProductImage.objects.create(image_url=image_url, product_id=product_id)