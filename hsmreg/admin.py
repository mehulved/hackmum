from hsmreg.models import Event, Users
from django.contrib import admin

admin.site.register(Event)

class UserAdmin(admin.ModelAdmin):
    list_display = ('fullname',)
    list_filter = ('event',)

admin.site.register(Users, UserAdmin)
