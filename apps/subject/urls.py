from django.urls import path

from .views import SubjectApiView, SubjectDetailApiView

urlpatterns = [
    path('subjects/', SubjectApiView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailApiView.as_view(), name='subject-detail'),
]
