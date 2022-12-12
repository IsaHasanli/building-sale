from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

class Tag(models.Model):
    title = models.CharField(max_length = 50)
    
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(max_length = 100)
    parent = models.ForeignKey('self',blank = True, null = True, on_delete = models.CASCADE, related_name = 'categories')
    def __str__(self) -> str:
        return f'{self.title} / {self.parent}'

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'blogs/', default = '../static/img/blog-img-1.jpg')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'blogs')
    description = models.TextField()
    description2 = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blogs')
    tages = models.ManyToManyField(Tag,related_name = 'blogs', blank = True)
    created_time = models.DateField(auto_now_add = True)
    updated_time = models.DateField(auto_now = True)

    def __str__(self) -> str:
        return f'{self.title} / {self.category}'

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"id": self.pk})
    
    def next_url(self):
        for i in range(len(Blog.objects.all())):
            if Blog.objects.all()[i].pk == self.pk and Blog.objects.last().pk != self.pk:
                page=Blog.objects.all()[i+1].pk
                return reverse("blog_detail", kwargs={"id": page})

    def prev_url(self):
        for i in range(len(Blog.objects.all())):
            if Blog.objects.all()[i].pk == self.pk and Blog.objects.first().pk != self.pk:
                page=Blog.objects.all()[i-1].pk
                return reverse("blog_detail", kwargs={"id": page})

    def has_next(self):
        if Blog.objects.last().pk == self.pk:
            return False
        return True

    def has_prev(self):
        if Blog.objects.first().pk == self.pk:
            return False
        return True

class Comment(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    website = models.CharField(max_length = 200)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = "comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null = True,  blank = True,  related_name = 'comments' )
    created_time = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.blog} / {self.name} / {self.content}'

class Banner(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()
    image = models.ImageField('banner/')

    def __str__(self) -> str:
        return self.title
    