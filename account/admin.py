from django.contrib import admin

# Register your models here.
from .models import lostitem
class lostitemAdmin(admin.ModelAdmin):
    list_display=('lostid','category','claimpla','issuedate','info')
admin.site.register(lostitem,lostitemAdmin)