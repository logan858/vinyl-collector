from django.contrib import admin

# Register your models here.

from .models import Vinyl, Listen, StoreTwo
admin.site.register(Vinyl)
admin.site.register(Listen)
admin.site.register(StoreTwo)
