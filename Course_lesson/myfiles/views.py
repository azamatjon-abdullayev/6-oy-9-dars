from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .add_flower import *
from .models import *
# Create your views here.

def index(request: WSGIRequest):
    posts = Lesson.objects.filter(published=True)
    context = {
        "posts": posts,
        "title": "Barcha maqolalar"
    }
    return render(request, "index.html", context)


def posts_by_category(request, category_id):
    posts = get_list_or_404(Lesson, category_id=category_id, published=True)
    category = get_object_or_404(Course, pk=category_id)
    context = {
        'posts': posts,
        "title": f"{category.name}: barcha maqolalar!"
    }
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Lesson, pk=post_id, published=True)
    post.views += 1
    post.save()

    context = {
        "post": post,
        "title": post.title
    }
    return render(request, 'detail.html', context)

def add_flower(request: WSGIRequest):
    if request.method == "POST":
        form = Gullarforms(data=request.POST,files=request.FILES)
        if form.is_valid():
            gul = Lesson.objects.create(**form.cleaned_data)
            print(gul,"qo'shildi")
    gul = Gullarforms()
    context = {
        "gul":gul
    }
    return render(request,'flower.html',context)