from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from apps.fee.models import Fee

@admin.register(Fee)
class FeeAdmin(ModelAdmin):
    model = Fee
    list_display = ("class_name","month", "amount", "subject",)
    list_filter = ("class_name", "month",)
    search_fields = ("class_name", "subject__name",)
    fieldsets = (
        (None, {"fields": ("class_name", "month", "amount", "subject", )}),
    )
