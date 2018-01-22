from django import forms


class ZamowienieForm(forms.Form):
    sposob_zaplaty = forms.CharField(label='Sposób zapłaty', max_length=500)
    sposob_wysylki = forms.CharField(label='Sposób wysyłki', max_length=500)
    adres_wysylki = forms.CharField(label='Adres wysyłki', max_length=500)