# Generated by Django 4.1.13 on 2024-03-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]