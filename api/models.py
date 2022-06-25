from django.conf import settings
from django.db import models
from django.utils import timezone


class Users(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #title = models.CharField(max_length=200)
    #text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    #def publish(self):
       # self.published_date = timezone.now()
        #self.save()

    def __str__(self):
        return self.first_name

class Customers(models.Model):
  
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Orders(models.Model):
  
    item = models.CharField(max_length=40, blank=True, null=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    time = models.TimeField()

    def __str__(self):
        return self.item