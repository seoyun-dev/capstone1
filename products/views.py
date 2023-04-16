from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models  import Product, Category, SubCategory

class ProductListView(View):
    def get(self, request):
        try:
            main_category = request.GET.get('main_category', 'speakers')
            sub_category  = request.GET.get('sub_category')
            sort_method   = request.GET.get('sort_method', '-release_date')
            limit         = int(request.GET.get('limit', 9))
            offset        = int(request.GET.get('offset', 0))

            q = Q()

            if main_category:
                q &= Q(sub_category__category__name=main_category)

            elif sub_category:
                q &= Q(sub_category__name=sub_category)

            products      = Product.objects.filter(q).order_by(sort_method)
            products_list = products[offset:offset+limit]
            print(products_list[5].productimage_set.first().image_url)
            res_products = [
                {
                    'id'          : product.id,
                    'name'        : product.name,
                    'description' : product.description,
                    'price'       : product.price,
                    'image_url'   : [image.image_url for image in product.productimage_set.all()],
                    'release_date': product.release_date,
                } for product in products_list
            ]

            return JsonResponse({'RESULT':res_products, 'totalItems' : products.count()}, status=200)
        
        except Category.DoesNotExist:
            return JsonResponse({'message':'CATEGORY_DOES_NOT_EXIST'}, status=404)
        except SubCategory.DoesNotExist:
            return JsonResponse({'message':'SUB_CATEGORY_DOES_NOT_EXIST'}, status=404)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)
            product_detail = {
                'id'           : product.id,
                'name'         : product.name,
                'product_image': [product.image_url for product in product.productimage_set.all()],
                'description'  : product.description,
                'content_url'  : product.content_url,
                'price'        : product.price,
                'stock'        : product.stock
            }
            return JsonResponse({"result" : product_detail}, status=200)
        
        except Product.DoesNotExist:
            return JsonResponse({"message" : "DoesNotExist"}, status=400)