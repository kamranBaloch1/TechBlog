from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=200,default="No title")
    category = models.CharField(max_length=50,default="No category")
    desc = models.TextField(max_length=10000,default="No desc")
    Mdescimg = models.ImageField(upload_to='images/blogImg',default='TechBlog\static\img\default.png')
    Mdesc = models.TextField(max_length=10000,default='Empty')
    Mdesctitle = models.CharField(max_length=200,default='Empty')
    MMdescimg = models.ImageField(upload_to='images/blogImg',default='TechBlog\static\img\default.png')
    MMdesc = models.TextField(max_length=10000,default='Empty')
    MMdesctitle = models.CharField(max_length=200,default='Empty')
    Moredescimg = models.ImageField(upload_to='images/blogImg',default='TechBlog\static\img\default.png')
    Moredesc = models.TextField(max_length=10000,default=' Empty')
    Moredesctitle = models.CharField(max_length=200,default='Empty')
    Date = models.DateField(default=date.today)
    img = models.ImageField(upload_to='images/blogImg')
    
    def __str__(self):
        return  self.title


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=5000)
    Date = models.DateField(default=date.today)
    email = models.CharField(max_length=50,default="NO email")
    number = models.CharField(max_length=20)

    def __str__(self):
        return  self.message

class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blogs, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    Date = models.DateField(default=date.today)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    
        
class Carosel(models.Model):
    carouselimg1 = models.ImageField(upload_to='images/blogImg',default='TechBlog\static\img\default.png')
    carouselimg2 = models.ImageField(upload_to='images/blogImg',default='TechBlog\static\img\default.png')
    carouselimg3 = models.ImageField(upload_to='images/blogImg',default='TechBlog\static\img\default.png')