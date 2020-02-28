from django.utils import timezone
from django.db import models
from datetime import datetime


class Artist(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default='enter location...')

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default='enter location...')
#     name = models.models.CharField(_(""), max_length=30)
#     location = models.models.CharField(_(""), max_length=30)

    def __str__(self):
        return self.name


class Engineer(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default='enter location...')

#     name = models.models.CharField(_(""), max_length=30)
#     location = models.models.CharField(_(""), max_length=30)
    def __str__(self):
        return self.name


class Session(models.Model):
    appointment_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=False)
    duration = models.PositiveIntegerField(default=30, verbose_name='minutes')

#     name = models.models.CharField(_(""), max_length=30)
#     location = models.models.CharField(_(""), max_length=30)
    def __str__(self):
        return self.appointment_date
