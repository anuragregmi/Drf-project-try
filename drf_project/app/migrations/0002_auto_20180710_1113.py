# Generated by Django 2.0.6 on 2018-07-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Address'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
    ]