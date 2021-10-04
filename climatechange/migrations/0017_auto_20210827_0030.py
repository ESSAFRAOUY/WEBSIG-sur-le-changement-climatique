# Generated by Django 3.2.5 on 2021-08-26 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climatechange', '0016_auto_20210825_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='action',
        ),
        migrations.CreateModel(
            name='EntrepriseAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.action')),
                ('entreprise', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.entreprise')),
            ],
        ),
    ]
