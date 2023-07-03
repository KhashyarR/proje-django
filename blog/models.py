from django.db import models
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])

class User(models.Model):
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    phone = models.CharField(max_length=11,null=False,blank=False,)
    email = models.EmailField(max_length=80,null=False,blank=False)
    skills = models.TextField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self): 
        return reverse('user_detail', args=[str(self.id)])
