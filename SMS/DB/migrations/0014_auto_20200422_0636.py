# Generated by Django 2.2.5 on 2020-04-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0013_auto_20200422_0631'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='departmentgraduationcredits',
            unique_together=set(),
        ),
    ]