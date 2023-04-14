from django.db   import models
from core.models import TimeStampModel

class Cart(TimeStampModel): 
    quantity = models.IntegerField()
    product  = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user     = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'carts'