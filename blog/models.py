from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=234)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.pk})

        