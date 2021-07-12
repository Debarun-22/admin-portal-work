from django.db import models
from category.models import Category
from django.urls import reverse
from account.models import Account


class Type(models.Model):
    type_name   =models.CharField(max_length =200,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    category       =models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date   =models.DateTimeField(auto_now_add=True)
    modified_date  =models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)

    def get_url(self):
        return reverse('post',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.type_name

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(max_length=500,blank=True)
    created_date   =models.DateTimeField(auto_now_add=True)
    to_post_date  =models.DateTimeField()
    url = models.URLField(blank=True)
    type_image = models.ImageField(upload_to='photos/type', blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)