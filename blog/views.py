from django.shortcuts import render, redirect
from .models import Blog, Comment, Category, Tag, Banner
from django.core.paginator import Paginator
from django.db.models import Count, Sum
from rest_framework.generics import ListCreateAPIView
from .serializers import CommentSerializer
from . forms import CommentForm
def blog(request):
    search = request.GET.get('search')
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    author = request.GET.get('author')
    if search:
        blogs = Blog.objects.filter(title__contains = search)
        
    elif author:
        blogs = Blog.objects.filter(author = author)
       
    elif category:
        blogs = Blog.objects.filter(category = category)
       
    elif tag:
        blogs = Blog.objects.filter(tages = tag)
       
    else:
        blogs = Blog.objects.all()
    blogs = blogs.annotate(total_comments = Count('comments')).order_by("-id")
    paginator = Paginator(blogs,8)
    page_number = request.GET.get("page")
    blog_obg = paginator.get_page(page_number)    
    categories = Category.objects.filter(parent = None).annotate(total_blogs = Count('blogs') ,total_blogs_for_alt_category = Count('categories__blogs'), total_categories = Count('categories'))
    alt_categories = Category.objects.exclude(parent = None).annotate(total_blogs = Count('blogs'))
    print(alt_categories)
    tages = Tag.objects.all()
    recent_posts = Blog.objects.all().order_by('-id')[0:3]
    banner = Banner.objects.first()
    return render(request, 'blog.html', {"blog_obg": blog_obg, "categories": categories, "alt_categories": alt_categories, "tages": tages, "recent_posts" :recent_posts, "banner": banner})

def blog_detail(request, id, comment_id = None):
    blog = Blog.objects.get(id = id)
    categories = Category.objects.filter(parent = None).annotate(total_blogs = Count('blogs'), total_categories = Count('categories'))
    alt_categories = Category.objects.exclude(parent = None).annotate(total_blogs = Count('blogs'),)
    blog_tages = Tag.objects.filter(blogs = blog)
    tages = Tag.objects.all()
    recent_posts = Blog.objects.all().order_by('-id')[0:3]
    banner = Banner.objects.first()
    comment_count = Comment.objects.filter(blog = blog).count()
    blogs_count = Blog.objects.count()
    related_posts = Blog.objects.filter(category = blog.category).exclude(id=id).annotate(total_comments = Count('comments')).order_by("-id")
    comments = Comment.objects.filter(blog = blog, parent = None)
    print(comment_id)
    paginator = Paginator(comments,6)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)
    if request.method == "POST":
        print(comment_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.blog = blog
            if request.user.is_authenticated:
                comment.author = request.user
                comment.name = f'{request.user.first_name} {request.user.last_name}'            
            if comment_id:
                comment.parent = Comment.objects.get(id = comment_id).author
            comment.save()
            return redirect(blog.get_absolute_url())
    return render(request, 'blog-detail.html', {"blog": blog,"blogs_count":blogs_count,"comment_count": comment_count, "related_posts": related_posts, "comments": comments,  "categories": categories, "alt_categories": alt_categories, "tages": tages, "blog_tages": blog_tages, "recent_posts" :recent_posts, "banner": banner})



class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer