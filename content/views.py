from django.shortcuts import render, get_object_or_404
from .models import Content

# Create your views here.

def content_list(request):
    contents = Content.objects.all()

    s = request.GET.get('s','')

    if s:
        contents = contents.filter(title__icontains = s)

    return render(request, 'content/content_list.html', { 'contents': contents, 's':s, })


def content_category(request, category):
    contents_all = Content.objects.all()
    contents = Content.objects.all().filter(category = category)

    s = request.GET.get('s', '')

    if s:
        contents = contents_all.filter(title__icontains = s)

    return render(request, 'content/content_category.html', { 'contents': contents, 's':s, })


def content_register(request):
    return render(request, 'content/content_register.html')


def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    p = request.GET.get('p', '') #p는 user_id로 전달받음
    current_point = int(request.user.profile.point)

    if p:
        if current_point >= int(content.point): #포인트 구현
            current_point = current_point - int(content.point)
            request.user.profile.point = current_point
            request.user.profile.save()

            content.user_set.add(p)



    return render(request, 'content/content_detail.html', { 'content': content, 'p': p })
