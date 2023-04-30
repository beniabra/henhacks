from django.shortcuts import render, redirect
from .models import Resource, Post
from django.http import HttpResponse

def home(response):
    return render(response, "finance_resources/home.html")

def find_matches(response):
    return render(response, "finance_resources/find_matches.html")

def all_resources(response):
    resources = Resource.objects.all()
    return render(response, "finance_resources/all_resources.html", {"resources": resources})

def discussion_forum(response):
    posts = Post.objects.all()
    return render(response, "finance_resources/discussion_forum.html", {"posts": posts})

def newPost(response):
    if response.method == "POST":
        if response.POST.get("name"):
            person = response.POST.get('name')
        if response.POST.get('comment'):
            comment = response.POST.get('comment')
        p = Post.objects.create(name=person, description=comment)
        p.save()
    return redirect(discussion_forum)