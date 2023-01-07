from django.shortcuts import render
from property.models import PropertyImage
from .models import GalleryView

def gallery(request):
    images = PropertyImage.objects.all()
    gallery_view = GalleryView.objects.first()
    return render(request, 'gallery.html', {"images": images, "gallery_view": gallery_view})