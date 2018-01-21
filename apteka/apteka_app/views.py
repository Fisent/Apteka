from django.shortcuts import render
from apteka_app.models import Produkt, Zamowienie, ZamowienieProdukt
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'apteka_app/index.html', {'produkty':Produkt.objects.all(), 'zamowienie':Zamowienie.objects.get(pk=1)})

def zamowienie(request, id):
    produkty = []
    licznosci = []
    zam_prod = ZamowienieProdukt.objects.filter(idZamowienie=id)
    return render(request, 'apteka_app/zamowienie.html', {'zamowienie':Zamowienie.objects.get(pk=id), 'zam_prod':zam_prod})

def produkt(request, id):
    return HttpResponse('produkt: ' + (Produkt.objects.get(pk=id)).nazwa)

def zamow_produkt(request, id, ilosc_arg):
    zam_prod = ZamowienieProdukt(idZamowienie=Zamowienie.objects.get(pk=1), idProdukt=Produkt.objects.get(pk=id), ilosc=ilosc_arg)
    zam_prod.save()
    return HttpResponse('Produkt ' + str(Produkt.objects.get(pk=id).nazwa) + ' dodany do koszyka<br> ZamowienieProdukt: ' + str(ZamowienieProdukt.objects.get(pk=zam_prod.id)))

def zloz_zamowienie(request, zamowienie_id):
    return HttpResponse('zlozone')