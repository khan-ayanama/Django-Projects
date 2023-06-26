from django.db import models

# Create your models here.


class contactEnquiry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    user_image = models.FileField(
        upload_to='contactEnquiry/', max_length=250, null=True, default=None)
