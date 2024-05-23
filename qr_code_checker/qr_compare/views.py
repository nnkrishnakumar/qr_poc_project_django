# qr_compare/views.py
import cv2
import numpy as np
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QRCodeUploadSerializer

def read_and_preprocess_image(image):
    # Convert the image to a numpy array
    image = np.array(image)
    # Convert the image from RGB to BGR (OpenCV format)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def are_images_exact_duplicates(image1, image2):
    # Check if the images are of the same size
    if image1.shape != image2.shape:
        return False
    # Compare the images
    difference = cv2.absdiff(image1, image2)
    return np.count_nonzero(difference) == 0

class CompareQRCodesAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QRCodeUploadSerializer(data=request.data)
        if serializer.is_valid():
            image1 = read_and_preprocess_image(serializer.validated_data['image1'])
            image2 = read_and_preprocess_image(serializer.validated_data['image2'])
            result = are_images_exact_duplicates(image1, image2)
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
