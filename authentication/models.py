from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import Referral


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(default='uploads/profile_pic/default_pic.jpg', upload_to="uploads/profile_pic", blank=True, null=True)
    account_name = models.CharField(max_length=300, blank=True, null=True)
    account_number= models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=300, blank=True, null=True)
    is_referred = models.BooleanField(default=False, null=True, blank=True)
    has_referred = models.IntegerField(default=0, blank=True, null=True)
    referral_balance = models.IntegerField(default=0, blank=True, null=True)
    referred_active = models.IntegerField(default=0, blank=True, null=True)#number to determine wether withdraw button will be active
    referral_code = models.CharField(max_length=100, null=True, blank=True)
    has_withdrawn = models.BooleanField(default=False, null=True, blank=True)#once this is True, the withdraw field becomes readonly

    def __str__(self):
        return str(self.user.username)

def profileCreate(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, referral_code=instance.username)
        print('profile created')
post_save.connect(profileCreate, sender=User)

# def profileUpdate(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
# post_save.connect(profileUpdate, sender=User)

