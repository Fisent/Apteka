from django.db import models

# Create your models here.

class Klient(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=50)


class Zamowienie(models.Model):
    dataZamowienia = models.DateField()
    oplacone = models.BooleanField()
    sposobZaplaty = models.CharField(max_length=100)
    sposobWysylki = models.CharField(max_length=100)
    adresWysylki = models.CharField(max_length=100)

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=1000)

class RolaPracownika(models.Model):
    nazwaRoli = models.CharField(max_length=20)

class Pracownik(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=50)
    pensja = models.IntegerField()
    dataZatrudnienia = models.DateField()
    pesel = models.CharField(max_length=11)
    idRolaPracownika = models.ForeignKey(RolaPracownika, on_delete=models.CASCADE)
