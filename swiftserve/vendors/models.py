from django.db import models

class Vendors(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_location = models.CharField(max_length=255, blank=True, null=True)
    contact_information = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.vendor_name