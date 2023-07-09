from django.contrib import admin
from .models import Event, Admin, Organizer, User

# Register your models here.

admin.site.register(Event)
admin.site.register(Admin)
admin.site.register(Organizer)
admin.site.register(User)


admin.site.site_header = "Event Lanka Administration"

