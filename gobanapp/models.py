from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    about = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=500)
    
    def __str__(self):
        return self.user.username
        
class Job(models.Model):
    CATEGORY_CHOICES = (
    ("GD", "Graphics & Design"),
    ("DM", "Digital Marketing"),
    ("VA", "Video & Animation"),
    ("MA", "Music & Audio"),
    ("PT", "Programming & Tech")
)

    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=50000)
    photo = models.FileField(upload_to='jobs')
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    job = models.ForeignKey(Job)
    buyer = models.ForeignKey(User)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
    
class Review(models.Model):
    job = models.ForeignKey(Job)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return self.content
