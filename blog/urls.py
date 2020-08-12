from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import BlogSitemap, fixedMap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'Blogpost': BlogSitemap,
    'static': fixedMap,
}

urlpatterns = [
    
    path('', views.index, name='index'),
    path("<int:Blogpost_id>", views.post, name="post"),
    path("edit/<int:Blogpost_id>", views.edit, name="edit"),
    path("delete/<int:Blogpost_id>", views.delete, name="delete"),
    path("<int:Blogpost_id>/sources/deleteSource/<int:Source_id>", views.deleteSource, name="deleteSource"),
    path("<int:Blogpost_id>/sources", views.sources, name="sources"),
    path('logout', views.logout, name="logout"),
    path('add', views.add, name="add"),
    path('contact', views.contact, name="contact"),
    path('motivateur', views.motivateur, name="motivateur"),

    path('generator', views.generator, name="generator"),
    path('scrambbler', views.scrambbler, name="scrambbler"),
    path('imgupload', views.imgupload, name="imgupload"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)