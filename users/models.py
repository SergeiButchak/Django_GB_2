from datetime import datetime, timedelta

import pytz
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from geekshop import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True)

    def is_activation_key_expired (self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) < (self.activation_key_created + timedelta(hours=48)):
            return False
        return True


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, db_index=True)
    tagline = models.CharField(max_length=150, blank=True)
    about_me = models.TextField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, max_length=1)
    age = models.PositiveIntegerField(default=18)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()