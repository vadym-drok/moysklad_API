from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=36, blank=True, null=True)
    sum = models.DecimalField(max_digits=12, decimal_places=1, blank=True, null=True)
    
    class Meta():
        db_table = 'Vadym].[Orders'
