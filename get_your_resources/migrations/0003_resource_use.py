# Generated by Django 3.2.3 on 2021-05-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_your_resources', '0002_auto_20210529_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='use',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
