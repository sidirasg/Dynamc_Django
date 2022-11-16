from django.db import models

# Create your models here.
class  Stident(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    test_score = models.FloatField()  
    
    
    def __str__(self):
        return self.name8