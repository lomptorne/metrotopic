from django.db import models


class Blogpost(models.Model):


    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_posted = models.DateTimeField('date published')
    img = models.CharField(max_length=200)
    content =models.TextField()

    def get_absolute_url(self):
        return '/'+str(self.id)

