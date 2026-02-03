from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FeePayment
# Register your models here.
@admin.register(FeePayment)
class FeePaymentAdmin(ModelAdmin):
    model = FeePayment
    list_display = ("student", "amount", "month", "status",)
    list_filter = ("student", "month", "status",)
    search_fields = ("student__email", "transaction_id",)
    fieldsets = (
        (None, {"fields": ("student", "amount", "month", "status", "transaction_id",)}),
    )
