from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from apps.fee.models import Fee

@admin.register(Fee)
class FeeAdmin(ModelAdmin):
    model = Fee
    list_display = ("student", "amount", "date_paid",)
    list_filter = ("student", "date_paid",)
    search_fields = ("student__email",)
    fieldsets = (
        (None, {"fields": ("student", "amount", "date_paid",)}),
    )
