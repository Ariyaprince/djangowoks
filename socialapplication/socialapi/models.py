from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="profilepic",null=True)
    dob=models.IntegerField()
    cover_pic=models.ImageField(upload_to="coverpics",null=True)
    gender=models.CharField(max_length=120)
    bio=models.CharField(max_length=120)
    following=models.ManyToManyField(User,null=True,related_name="following")


class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
    image=models.ImageField(upload_to="image",null=True)
    date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)



    def __str__(self):
        return self.title
    def fetch_comments(self):
        return self.comments_set.all()

    def like_count(self):
        return self.liked_by.all().count()


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment



