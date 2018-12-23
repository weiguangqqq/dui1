
# Register your models here.
from django.contrib import admin
# Register your models here.

from .models import lostitem,finditem
class lostitemAdmin(admin.ModelAdmin):
    list_display=('lostid','category','claimpla','issuedate','info')
admin.site.register(lostitem,lostitemAdmin)

class finditemAdmin(admin.ModelAdmin):
    list_display=('findid','category','tele','lostpla','issuedate','info')
admin.site.register(finditem,finditemAdmin)