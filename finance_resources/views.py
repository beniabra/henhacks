from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response, "finance_resources/home.html")

def find_matches(response):
    return render(response, "finance_resources/find_matches.html")

def all_resources(response):
    return render(response, "finance_resources/all_resources.html")

def discussion_forum(response):
    return render(response, "finance_resources/discussion_forum.html")