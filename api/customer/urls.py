from django.urls import path
from .views import CustomerCreateView

urlpatterns = [
    path('create_customer/', CustomerCreateView.as_view(), name='create'),
]