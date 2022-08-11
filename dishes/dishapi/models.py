from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Dishes(models.Model):
    name=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=120)


    def __str__(self):
        return self.name

class Review(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dishes,on_delete=models.CASCADE)
    review=models.CharField(max_length=120)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])