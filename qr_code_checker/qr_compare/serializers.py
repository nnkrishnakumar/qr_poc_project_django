# qr_compare/serializers.py
from rest_framework import serializers

class QRCodeUploadSerializer(serializers.Serializer):
    image1 = serializers.ImageField()
    image2 = serializers.ImageField()
