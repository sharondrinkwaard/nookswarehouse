# Generated by Django 3.2.16 on 2023-03-06 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', models.CharField(blank=True, choices=[('Netherlands', 'Netherlands'), ('Belgium', 'Belgium')], max_length=40, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_street_address', models.CharField(blank=True, max_length=80, null=True)),
                ('default_house_number', models.CharField(blank=True, max_length=10, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]