from django.contrib import admin

from manager.models import Country, CreateEvent, Holidays, ProfileUser

admin.site.register(Country)
admin.site.register(CreateEvent)
admin.site.register(Holidays)
admin.site.register(ProfileUser)
# Register your models here.
