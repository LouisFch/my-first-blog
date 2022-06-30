from django.db import models

class param(models.Model):
    Running=models.BooleanField()
    MachineName=models.CharField(max_length=10)

class three(models.Model):
    Running=models.BooleanField()
    MachineName=models.CharField(max_length=10)