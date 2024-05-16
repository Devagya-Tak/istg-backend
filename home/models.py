from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):
  username = models.CharField(max_length=190)

class Question(models.Model):
  user = models.ForeignKey(User, on_delete=CASCADE)
  question = models.CharField(max_length=400)