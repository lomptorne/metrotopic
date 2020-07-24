from django.contrib import admin

from .models import Blogpost, Source, Image

admin.site.register(Blogpost)
admin.site.register(Source)
admin.site.register(Image)
