from django.db import models
from vendors.models import Vendors

class Orders(models.Model):
    token_number = models.CharField(max_length=255, unique=True,db_index=True)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE,db_index=True)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255,db_index=True)

    def __str__(self):
        return self.token_number

class Order_Status_History(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.token_number} - {self.status}"