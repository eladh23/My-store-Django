# Generated by Django 3.2.20 on 2023-10-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_proj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
