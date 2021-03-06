# Generated by Django 3.1.2 on 2022-01-02 02:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('serverName', models.CharField(max_length=200)),
                ('serverIp', models.CharField(max_length=50)),
                ('serverType', models.CharField(max_length=50)),
                ('serverRole', models.CharField(max_length=50)),
                ('serverNote', models.TextField(blank=True, null=True)),
                ('idrac_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('idrac_User', models.CharField(blank=True, max_length=5, null=True)),
                ('idrac_Passwd', models.CharField(blank=True, max_length=50, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
