from datetime import datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    """ A model of a blog post """
    
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to ="images/", blank=False, null=True)
    body = models.TextField(max_length=100000, blank=True)
    
    def __str__(self):
        """String representation of single project """        
        return f'{self.title}'
    
    class Meta:
        ordering = ['id']
    
    