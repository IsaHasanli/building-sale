from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length = 100)
    email = models.EmailField()
    location_name = models.CharField(max_length = 100)
    def __str__(self) -> str:
        return self.location_name

class Message(models.Model):
    name = models.CharField(max_length = 100, null = True, blank = True)
    email = models.EmailField(blank = True, null = True)
    subject = models.CharField(max_length = 200, blank = True, null = True)
    message = models.TextField(blank = True, null = True)
    is_visible = models.BooleanField(default = False)
    def __str__(self) -> str:
        return self.name