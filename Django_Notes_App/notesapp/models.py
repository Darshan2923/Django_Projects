from django.db import models

# Create your models here.

class Title(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date_published')

    def __str__(self):
        return self.title
    
class Description(models.Model):
    title=models.ForeignKey(Title,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.desccription

