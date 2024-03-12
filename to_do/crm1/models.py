from django.db import models
import datetime
import os

# Create your models here.

def name_date(instance,filename):
    old_name = filename 
    add = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s"%(add,old_name)
    return os.path.join("crm/",filename)

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    contect = models.CharField(max_length=12)
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    year_sem = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=20)
    result = models.ImageField(upload_to=name_date,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    