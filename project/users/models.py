from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()

def valid_subscription(self):
    return False

User.add_to_class('valid_subscription', valid_subscription)

@receiver(pre_save, sender=User)
def set_username_to_email(sender, instance, **kwargs):
    instance.username = instance.email
