from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)
    price = models.CharField(max_length=50)
    product_details = models.TextField()

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.pk)]) 
        
    