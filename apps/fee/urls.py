from django.urls import path
from .views import FeeApiView

urlpatterns = [
    path('fee/', FeeApiView.as_view(), name='fee-list'),

]
