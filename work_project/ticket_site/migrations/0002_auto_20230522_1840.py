# Generated by Django 3.2.19 on 2023-05-22 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='event',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
