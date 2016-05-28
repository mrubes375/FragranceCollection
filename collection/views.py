from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Fragrance
import urllib, io
from PIL.Image import Image

def index(request):
    context_dict = {'All': Fragrance.objects.all()}
    return render(request, 'collection/index.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'collection/about.html', context=context_dict)

def create(request):
    context_dict = {}
    return render(request, 'collection/create.html', context=context_dict)

def detail(request):
    object = get_object_or_404(Fragrance, name="Original Santal")
    context_dict = {"title": object.name, "instance": object}
    return render(request, 'collection/detail.html', context=context_dict)

def update(request):
    context_dict = {}
    return render(request, 'collection/update.html', context=context_dict)
def delete(request):
    context_dict = {}
    return render(request, 'collection/delete.html', context=context_dict)
