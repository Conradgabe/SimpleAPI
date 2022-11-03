from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('addition', 'addition'),
    ('subtraction', 'subtraction'),
    ('multiplication', 'multiplication'),
)

class Profile(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return self.slackUsername

class Operations(models.Model):
    slackUsername = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    operation_type = models.CharField(max_length=14, choices=CHOICES, default='+')
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return self.operation_type
