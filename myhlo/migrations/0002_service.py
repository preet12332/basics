# Generated by Django 3.2.19 on 2023-11-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhlo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=200)),
                ('service_title', models.CharField(max_length=200)),
                ('service_desc', models.TextField()),
            ],
        ),
    ]