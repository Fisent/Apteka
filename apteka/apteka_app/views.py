from django.shortcuts import render, redirect
from apteka_app.models import Produkt, Zamowienie, ZamowienieProdukt, ZamowienieKlient
from django.http import HttpResponse
from apteka_app.forms import ZamowienieForm


# Create your views here.

def index(request):
    return render(request, 'apteka_app/index.html', {'produkty':Produkt.objects.all(), 'zamowienie':Zamowienie.objects.get(pk=1)})

def zamowienie(request, id):
    if request.method == 'POST':
        form = ZamowienieForm(request.POST)
        form.is_valid()
        zam = Zamowienie.objects.get(pk=id)
        zam.sposobZaplaty = form.cleaned_data['sposob_zaplaty']
        zam.sposobWysylki = form.cleaned_data['sposob_wysylki']
        zam.adresWysylki = form.cleaned_data['adres_wysylki']
        zam.save()
        return redirect('/apteka')
    else:
        zam_prod = ZamowienieProdukt.objects.filter(idZamowienie=id)
        form = ZamowienieForm()
        return render(request, 'apteka_app/zamowienie.html', {'zamowienie':Zamowienie.objects.get(pk=id), 'zam_prod':zam_prod, 'form':form, 'id':id})

def produkt(request, id):
    return render(request, 'apteka_app/produkt.html', {'produkt':Produkt.objects.get(pk=id)})

def zamow_produkt(request, id, ilosc_arg):
    zam_prod = ZamowienieProdukt(idZamowienie=Zamowienie.objects.get(pk=1), idProdukt=Produkt.objects.get(pk=id), ilosc=ilosc_arg)
    zam_prod.save()
    return HttpResponse('Produkt ' + str(Produkt.objects.get(pk=id).nazwa) + ' dodany do koszyka<br> ZamowienieProdukt: ' + str(ZamowienieProdukt.objects.get(pk=zam_prod.id)))

def zloz_zamowienie(request, zamowienie_id):
    return HttpResponse('zlozone')

def historia_zamowien(request, id_uzytkownik):
    zam_prod = ZamowienieKlient.objects.filter(idKlient=id_uzytkownik)
    zamowienia = []
    for zp in zam_prod:
        zamowienia.append(zp.idZamowienie)
    return render(request, 'apteka_app/historia_zamowien.html', {'zamowienia':zamowienia})