from django.db import models

# Create your models here.

class Table_details(models.Model):
    day = models.CharField(max_length=60)
    time = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    sclass = models.CharField(max_length=100)
    dname = models.CharField(max_length=100)
