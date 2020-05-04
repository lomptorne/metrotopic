from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Blogpost

class fixedMap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.9

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['index']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 0.9

    def items(self):
        return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.date_posted
