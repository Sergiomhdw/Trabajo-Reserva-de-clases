# Generated by Django 3.2.3 on 2021-05-25 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('image', models.ImageField(upload_to='clases')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='profesores')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservationday', models.DateField()),
                ('horainicio', models.CharField(max_length=2)),
                ('horafinal', models.CharField(max_length=2)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clase')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profesor')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='reservas',
            field=models.ManyToManyField(through='app.Reserv', to='app.Profesor'),
        ),
    ]
