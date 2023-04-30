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

def likePost(response, id):
    p = Post.objects.get(id=id)
    p.likes += 1
    p.save()
    return redirect(discussion_forum)

def results(response):
    if response.method == "POST":
        print(response.POST)
        valid = False
        category = ''
        if response.POST.get('name'):
            name = response.POST.get('name')
        if response.POST.get('age'):
            elderly = int(response.POST.get('age')) >= 65
        if response.POST.get('income'):
            if response.POST.get('income') == '...': 
                valid = True
            else: 
                if response.POST.get('income') == 'less' or response.POST.get('income') == 'middle':
                    valid = True
                else:
                    valid = False
        if response.POST.get('category'):
            category = response.POST.get('category')
    resources = []
    if valid:
        all_resources = Resource.objects.all()
        resources = all_resources.filter(categories__icontains=category)
        if not elderly:
            resources = resources.exclude(categories__icontains="elderly")
     
    return render(response, "finance_resources/results.html", {"valid": valid, "resources": resources} )