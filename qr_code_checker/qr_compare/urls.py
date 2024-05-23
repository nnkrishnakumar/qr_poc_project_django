# qr_compare/urls.py
from django.urls import path
from .views import CompareQRCodesAPIView

urlpatterns = [
    path('compare/', CompareQRCodesAPIView.as_view(), name='compare_qr_codes'),
]
