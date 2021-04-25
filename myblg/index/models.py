from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class author(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    details=RichTextField(blank=False)
    profile_pic=models.ImageField()
    facebook=models.CharField(max_length=500,blank=True)
    instagram=models.CharField(max_length=500,blank=True)
    twitter=models.CharField(max_length=500,blank=True)
    linkedin=models.CharField(max_length=500,blank=True)
    github=models.CharField(max_length=500,blank=True)
    stack_overflow=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.name.username
class categary(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class artical(models.Model):

   
    
    artical_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=RichTextUploadingField(blank=False)
    categary=models.ForeignKey(categary,on_delete=models.CASCADE)
    posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
    image=models.ImageField()
    def __str__(self):
        return self.title
    def getmyartical(self):
        return reverse('mainblogapp:single_post',kwargs={"id":self.id})
    def get_author_url(self):
        return reverse('mainblogapp:author',kwargs={"name": self.artical_author.name.username})
    def get_cat_url(self):
        return reverse('mainblogapp:categary',kwargs={"name": self.name})
    


class comment(models.Model):
    post=models.ForeignKey(artical,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100, blank=False)
    email=models.CharField(max_length=200,blank=True)
    post_comment=RichTextField(blank=False)

    def __str__(self):

        return self.post_comment

  
