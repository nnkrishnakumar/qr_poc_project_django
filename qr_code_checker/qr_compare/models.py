from django.db import models

class QRCodeImage(models.Model):
    image = models.ImageField(upload_to='qr_codes/')

