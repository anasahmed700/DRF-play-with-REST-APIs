from django.contrib.auth.models import User
from django.db.models.signals import post_save
# receiver will receive the signal using receiver decorator
from django.dispatch import receiver
from .models import Profile

#  when a user instance get saved a signal will sent to receiver
# this function will receive the signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('Created: ', created)  # when a new profile is created this block will run
    if created:
        Profile.objects.create(user=instance)
