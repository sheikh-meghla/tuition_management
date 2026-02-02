from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.subject.models import Subject

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    model = Subject
    list_display = ("name", "description",)
    search_fields = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "description")}), 
    )