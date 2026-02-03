from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import FeePayment
from rest_framework_simplejwt.authentication import JWTAuthentication

class BkashOtpVerifyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        payment_id = request.data.get("payment_id")
        otp = request.data.get("otp")

        try:
            payment = FeePayment.objects.get(id=payment_id)
        except FeePayment.DoesNotExist:
            return Response({"error": "Invalid payment"}, status=400)

        if payment.otp == otp:
            payment.status = "PAID"
            payment.transaction_id = f"BKASH-DEMO-{payment.id}"
            payment.save()

            return Response({
                "message": "Payment successful ",
                "transaction_id": payment.transaction_id
            })
        else:
            return Response({"error": "Invalid OTP"}, status=400)
