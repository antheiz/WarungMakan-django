from django.contrib import admin

# Register your models here.

from .models import Makanan, Minuman

data = Makanan, Minuman

admin.site.register(data)