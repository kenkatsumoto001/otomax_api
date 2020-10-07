from django.db import models
from django.contrib.auth.models import User


class MobilepulsaPriceList(models.Model):
    status = models.CharField(max_length=50)
    icon_url = models.CharField(max_length=50)
    pulsa_code = models.CharField(max_length=50)
    pulsa_op = models.CharField(max_length=50)
    pulsa_nominal = models.CharField(max_length=50)
    pulsa_details = models.CharField(max_length=50)
    pulsa_price = models.CharField(max_length=50)
    pulsa_type = models.CharField(max_length=50)
    masaaktif = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pulsa_code
