# Generated by Django 4.0.4 on 2022-04-13 22:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_receipt_description_alter_receiptfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptfile',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='file'),
        ),
    ]
