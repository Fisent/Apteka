# Generated by Django 2.0.1 on 2018-01-06 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apteka_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracownikZamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.Pracownik')),
                ('idZamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka_app.Zamowienie')),
            ],
        ),
    ]
