from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="profilepic")
    phone=models.IntegerField()
    dob=models.IntegerField()
    address=models.CharField()

class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
    image=models.ImageField(upload_to="image")
    date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    



