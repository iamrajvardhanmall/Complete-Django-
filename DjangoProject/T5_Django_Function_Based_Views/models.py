from django.db import models

# Declare a new model with a name "raj"
class raj(models.Model):
    # field of the model
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # renames the instance of the model with their title name
    def __str__(self):
        return self.title
    
