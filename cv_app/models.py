from random import choices
from statistics import mode
from django.db import models

STATE_CHOICE = ((

    ('KOTTAYAM','KOTTAYAM'),
    ('THRISHUR','THRISHUR'),
    ('ERANAKULAM','ERANAKULAM'),

))

# Create your models here.
class prof(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False,auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE,max_length=50)
    gender= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    piimage= models.ImageField(upload_to='pimages', blank=True)
    docfile= models.FileField(upload_to='docfiles', blank=True)