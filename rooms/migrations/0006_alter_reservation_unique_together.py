# Generated by Django 4.1.5 on 2023-02-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_reservation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('room', 'date')},
        ),
    ]
