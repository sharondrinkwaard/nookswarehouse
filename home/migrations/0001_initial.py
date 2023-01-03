# Generated by Django 3.2.16 on 2023-01-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
