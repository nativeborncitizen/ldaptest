#coding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ip = models.CharField(max_length=30, blank=True)


def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)