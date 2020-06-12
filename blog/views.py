from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.db.models.functions import Trunc
from django.contrib.auth import logout as django_logout
from django.contrib import messages

import datetime

from .models import Blogpost, Source

def index(request):

    context = {
        "Blogposts" : Blogpost.objects.all().order_by('-date_posted')
    }

    return render(request, "blog/index.html", context)

def post(request, Blogpost_id):

    if request.method == "GET":

        try:
            post = Blogpost.objects.get(pk=Blogpost_id)
            
        except Blogpost.DoesNotExist:
            raise Http404("This post does not exist")

        context ={
            "Blogpost" : Blogpost.objects.get(pk=Blogpost_id),
            "Sources" : Source.objects.filter(blogpost = Blogpost_id)
        }
    
        return render(request, "blog/post.html", context)

    if request.method == "POST":

        if request.POST.get("sourceLink") and request.POST.get("sourceTitle"):

            blogpost = Blogpost.objects.get(pk=Blogpost_id)
            source = Source()
            source.link = request.POST.get('sourceLink')
            source.title = request.POST.get('sourceTitle')
            source.blogpost = blogpost
            source.save()
            
        return HttpResponseRedirect(request.path_info)

def tools(request):
    
    return render(request, "blog/tools.html")
@login_required
def delete(request, Blogpost_id):
    post = Blogpost.objects.get(pk=Blogpost_id)
    post.delete()
    messages.success(request, 'Post deleted')
    return redirect('/')

@login_required
def deleteSource(request, Blogpost_id, Source_id):

    source = Source.objects.filter(blogpost = Blogpost_id, id = Source_id)
    source.delete()

    return redirect(sources, Blogpost_id=Blogpost_id)

@login_required
def sources(request, Blogpost_id):

    context ={
        "Blogpost" : Blogpost.objects.get(pk=Blogpost_id),
        "Sources" : Source.objects.filter(blogpost = Blogpost_id)
    }

    if request.method == "POST":

        if request.POST.get("sourceLink") and request.POST.get("sourceTitle"):

            blogpost = Blogpost.objects.get(pk=Blogpost_id)
            source = Source()
            source.link = request.POST.get('sourceLink')
            source.title = request.POST.get('sourceTitle')
            source.blogpost = blogpost
            source.save()
                
        return HttpResponseRedirect(request.path_info)

    else:

        return render(request, "blog/sources.html", context)

@login_required
def edit(request, Blogpost_id):

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):

            blogpost=Blogpost.objects.get(pk=Blogpost_id)
            blogpost.title= request.POST.get('title')
            blogpost.subtitle= request.POST.get('subtitle')
            blogpost.author= request.POST.get('author')
            blogpost.content= request.POST.get('content')
            blogpost.img= request.POST.get('img')
            blogpost.save()

            messages.success(request, 'Post edited')
            return redirect('/')

    else :

        try:
            Blogpost.objects.get(pk=Blogpost_id)
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
            blogpost.img= request.POST.get('img')
            blogpost.date_posted= datetime.datetime.now()
            blogpost.save()

            source = Source()
            source.link = request.POST.get('sourceLink')
            source.title = request.POST.get('sourceTitle')
            source.blogpost = blogpost
            source.save()
            
            messages.success(request, 'Post added')


            return redirect('/')

    else :






        return render(request, "blog/add.html")

def contact(request):

    return render(request, "blog/contact.html")