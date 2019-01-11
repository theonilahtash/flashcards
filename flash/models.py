from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    profile = models.ImageField(upload_to='profile_image',blank=True)
    username =models.CharField(max_length=30)
    bio = models.CharField(max_length=100,null=True)
    contacts = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

class  Card(models.Model):
    user = models.ForeignKey(User,blank=True,null=True)
    subject = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    short_notes = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


    @classmethod
    def search_by_subject(cls,search_term):
        subject = cls.objects.filter(title_icontains=search_term)
        return subject

    def save_card(self):
        self.save()
        
    def delete_card(self):
        self.delete()

    def update_card(self):
        self.update()