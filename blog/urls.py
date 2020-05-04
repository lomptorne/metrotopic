from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import BlogSitemap, fixedMap

sitemaps = {
    'Blogpost': BlogSitemap,
    'static': fixedMap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:Blogpost_id>", views.post, name="post"),
    path("edit/<int:Blogpost_id>", views.edit, name="edit"),
    path("delete/<int:Blogpost_id>", views.delete, name="delete"),
    path('logout', views.logout, name="logout"),
    path('add', views.add, name="add"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
