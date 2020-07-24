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

    pass

class Source(models.Model):

    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

class Image(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):

        return self.nam