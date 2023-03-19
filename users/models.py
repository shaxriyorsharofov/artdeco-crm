from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    number = models.CharField(max_length=200, blank=True, null=True)
    course_name = models.CharField(max_length=200, blank=True, null=True)
    course_percentage = models.CharField(max_length=200, blank=True, null=True)
    discount = models.CharField(max_length=200, blank=True, null=True)
    discount_percentage = models.CharField(max_length=200, blank=True, null=True)
    money_paid = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ,{self.first_name}, {self.course_name}"


class CheckImage(models.Model):
    check_user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.check_user.username)


class Saved(models.Model):
    pass
    # products = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # date = models.DateField(auto_now_add=True)