# Generated by Django 3.1.2 on 2022-01-04 01:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220102_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('region', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('siteAddress', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('servInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.asset')),
            ],
        ),
    ]
