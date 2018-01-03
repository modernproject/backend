from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def set_username_to_email(sender, instance, **kwargs):
    instance.username = instance.email
