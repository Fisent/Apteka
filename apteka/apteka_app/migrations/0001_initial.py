# Generated by Django 2.0.1 on 2018-01-06 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pensja', models.IntegerField()),
                ('dataZatrudnienia', models.DateField()),
                ('pesel', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RolaPracownika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwaRoli', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataZamowienia', models.DateField()),
                ('oplacone', models.BooleanField()),
                ('sposobZaplaty', models.CharField(max_length=100)),
                ('sposobWysylki', models.CharField(max_length=100)),
                ('adresWysylki', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pracownik',
            name='idRolaPracownika',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.RolaPracownika'),
        ),
    ]
