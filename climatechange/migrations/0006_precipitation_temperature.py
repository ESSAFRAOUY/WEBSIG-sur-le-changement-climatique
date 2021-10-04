# Generated by Django 3.2.5 on 2021-08-16 10:26

import climatechange.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climatechange', '0005_rename_mpoly_region_polygon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur_max', models.SmallIntegerField()),
                ('valeur_min', models.SmallIntegerField()),
                ('valeur_moyenne', models.FloatField()),
                ('month', models.IntegerField(choices=[(1, 'Janvier'), (2, 'Février'), (3, 'Mars'), (4, 'Avril'), (5, 'Mai'), (6, 'Juin'), (7, 'Juillet'), (8, 'Aout'), (9, 'Septembre'), (10, 'Octobre'), (11, 'Novembre'), (12, 'Décembre')], default=1)),
                ('year', models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1984), climatechange.models.max_value_current_year])),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
        
    ]