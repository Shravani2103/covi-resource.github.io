# Generated by Django 3.2.3 on 2021-05-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_your_resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='Availability',
            new_name='Beds_avail',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Res_quantity',
        ),
    ]