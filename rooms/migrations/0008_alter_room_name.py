# Generated by Django 4.1.5 on 2023-02-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_reservation_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]