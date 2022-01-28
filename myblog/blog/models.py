from datetime import datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    """ A model of a blog post """
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField()
    body = models.TextField(max_length=100000)
    
    def __str__(self):
        """String representation of single project """        
        return f'{self.name}'
    
    