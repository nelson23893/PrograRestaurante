# Generated by Django 2.1.3 on 2018-11-07 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Jugador')),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='mains',
            name='personaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Personaje'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='personajes',
            field=models.ManyToManyField(through='torneo.Mains', to='torneo.Personaje'),
        ),
    ]