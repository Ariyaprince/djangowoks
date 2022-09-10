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
    def avg_rating(self):
        all_reviews=self.review_set.all()
        if all_reviews:
            total=sum([r.rating for r in all_reviews])
            return total/len(all_reviews)
        else:
            return 0

class Review(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dishes,on_delete=models.CASCADE)
    review=models.CharField(max_length=120)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])