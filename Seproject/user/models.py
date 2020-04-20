from django.db import models


# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=30, default="learn")
    raiting = models.IntegerField(default=0)
    status = models.CharField(max_length=30, default='learn')


class User(models.Model):
    name = models.CharField(max_length=300)
    availability = models.CharField(max_length=300)
    reviews = models.TextField()
    email = models.TextField()
    gender = models.TextField()
    age = models.IntegerField()
    skill = models.ForeignKey(Skill, to_field='id', on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=50, default='user')
    rait = models.IntegerField(default=0)
