from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Count,Q
from .forms import CommentForm

def searchQ(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    context ={
        'queryset':queryset,
    }
    return render(request,'search.html',context)

def get_category_count():
    queryset = Post.objects.values('post_category__name').annotate(Count('post_category__name'))
    return queryset

def home(request):
    all_post = Post.objects.filter(featured=True)
    latest_post = Post.objects.order_by('-date')[0:3]
    context = {
        'all_post':all_post,'latest_post':latest_post,
    }
    return render(request,'index.html',context)

def blog(request):
    blogs = Post.objects.all()
    recent_post = Post.objects.order_by('-date')[0:3]
    category_count = get_category_count()
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
        'recent_post':recent_post,
        'category_count':category_count,
    }
    return render(request,'blog.html',context)

def details(request,pk):
    recent_post = Post.objects.order_by('-date')[0:3]
    category_count = get_category_count()
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect('/')
  
    context ={
        'post':post,
        'recent_post':recent_post,
        'category_count':category_count,
        'form':form,
    }
    return render(request,'post.html',context)