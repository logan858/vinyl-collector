from django.contrib import admin

# Register your models here.

from .models import Vinyl, Listen
admin.site.register(Vinyl)
admin.site.register(Listen)
