from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.db.models.functions import Trunc
from django.contrib.auth import logout as django_logout
from django.contrib import messages

import datetime
from .models import Blogpost


def index(request):

    context = {
        "Blogposts" : Blogpost.objects.all().order_by('-date_posted')
    }

    return render(request, "blog/index.html", context)

def post(request, Blogpost_id):

    try:
        post = Blogpost.objects.get(pk=Blogpost_id)
    except Blogpost.DoesNotExist:
        raise Http404("This post does not exist")

    context ={
        "Blogpost" : Blogpost.objects.get(pk=Blogpost_id)
    }

    return render(request, "blog/post.html", context)

@login_required
def delete(request, Blogpost_id):
    post = Blogpost.objects.get(pk=Blogpost_id)
    post.delete()
    messages.success(request, 'Post deleted')
    return redirect('/')

@login_required
def edit(request, Blogpost_id):

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):

            blogpost=Blogpost.objects.get(pk=Blogpost_id)
            blogpost.title= request.POST.get('title')
            blogpost.subtitle= request.POST.get('subtitle')
            blogpost.author= request.POST.get('author')
            blogpost.content= request.POST.get('content')
            blogpost.date_posted= datetime.datetime.now()
            blogpost.save()

            messages.success(request, 'Post edited')
            return redirect('/')

    else :

        try:
            post = Blogpost.objects.get(pk=Blogpost_id)
        except Blogpost.DoesNotExist:
            raise Http404("This post does not exist")

        context ={
            "Blogpost" : Blogpost.objects.get(pk=Blogpost_id)
        }

        return render(request, "blog/edit.html", context)



@login_required
def logout(request):

    django_logout(request)

    return HttpResponseRedirect('/')

@login_required
def add(request):

    if request.method == "POST":

        if request.POST.get('title') and request.POST.get('content'):

            blogpost=Blogpost()
            blogpost.title= request.POST.get('title')
            blogpost.subtitle= request.POST.get('subtitle')
            blogpost.author= request.POST.get('author')
            blogpost.content= request.POST.get('content')
            blogpost.date_posted= datetime.datetime.now()
            blogpost.save()

            messages.success(request, 'Post added')
        return redirect('/')

    else :






        return render(request, "blog/add.html")
