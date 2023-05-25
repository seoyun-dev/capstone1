import json, re

from django.http   import JsonResponse
from django.db     import transaction
from django.views  import View

from orders.models import Order, OrderProduct
from carts.models  import Cart
from users.utils   import signin_decorator

class OrderView(View):
    @signin_decorator
    def post(self,request):
        try:
            data  = json.loads(request.body)
            carts = Cart.objects.filter(id__in=data['cart_ids'])

            with transaction.atomic():
                order = Order.objects.create(
                    tid             = data['tid'],
                    receiver        = data['receiver'],
                    address         = data['address'],
                    order_status_id = 1,
                    user_id         = request.user.id
                )
                order_product_list = [OrderProduct(
                    order_id        = order.id,
                    product_id      = cart.product_id,
                    quantity        = cart.quantity,
                    )for cart in carts]

                OrderProduct.objects.bulk_create(order_product_list)

                Cart.objects.filter(user=request.user, id__in=data['cart_ids']).delete()
                return JsonResponse({"message" : "NEW_ORDER_CREATED"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'message':'JSONDecodeError'}, status=404)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

    @signin_decorator
    def get(self, request):
        try:
            result = {
                'user_id'    : request.user.id,
                'user_name'  : request.user.nickname,
                'orders_list': [
                    {
                        'id'          : order.id,
                        'tid'         : order.tid,
                        'receiver'    : order.receiver,
                        'order_status': order.order_status.status,
                        # re.sub(pattern, new_text, text): text에서 pattern인 부분을 new_text로 변경
                        'order_number': re.sub('[^0-9]', '', str(order.created_at)) + str(order.id),
                        'products'    : [
                            {
                                'id'          : order_product.id,
                                'product_img' : order_product.product.productimage_set.all()[0].image_url,
                                'product_name': order_product.product.name,
                                'product_price' : order_product.product.price,
                                'quantity' : order_product.quantity,
                                'product_total_price' : order_product.product.price * order_product.quantity
                            } for order_product in order.orderproduct_set.all()
                        ]
                    } for order in Order.objects.filter(user_id=request.user.id)
                ]
            }

            return JsonResponse({'RESULT' : result}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSONDecoderError'}, status=400)
    

    @signin_decorator
    def patch(self, request):
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')

            order = Order.objects.get(id=order_id)
            if order.order_status_id == 2:
                return JsonResponse({'message' : 'ALREADY_CHANGE'}, status=400)
            order.order_status_id = 2 
            order.save()
            
            return JsonResponse({'message' : 'CANCEL_ORDER'}, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSONDecoderError'}, status=400)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except Order.DoesNotExist:
            return JsonResponse({'message' : 'ORDER_DOES_NOT_EXIST'}, status=404)