from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField

from users.models import User


# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    # file_doc = models.FileField(upload_to='doc_uploaded/', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    
    
class File_Doc(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    file_doc = models.FileField(upload_to='doc_uploaded/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title



class News(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    news_image = models.ImageField(upload_to='news_image/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('Comment of' + self.author.username)




