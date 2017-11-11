from django.contrib import admin
from .models import Profile, Job, Purchase, Review

# Register your models here.
admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Purchase)
admin.site.register(Review)