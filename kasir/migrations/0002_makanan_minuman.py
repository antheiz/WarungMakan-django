# Generated by Django 2.2.8 on 2021-01-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaMakanan', models.CharField(max_length=255)),
                ('hargaMakanan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Minuman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaMinuman', models.CharField(max_length=255)),
                ('hargaMinuman', models.CharField(max_length=255)),
            ],
        ),
    ]
