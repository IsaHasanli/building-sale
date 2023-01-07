from django.shortcuts import render, redirect
from .models import Contact
from .forms import MessageForm
import folium
import geocoder
def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        print(form.data)
        if form.is_valid():
            message = form.save(commit = False) 
            if request.user.is_authenticated:
                message.name = request.user.username
                message.email = request.user.email
            message.save()
        return redirect("contact")
    contact =Contact.objects.first()
    location = geocoder.osm(contact.location_name)
    country = location.country
    lat = location.lat
    lng = location.lng
    m = folium.Map(location=[lat, lng], zoom_start=12)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,
        'contact': contact
    }
    return render(request, 'contact.html', context)