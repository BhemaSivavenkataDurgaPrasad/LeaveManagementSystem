# Generated by Django 4.2.5 on 2023-09-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0006_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='Fdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='Tdata',
            field=models.CharField(max_length=10),
        ),
    ]
