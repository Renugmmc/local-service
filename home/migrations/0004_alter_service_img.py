# Generated by Django 5.0.6 on 2024-07-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
