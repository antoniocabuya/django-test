from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog/images')
    date = models.DateTimeField(datetime.date.today)
    
    def __str__(self) -> str:
        return self.title