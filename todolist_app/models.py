from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):    #Tasklist table at database
    id = models.AutoField(primary_key=True)
    tasks = models.CharField(max_length = 300)
    done = models.BooleanField(default = False)
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.tasks + '-' + str(self.done)
    

    