from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return self.slackUsername
