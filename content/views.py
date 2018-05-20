from django.shortcuts import render
from .models import Content

# Create your views here.

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content/content_list.html', { 'contents': contents })