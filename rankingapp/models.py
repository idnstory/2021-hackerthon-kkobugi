from django.db import models

# Create your models here.

class Ranking(models.Model):
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(null=False)
    created = models.DateTimeField('created', auto_now_add=True)
