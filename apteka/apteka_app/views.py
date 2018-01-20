from django.shortcuts import render
from apteka_app.models import Produkt

# Create your views here.

def index(request):
    return render(request, 'apteka_app/index.html', {'produkty':Produkt.objects.all()})
