from django.db import models
from django.db.models.base import ModelState
import uuid

from django.db.models.deletion import CASCADE

# Create your models here.

################# Main DataBase Information #################

################# Main Table  #################
class Asset(models.Model):
    serverName = models.CharField(max_length=200)
    serverIp = models.CharField(max_length=50)
    serverType = models.CharField(max_length=50)
    serverRole = models.CharField(max_length=50)
    serverNote = models.TextField(null=True, blank=True)
    idrac_ip = models.CharField(max_length=50, null=True, blank=True)
    idrac_User = models.CharField(max_length=50, null=True, blank=True)
    idrac_Passwd = models.CharField(max_length=50, null=True, blank=True)
    locationsInfo = models.ManyToManyField('Locations')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.serverName

################# Location Table information many to many relantionship to Main Table Asset #################
class Locations(models.Model):
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    siteAddress = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.country