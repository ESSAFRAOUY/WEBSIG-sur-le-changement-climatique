# Generated by Django 3.2.5 on 2021-09-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatechange', '0019_alter_action_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='Location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
