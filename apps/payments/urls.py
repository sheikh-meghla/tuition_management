from django.urls import path
from .views import BkashPaymentRequestAPIView, BkashOtpVerifyAPIView

urlpatterns = [
    path('bkash/request/', BkashPaymentRequestAPIView.as_view()),
    path('bkash/verify/', BkashOtpVerifyAPIView.as_view()),
]