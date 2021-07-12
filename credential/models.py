from django.db import models
from category.models import Category
from account.models import Account




class Credential(models.Model):
    username   =models.CharField(max_length =200,blank=True)
    email = models.CharField(max_length=100,blank=True)
    phone_no= models.CharField(max_length=20,blank=True)
    password =  models.CharField(max_length=100)
    category       =models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)


    def __str__(self):
        return self.username
