from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from .models import *


def home(request):
    all_post = Post.objects.filter(featured=True)
    latest_post = Post.objects.order_by('-date')[0:3]
    context = {
        'all_post':all_post,'latest_post':latest_post,
    }
    return render(request,'index.html',context)

def blog(request):
    blogs = Post.objects.all()
    paginator = Paginator(blogs, 1)
    page_numb = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_numb)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {
        'page_obj':page_obj,
        'page_numb':page_numb,
    }
    return render(request,'blog.html',context)