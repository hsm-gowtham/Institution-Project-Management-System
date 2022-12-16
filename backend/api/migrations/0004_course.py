# Generated by Django 4.0.8 on 2022-11-27 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_student_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('instituition_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.instituition')),
            ],
        ),
    ]