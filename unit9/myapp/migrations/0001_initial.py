# Generated by Django 3.2.4 on 2021-06-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('timestamp', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('timestamp', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=5)),
            ],
        ),
    ]
