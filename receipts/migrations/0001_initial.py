# Generated by Django 4.0.4 on 2022-04-13 07:46

from django.db import migrations, models
import django.db.models.deletion
import receipts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ReceiptFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=receipts.models.file_upload)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='receipts.receipt')),
            ],
        ),
    ]
