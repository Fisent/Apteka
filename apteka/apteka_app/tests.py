from django.test import TestCase
from apteka_app.models import Zamowienie, Klient, ZamowienieProdukt, Produkt
from datetime import datetime

# Create your tests here.
class ZamowienieProduktTestCase(TestCase):
    def setUp(self):
        a = Zamowienie.objects.create(dataZamowienia=datetime.today(), oplacone=False, sposobZaplaty="Przelew", sposobWysylki="Poczta Polska", adresWysylki="Wrocław, ul. Drewniana 1")
        b = Produkt.objects.create(nazwa='witamina a', opis='suplement diety zawierający witaminę a', cena=10)
        ZamowienieProdukt.objects.create(idZamowienie=a, idProdukt=b, ilosc=3)
        ZamowienieProdukt.objects.create(idZamowienie=a, idProdukt=b, ilosc=0)
    
    def test_1(self):
        Zamowienie.objects.get(id=1)
        self.assertEqual(1,1)

    def test_cena_zamowienie_produkt(self):
        self.assertEqual(ZamowienieProdukt.objects.get(pk=1).cena(), 30)
    
    def test_cena_brzegowe(self):
        self.assertEqual(ZamowienieProdukt.objects.get(pk=2).cena(), 0)

class ZamowienieTestCase(TestCase):
    def setUp(self):
        a = Zamowienie.objects.create(dataZamowienia=datetime.today(), oplacone=False, sposobZaplaty="Przelew", sposobWysylki="Poczta Polska", adresWysylki="Wrocław, ul. Drewniana 1")
        b = Produkt.objects.create(nazwa='witamina a', opis='suplement diety zawierający witaminę a', cena=10)
        c = Produkt.objects.create(nazwa='witamina c', opis='suplement diety zawierający witaminę c', cena=50)
        ZamowienieProdukt.objects.create(idZamowienie=a, idProdukt=b, ilosc=3)
        ZamowienieProdukt.objects.create(idZamowienie=a, idProdukt=c, ilosc=4)

    def test_cena_zamowienia(self):
        self.assertEqual(Zamowienie.objects.get(pk=1).cena(), 230)
