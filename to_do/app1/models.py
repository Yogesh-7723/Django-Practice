from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    due_date = models.DateField(default=None,null=True,blank=True)
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.task_name