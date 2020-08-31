from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='referrer')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='referrer_user')
    is_settled = models.BooleanField(default=False, blank=True, null=True)# this becomes active for the referrer as soon as the referre donates
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "{} - {}".format(self.user.username, self.referrer.username)