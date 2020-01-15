from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
