# Generated by Django 4.2.2 on 2023-10-17 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vinilo',
            fields=[
                ('idVinilo', models.IntegerField(db_column='idVinilo', primary_key=True, serialize=False, verbose_name='Id_Vinilo')),
                ('nombreArt', models.CharField(max_length=50)),
                ('nombreDisco', models.CharField(max_length=80)),
                ('valorDisco', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
