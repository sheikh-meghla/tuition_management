from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FeePayment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.CharField(max_length=20)

    bkash_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6, blank=True, null=True)

    STATUS = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')

    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
