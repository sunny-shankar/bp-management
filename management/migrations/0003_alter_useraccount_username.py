# Generated by Django 3.2.9 on 2021-11-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_bloodpressure_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
