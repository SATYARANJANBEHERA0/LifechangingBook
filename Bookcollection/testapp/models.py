from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Price = models.IntegerField()
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
