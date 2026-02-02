from django.urls import path
from .views import SignUpApiView, SignInApiView, SignOutApiView

urlpatterns = [
    path('signup/', SignUpApiView.as_view(), name='signup'),
    path('signin/', SignInApiView.as_view(), name='signin'),
    path('signout/', SignOutApiView.as_view(), name='signout'),
]
