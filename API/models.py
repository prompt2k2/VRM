from django.db import models


class APIconnect(models.Model):
    name = models.CharField(max_length=100)
    keys = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name