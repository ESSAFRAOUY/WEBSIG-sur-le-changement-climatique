# Generated by Django 3.2.5 on 2021-08-25 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climatechange', '0011_alter_document_titre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_action', models.CharField(max_length=150)),
                ('type_action', models.IntegerField(choices=[(1, 'Individuelle'), (2, 'Cooperative')], default=1)),
                ('theme', models.IntegerField(choices=[(1, 'Occupation du sol'), (2, 'Eau'), (3, 'Energie'), (4, 'Industrie'), (5, 'Transport'), (6, 'Océan et zones cotières')], default=1)),
                ('type', models.IntegerField(choices=[(1, 'Réduction des émissions'), (2, 'Établissement du prix du carbone'), (3, 'Efficacité énergétique'), (4, 'Investissement'), (5, 'Énergie renouvelable'), (6, 'La consommation de ressources'), (7, "Émission d'obligations")], default=1)),
                ('Objectifs_de_développement_durable', models.IntegerField(choices=[(1, 'Énergie abordable et propre'), (2, "Innovation et infrastructure de l'industrie"), (3, 'Pas de pauvreté'), (4, 'Éducation de qualité'), (5, 'Villes et communautés durables'), (6, 'Consommation et production responsables')], default=1)),
                ('date_action', models.DateField()),
                ('description', models.TextField()),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('nombre_employes', models.IntegerField()),
                ('revenue', models.CharField(max_length=100)),
                ('secteur_activité', models.CharField(max_length=100)),
                ('action', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.action')),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('nombre_employes', models.IntegerField()),
                ('revenue', models.CharField(max_length=100)),
                ('secteur_activité', models.CharField(max_length=100)),
                ('action', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.action')),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('nombre_employes', models.IntegerField()),
                ('revenue', models.CharField(max_length=100)),
                ('secteur_activité', models.CharField(max_length=100)),
                ('action', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.action')),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='climatechange.region')),
            ],
        ),
    ]
