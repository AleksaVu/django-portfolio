from datetime import datetime
from django.db import models


class Post(models.Model):
    """ A model of a blog post """

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/", blank=True, default='')
    body = models.TextField(max_length=100000)

    def __str__(self):
        """String representation of single project """
        return f'{self.title}'

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    """ A model of a single comment """
    
    nickname = models.CharField(max_length=200)
    comment = models.TextField(max_length=5000)
    date = models.DateTimeField(default=datetime.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        """String representation of single project """
        return f'{self.post}' + " " + f'{self.date}' 
    
    class Meta:
        ordering = ['id']
