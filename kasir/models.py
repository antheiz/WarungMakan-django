from django.db import models

# Create your models here.

class Makanan(models.Model):
    namaMakanan = models.CharField(max_length=255)
    hargaMakanan = models.CharField(max_length=255)
    imageMakanan = models.ImageField(null=True, blank=True, upload_to="menu/")

    def __str__(self):
        return self.namaMakanan
    
class Minuman(models.Model):
    namaMinuman = models.CharField(max_length=255)
    hargaMinuman = models.CharField(max_length=255)
    imageMinuman = models.ImageField(null=True, blank=True, upload_to="menu/")
    
    def __str__(self):
        return self.namaMinuman