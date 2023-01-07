from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name = "properties"),
    path('<int:id>/', views.property_detail, name = "property_detail")
]
