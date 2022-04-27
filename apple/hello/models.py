from django.db import models
from django.forms import forms
from django.urls import reverse


class Postusers(models.Model):
    username = models.CharField(max_length=250, verbose_name="Username")
    email = models.EmailField(max_length=30, verbose_name="Email")
    password = models.CharField(max_length=20, verbose_name="Password")
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    city = models.CharField(max_length=30, verbose_name="City")
    address = models.CharField(max_length=30, verbose_name="Address")

    def __str__(self):
        return self.username


