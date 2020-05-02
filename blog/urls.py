from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("<int:Blogpost_id>", views.post, name="post"),
    path("edit/<int:Blogpost_id>", views.edit, name="edit"),
    path("delete/<int:Blogpost_id>", views.delete, name="delete"),
    path('logout', views.logout, name="logout"),
    path('add', views.add, name="add"),
    
]
