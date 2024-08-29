from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField()