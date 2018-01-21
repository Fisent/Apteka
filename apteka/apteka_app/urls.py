from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path(r'zamowienie/<int:id>', views.zamowienie),
    path(r'zamow/<int:id>/<int:ilosc_arg>', views.zamow_produkt),
    path(r'produkt/<int:id>', views.produkt),
    path(r'zloz_zamowienie/<int:zamowienie_id>', views.zloz_zamowienie),
    path(r'historia_zamowien/<int:zamowienie_id>', views.historia_zamowien)
]
