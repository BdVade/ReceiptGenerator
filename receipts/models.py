from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


# Create your models here.


class Receipt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receipts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)


def file_upload(instance, filename):
    return f'{instance.receipt.id}/{instance.id}'


class ReceiptFile(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='files')
    file = models.FileField()
