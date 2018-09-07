from django.db import models
from django.db import models
from datetime import date
from django.contrib.auth.models import  User

#lines = [('EP-1','EP-1'),('EP-2A','EP-2A'),('EP-2B','EP-2B'),('EP-3A','EP-3A'),('EP-3B','EP-3B'),('EP-4','EP-4'),('EP-5A','EP-5A'),('EP-5B','EP-5B'),('EP-6','EP-6'),('EP-7A','EP-7A'),('EP-7B','EP-7B'),('EP-8A','EP-8A'),('EP-8B','EP-8B'),('EP-9','EP-9'),('EP-10','EP-10'),('EP-11A','EP-11A'),('EP-11B','EP-11B'),('EP-12','EP-12'),('EP-13','EP-13'),('EP-14A','EP-14A'),('EP-14B','EP-14B'),('EP-15A','EP-15A'),('EP-15B','EP-15B'),('EP-16A','EP-16A'),('EP-16B','EP-16B'),('EP-17','EP-17'),('EP-18','EP-18'),('EP-19','EP-19'),('EP-20','EP-20'),('EP-21','EP-21'),('EP-22','EP-22')]




class order(models.Model):
    product_name = models.CharField(max_length=200)
    product_details = models.TextField()
    price = models.IntegerField()
    active = models.IntegerField(default='1')

    def __str__(self):
        return '%s (%s tk)' % (self.product_name, self.price)


class select(models.Model):
    sele = models.CharField(max_length= 20)










# Create your models here.
