from django.shortcuts import render
from .models import Blog, Comment, Category, Tag, Banner
from django.core.paginator import Paginator
from django.db.models import Count, Sum

def blog(request):
    search = request.GET.get('search')
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    author = request.GET.get('author')
    if search:
        blogs = Blog.objects.filter(title__contains = search).annotate(total_comments = Count('comments')).order_by("-id")
        paginator = Paginator(blogs,8)
        page_number = request.GET.get("page")
        blog_obg = paginator.get_page(page_number)
    elif author:
        blogs = Blog.objects.filter(author = author).annotate(total_comments = Count('comments')).order_by("-id")
        paginator = Paginator(blogs,8)
        page_number = request.GET.get("page")
        blog_obg = paginator.get_page(page_number)
    elif category:
        blogs = Blog.objects.filter(category = category).annotate(total_comments = Count('comments')).order_by("-id")
        paginator = Paginator(blogs,8)
        page_number = request.GET.get("page")
        blog_obg = paginator.get_page(page_number)
    elif tag:
        blogs = Blog.objects.filter(tages = tag).annotate(total_comments = Count('comments')).order_by("-id")
        paginator = Paginator(blogs,8)
        page_number = request.GET.get("page")
        blog_obg = paginator.get_page(page_number)
    else:
        blogs = Blog.objects.annotate(total_comments = Count('comments')).order_by("-id")
        paginator = Paginator(blogs,8)
        page_number = request.GET.get("page")
        blog_obg = paginator.get_page(page_number)
    categories = Category.objects.filter(parent = None).annotate(total_blogs = Count('blogs'), total_categories = Count('categories'))
    alt_categories = Category.objects.exclude(parent = None).annotate(total_blogs = Count('blogs'),)
    tages = Tag.objects.all()
    recent_posts = Blog.objects.all().order_by('-id')[0:3]
    banner = Banner.objects.first()
    return render(request, 'blog.html', {"blog_obg": blog_obg, "categories": categories, "alt_categories": alt_categories, "tages": tages, "recent_posts" :recent_posts, "banner": banner})

def blog_detail(request, id):
    blog = Blog.objects.get(id = id)
    categories = Category.objects.filter(parent = None).annotate(total_blogs = Count('blogs'), total_categories = Count('categories'))
    alt_categories = Category.objects.exclude(parent = None).annotate(total_blogs = Count('blogs'),)
    blog_tages = Tag.objects.filter(blogs = blog)
    tages = Tag.objects.all()
    recent_posts = Blog.objects.all().order_by('-id')[0:3]
    banner = Banner.objects.first()
    comments = Comment.objects.filter(blog = blog)
    blogs_count = Blog.objects.count()
    related_posts = Blog.objects.filter(category = blog.category).exclude(id=id).annotate(total_comments = Count('comments')).order_by("-id")
    return render(request, 'blog-detail.html', {"blog": blog,"blogs_count":blogs_count, "related_posts": related_posts, "comments": comments,  "categories": categories, "alt_categories": alt_categories, "tages": tages, "blog_tages": blog_tages, "recent_posts" :recent_posts, "banner": banner})