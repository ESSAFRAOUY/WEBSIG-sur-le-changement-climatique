# Generated by Django 3.2.5 on 2021-09-07 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climatechange', '0023_document_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('secteur', models.CharField(max_length=100)),
                ('horizon', models.CharField(max_length=100)),
                ('valeur', models.FloatField()),
                ('nombre_actions_conditionnelles', models.IntegerField()),
                ('nombre_actions_inconditionnelles', models.IntegerField()),
                ('cout', models.FloatField()),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
    ]
