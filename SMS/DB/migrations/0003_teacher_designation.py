# Generated by Django 2.2.5 on 2020-01-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]