from django.shortcuts import render
from .models import Property
from django.core.paginator import Paginator
from .filters import PropertyFilter

def properties(request):
    sort = request.GET.get("sort")
    item_count = request.GET.get("item_count")
    properties = PropertyFilter(request.GET, queryset=Property.objects.all())
    if sort:
        paginator = Paginator(properties.qs.order_by(sort), 6)
    else:
        sort = "-date"
    if item_count:
        paginator = Paginator(properties.qs, item_count)
    else:
        item_count = 6
        paginator = Paginator(properties.qs, item_count)
    if sort.startswith("-"):
        sort = sort[1:].capitalize
    page_number = request.GET.get("page")
    properties = paginator.get_page(page_number)
    popular_properties = Property.objects.all().order_by("-view_count")[0:3]
    property_filter = PropertyFilter()
    return render(request, 'properties.html', {"properties": properties, "popular_properties": popular_properties, "property_filter": property_filter, "item_count": item_count, "sort": sort})

def property_detail(request, id):
    property = Property.objects.get(id = id)
    nearby_properties = Property.objects.filter(category = property.category, property_type = property.property_type, building_type = property.building_type ).exclude(id=id)
    property.view_count += 1
    property.save()
    popular_properties = Property.objects.exclude(id=id).order_by("-view_count")[0:3]
    return render(request, 'property_detail.html', {"property": property, "nearby_properties": nearby_properties,"popular_properties": popular_properties})