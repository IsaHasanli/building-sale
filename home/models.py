from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to = "about/")
    description = models.TextField()

    def __str__(self) -> str:
        return "About"

class AboutRequirement(models.Model):
    content = models.TextField()
    about = models.ForeignKey(About, on_delete = models.CASCADE, related_name = "about_requirements")

class AgentPosition(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Agent(models.Model):
    full_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "agents/")
    position = models.ForeignKey(AgentPosition, on_delete = models.SET_NULL, null = True, related_name = "agents")
    facebook = models.TextField(null = True, blank = True)
    twitter = models.TextField(null = True, blank = True)
    linkedin = models.TextField(null = True, blank = True)
    google = models.TextField(null = True, blank = True)
    
    def __str__(self) -> str:
        return self.full_name

class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'brands/')

    def __str__(self) -> str:
        return self.title