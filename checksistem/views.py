from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
from collections import defaultdict


def index(request):
    return render(request, "checksistem/index.html", {})


def cards(request):
    return render(request, "checksistem/cards.html", {})


def groups(request):
    return render(request, "checksistem/groups.html", {})


def employe(request):
    return render(request, "checksistem/employe.html", {})
