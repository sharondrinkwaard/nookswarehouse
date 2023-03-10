from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

COUNTRIES = (
    ('Netherlands', 'Netherlands'),
    ('Belgium', 'Belgium'),
)


class UserProfile(models.Model):
    ''' A user profile for maintaining default info and order history'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(choices=COUNTRIES, max_length=40, null=True, blank=True, default='Netherlands')
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    default_house_number = models.CharField(max_length=10, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def make_or_update_user_profile(sender, instance, created, **kwargs):
    ''' Make or update user profile '''
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
