# Generated by Django 4.2.5 on 2023-09-26 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='principle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]
