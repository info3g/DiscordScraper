from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(recent)
admin.site.register(search)