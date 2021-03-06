# Generated by Django 3.2.5 on 2021-08-25 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climatechange', '0014_remove_action_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='region',
        ),
        migrations.RemoveField(
            model_name='investisseur',
            name='region',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='region',
        ),
        migrations.CreateModel(
            name='RegionAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.action')),
                ('nom', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
    ]
