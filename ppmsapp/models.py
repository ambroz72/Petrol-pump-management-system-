from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pydoc import describe

# Create your models here.
class Category(models.Model):       #admin....
    product_category = models.CharField(max_length=100,null=True)
    product_price = models.IntegerField(null=True)
    product_stock = models.IntegerField(null=True)
    
class Report(models.Model):       #user....
    r_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    r_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    r_name=models.CharField(max_length=60)
    r_DOB = models.DateField(null=True)
    r_details=models.CharField(max_length=500,null=True)
    r_quantity = models.IntegerField(null=True)
    
class Employee(models.Model):       #user....
    e_category =models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    e_report = models.ForeignKey(Report, on_delete=models.CASCADE,null=True)
    e_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    e_fname = models.CharField(max_length=30,null=True)
    e_lname = models.CharField(max_length=30,null=True)
    e_address = models.CharField(max_length=100,null=True)
    e_gender = models.CharField(max_length=100,null=True)
    e_age=models.IntegerField(null=True)
    e_phone_numbr = models.BigIntegerField(10,null=True)
    e_email = models.EmailField(null=True)
    e_post=models.CharField(max_length=20,null=True)
    e_photo = models.ImageField(upload_to='image/',null=True)
    e_shift=models.CharField(max_length=30,null=True)
    e_status=models.CharField( max_length=10,null=True)
    
class Attendance(models.Model):
    a_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    a_users=models.ForeignKey(Employee,on_delete=models.PROTECT,null=True)
    a_attendnce=models.CharField(max_length=30,null=True)
    a_DOB=models.DateField(null=True)
    a_post=models.CharField(max_length=30,null=True)
    a_shift=models.CharField(max_length=30,null=True)
    a_status=models.CharField( max_length=10,null=True)

class Leave(models.Model):
    l_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    l_users = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    l_req=models.CharField(max_length=50,null=True)
    l_reason=models.CharField(max_length=100)
    l_DOB=models.DateField(null=True)
    l_status=models.CharField(max_length=10,null=True)
    
class Feedback(models.Model):
    f_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    f_users = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    f_name=models.CharField(max_length=50,null=True)
    f_feed=models.CharField(max_length=100,null=True)
    f_DOB=models.DateField(null=True)
    f_status=models.CharField(max_length=30,null=True)
    
class Review(models.Model):
    re_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    re_users=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    re_name=models.CharField(max_length=20,null=True)
    re_feed=models.CharField(max_length=100,null=True)
    re_post=models.CharField(max_length=20,null=True)
    re_DOB=models.DateField(null=True)
    re_status=models.CharField(max_length=20,null=True)
    
