from django.db       import models

from core.models     import TimeStampModel
from products.models import Product
from users.models    import User

class Order(TimeStampModel):
    receiver     = models.CharField(max_length=100)
    address      = models.CharField(max_length=255)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderProduct(models.Model):
    order                = models.ForeignKey('Order', on_delete=models.CASCADE)
    product              = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity             = models.IntegerField()

    class Meta:
        db_table = 'orders_products'

class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders_status' 
