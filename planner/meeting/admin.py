from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Meeting, Room
# Register your models here.

admin.site.register(Meeting)
admin.site.register(Room)