from django.db import models
from pygments.lexers import get_all_lexers


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class Project(models.Model):
    """ A model of a project """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    completed = models.BooleanField(default=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    link = models.URLField(default='', max_length=300)
    
    def __str__(self):
        """String representation of single project """        
        return f'{self.name}'

    class Meta:
        ordering = ['completed']
        
        
class Member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    
    def __str__(self):
        """String representation of single project member """        
        return f'{self.name}'
    