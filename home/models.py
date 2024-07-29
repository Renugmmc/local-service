from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('providers', 'Providers'),
        ('customer', 'Customer'),
    ]

    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Fact(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    description = models.TextField()

class Service(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    date = models.DateField()
    status = models.BooleanField(default=True)
    

















