# Generated by Django 3.1.2 on 2022-01-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_delete_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('siteAddress', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='locationsInfo',
            field=models.ManyToManyField(to='inventory.Locations'),
        ),
    ]