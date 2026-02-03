from rest_framework import serializers
from .models import FeePayment

class FeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePayment
        fields = "__all__"
        read_only_fields = ['status', 'transaction_id', 'otp']
