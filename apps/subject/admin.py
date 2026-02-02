from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.subject.models import Class, Subject

# Register your models here.
@admin.register(Class)
class ClassAdmin(ModelAdmin):
    model = Class
    list_display = ("name",)
    search_fields = ("name",)
    fieldsets = (
        (None, {"fields": ("name",)}),
    )

@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    model = Subject
    list_display = ("class_name","name", )
    list_filter = ("class_name",)
    search_fields = ("name", "class_name",)
    fieldsets = (
        (None, {"fields": ("class_name","name", )}),
    )