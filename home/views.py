from django.shortcuts import render
from property.models import Property
from .models import About, Agent, Brand
from contact.models import Message
from blog.models import Blog
from django.db.models import Count
def home(request):
    properties = Property.objects.all()
    about = About.objects.first()
    last_properties = Property.objects.all().order_by("-id")[0:6]
    agents = Agent.objects.all()
    messages = Message.objects.filter(is_visible = True)
    brands = Brand.objects.all()
    latest_news = Blog.objects.all().annotate(total_comments = Count('comments')).order_by("-id")[0:3]
    return render(request, 'home.html', {"properties": properties, "about": about, "last_properties": last_properties, "agents": agents, "messages": messages, "brands": brands, "latest_news": latest_news})