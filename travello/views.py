from django.shortcuts import render
from .models import Destination


# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.name = "Hyderabad"
    dest1.desc = "The Biryani City"
    dest1.img = "destination_1.jpg"
    dest1.price ="600"


    dest2 = Destination()
    dest2.name = "Mumbai"
    dest2.desc = "The City Never Sleeps"
    dest2.img = "destination_2.jpg"
    dest2.price = "650"

    dest3 = Destination()
    dest3.name = "bangalore"
    dest3.desc = "The Greenary City"
    dest3.img = "destination_6.jpg"
    dest3.price = "700"

    dests = [dest1,dest2,dest3]

    return render(request, 'index.html', {'dests': dests})
