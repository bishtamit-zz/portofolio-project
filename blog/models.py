from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()#auto_now_add=True, auto_now=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')