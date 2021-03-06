# Generated by Django 2.0.1 on 2018-01-06 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apteka_app', '0002_pracownikzamowienie'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZamowienieKlient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idKlient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.Klient')),
                ('idZamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.Zamowienie')),
            ],
        ),
        migrations.CreateModel(
            name='ZamowienieProdukt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.IntegerField()),
                ('idProdukt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.Produkt')),
                ('idZamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.Zamowienie')),
            ],
        ),
    ]
