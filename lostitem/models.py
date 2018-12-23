from django.db import models

from django.utils import timezone

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


class finditem(models.Model):
    findid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10)
    tele = models.CharField(max_length=20)
    lostpla = models.CharField(max_length=20)
    issuedate = models.DateTimeField(default=timezone.now)
    info = models.CharField(max_length=50)
    class Meta:
           ordering = ('-issuedate',)

    def __int__(self):
        return self.id