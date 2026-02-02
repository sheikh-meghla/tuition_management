from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Subject(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects', null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.class_name})"
