# Generated by Django 4.0.8 on 2022-11-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
    ]
