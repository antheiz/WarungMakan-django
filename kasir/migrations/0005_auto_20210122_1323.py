# Generated by Django 2.2.8 on 2021-01-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0004_makanan_imagemakanan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makanan',
            name='imageMakanan',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y'),
        ),
    ]
