from django.contrib import admin

from .models import Blogpost, Source

admin.site.register(Blogpost)
admin.site.register(Source)
