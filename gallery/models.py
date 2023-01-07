from django.db import models

class GalleryView(models.Model):
    content = models.TextField()
    
    def __str__(self) -> str:
        return "Gallery View"