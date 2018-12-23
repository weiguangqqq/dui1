from django.db import models
from django.conf import settings

from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	
    def __str__(self):
    	return 'Profile for user {}'.format(self.user.username)


# Create your models here.
class lostitem(models.Model):
    lostid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10)
    claimpla = models.CharField(max_length=20)
    issuedate = models.DateTimeField(default=timezone.now)
    info = models.CharField(max_length=50)
    class Meta:
           ordering = ('-issuedate',)

    def __int__(self):
        return self.id
    