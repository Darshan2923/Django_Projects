from django.db import models

# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
        # return self.body[0:69]
    
    class Meta:
        ordering=['title']

# class Title(models.Model):
#     title=models.CharField(max_length=200)
#     pub_date=models.DateTimeField('date_published',auto_now_add=True)

#     def __str__(self):
#         return self.title
    
# class Description(models.Model):
#     title=models.ForeignKey(Title,on_delete=models.CASCADE)
#     description=models.CharField(max_length=200)

#     def __str__(self):
#         return self.description

