from django.contrib import admin
from .models import leave,teacher,userprofile

# Register your models here.

admin.site.register(teacher)
admin.site.register(leave)
admin.site.register(userprofile)
