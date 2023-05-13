from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models  import Product, Category, SubCategory

class ProductListView(View):
    def get(self, request):
        try:
            category     = request.GET.get('category')
            sub_category = request.GET.get('sub_category')
            # + : 오름차순, - : 내림차순
            sort_method  = request.GET.get('sort_method', '-release_date') # 최신순 
            offset       = int(request.GET.get('offset', 0))
            limit        = 8

            q = Q()
            
            if category:
                # 예외처리 위해
                Category.objects.get(name=category)
                q &= Q(sub_category__category__name=category)

            if sub_category:
                SubCategory.objects.get(name=sub_category)
                q &= Q(sub_category__name=sub_category)

            products      = Product.objects.filter(q).order_by(sort_method)
            products_list = products[offset:offset+limit]
            res_products = [
                {
                    'id'          : product.id,
                    'name'        : product.name,
                    'description' : product.description,
                    'price'       : product.price,
                    'image_url'   : product.productimage_set.first().image_url,
                    'release_date': product.release_date,
                } for product in products_list
            ]

            return JsonResponse({'result':res_products}, status=200)
        
        except Category.DoesNotExist:
            return JsonResponse({'message':'CATEGORY_DOES_NOT_EXIST'}, status=404)
        
        except SubCategory.DoesNotExist:
            return JsonResponse({'message':'SUB_CATEGORY_DOES_NOT_EXIST'}, status=404)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)
            product_detail = {
                'id'          : product.id,
                'name'        : product.name,
                'description' : product.description,
                'content_url' : product.content_url,
                'price'       : product.price,
                'image_url'   : [image.image_url for image in product.productimage_set.all()],
                'release_date': product.release_date,
            }
            return JsonResponse({"result" : product_detail}, status=200)
        
        except Product.DoesNotExist:
            return JsonResponse({"message" : "PRODUCT_DOES_NOT_EXIST"}, status=400)