from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
class Category(models.Model):
    title = models.CharField(max_length=200)

    def _str_(self) -> str:
        return self.title

class Property(models.Model):
    CATEGORIES = (
        ("flat", "Flat"),
        ("land", "Land"),
        ("plot", "Plot"),
        ("commercial", "Commercial")
    )
    PROPERTY_TYPES = (
        ("for-sale", "For Sale"),
        ("for-rent", "For Rent"),
        ("sold-out", "Sold Out"),
    )
    BUILDING_TYPES = (
        ("old-building", "Old Building"),
        ("new-building", "New Building"),
    )

    title = models.CharField(max_length=200)
    price = models.BigIntegerField(default = 0, validators=[
            MaxValueValidator(1500000),
            MinValueValidator(0)
        ])
    view_count = models.IntegerField(default=0)
    description = models.TextField()
    video = models.FileField(upload_to="property/video", null = True, blank = True)
    # map = models.ForeignKey(Map, on_delete=models.SET_NULL, null=True)
    location = models.TextField()
    category = models.CharField(max_length=20, choices = CATEGORIES)
    building_type = models.CharField(max_length=20, choices = BUILDING_TYPES, default='new-building')
    property_type = models.CharField(max_length=20, choices = PROPERTY_TYPES, default='for-sale')
    area = models.IntegerField(default = 1, validators=[
            MaxValueValidator(500),
            MinValueValidator(0)
        ])
    rooms = models.IntegerField(default = 1, validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    ground = models.IntegerField(default=1, validators=[
            MaxValueValidator(30),
            MinValueValidator(0)
        ])
    building_ground = models.IntegerField(default=1, validators=[
            MaxValueValidator(30),
            MinValueValidator(0)
        ])
    date = models.DateTimeField(auto_now_add=True, blank = True)
    bedroom_count = models.IntegerField(default = 1, validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    bath_count = models.IntegerField(default = 1, validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    have_kitchen = models.BooleanField(default=True)
    have_air_condition = models.BooleanField(default=True)
    have_belcony = models.BooleanField(default=True)
    have_gym = models.BooleanField(default=True)
    have_garden = models.BooleanField(default=True)
    have_cctv = models.BooleanField(default=True)
    have_children_playground = models.BooleanField(default=True)
    have_community_center = models.BooleanField(default=True)
    have_security = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"id": self.pk})
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('title',)

class PropertyImage(models.Model):
    CATEGORIES = (
        ("apartment", "APARTMENT"),
        ("livingroom", "LIVING ROOM"),
        ("bedroom", "BEDROOM"),
        ("kitchen", "KITCHEN"),
        ("garage", "GARAGE")
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_images')
    image = models.ImageField(upload_to="property/images/")
    category = models.CharField(max_length=100, choices = CATEGORIES)

    def _str_(self) -> str:
        return f'{self.category} / {self.property.title}'
