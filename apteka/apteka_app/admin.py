from django.contrib import admin
from apteka_app.models import Klient, Zamowienie, Produkt, RolaPracownika, Pracownik, PracownikZamowienie, ZamowienieKlient, ZamowienieProdukt

# Register your models here.

admin.site.register(Klient)
admin.site.register(Zamowienie)
admin.site.register(Produkt)
admin.site.register(RolaPracownika)
admin.site.register(Pracownik)
admin.site.register(PracownikZamowienie)
admin.site.register(ZamowienieKlient)
admin.site.register(ZamowienieProdukt)
