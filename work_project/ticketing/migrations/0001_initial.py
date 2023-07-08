# Generated by Django 3.2.19 on 2023-07-08 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(choices=[('peluza_nord', 'Peluză Nord'), ('peluza_sud', 'Peluză Sud'), ('tribuna_1', 'Tribuna 1'), ('tribuna_2', 'Tribuna 2')], max_length=20)),
                ('seat_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('status', models.CharField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'In Review'), (4, 'Done')], max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tribuna', models.CharField(choices=[('peluza_nord', 'Peluză Nord'), ('peluza_sud', 'Peluză Sud'), ('tribuna_1', 'Tribuna 1'), ('tribuna_2', 'Tribuna 2')], default=0, max_length=20)),
                ('numar_locuri', models.IntegerField(default=0)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.eveniment')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('tickets', models.ManyToManyField(to='ticketing.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
