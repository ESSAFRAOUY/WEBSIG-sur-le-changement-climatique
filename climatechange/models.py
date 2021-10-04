from django.db import models
from django.db.models.base import Model
from django.contrib.gis.db import models as gismodels
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import DateField, IntegerField

# Create your models here.

class admin(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)


class region(models.Model):
    region_name = models.CharField(max_length=100)
    surface = models.FloatField()
    polygon = gismodels.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.region_name



#class Regions(models.Model):
    #region_name = models.CharField(max_length=100)
    #surface = models.FloatField()
    #geometrie = gismodels.MultiPolygonField(srid=4326)



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


MONTHS_CHOICES = ((1, "Janvier"), (2, "Février"), (3, "Mars"), (4, "Avril"),(5, "Mai"),(6, "Juin"),
(7, "Juillet"),(8, "Aout"),(9, "Septembre"),(10, "Octobre"),(11, "Novembre"),(12, "Décembre"),)

FORMAT_CHOICES = ((1, "PDF"), (2, "WORD"), (3, "CSV"),)

THEME_CHOICES = ((1, "Occupation du sol"), (2, "Eau"), (3, "Energie"),(4, "Industrie"),(5, "Transport"),(6, "Océan et zones cotières"),)

TYPE_CHOICES = ((1, "Réduction des émissions"), (2, "Établissement du prix du carbone"), (3, "Efficacité énergétique"),(4, "Investissement"),(5, "Énergie renouvelable"),(6, "La consommation de ressources"),(7, "Assurance des obligations"),)

SDGS_CHOICES = ((1, "Énergie abordable et propre"), (2, "Innovation et infrastructure de l'industrie"), (3, "Pas de pauvreté"),(4, "Éducation de qualité"),(5, "Villes et communautés durables"),(6, "Consommation et production responsables"),)

TYPE_ACTION_CHOICES = ((1, "Individuelle"), (2, "Cooperative"),)

LOCATION_CHOICES = ((1,"Maroc"), (2, "Tunisie"),(3, "Algérie"),(4, "Egypte"),(5, "Espagne"))

class Station(models.Model):
    region = models.ForeignKey(region, on_delete=models.CASCADE,null=True, blank=True)
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    Ville = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    def __str__(self):
        return self.nom

class Precipitation(models.Model):
    region = models.ForeignKey(region, on_delete=models.CASCADE,default="")
    station = models.ForeignKey(Station, on_delete=models.CASCADE,null=True, blank=True)
    valeur_max = models.FloatField()
    valeur_min = models.FloatField()
    valeur_moyenne = models.FloatField()
    month = models.IntegerField(choices=MONTHS_CHOICES, default=1)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    



class Temperature(models.Model):
    region = models.ForeignKey(region, on_delete=models.CASCADE,default="")
    station = models.ForeignKey(Station, on_delete=models.CASCADE,null=True, blank=True)
    valeur_max = models.SmallIntegerField()
    valeur_min = models.SmallIntegerField()
    valeur_moyenne = models.FloatField()
    month = models.IntegerField(choices=MONTHS_CHOICES, default=1)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    

class Document(models.Model):
    region = models.ForeignKey(region, on_delete=models.CASCADE,null=True, blank=True)
    titre = models.CharField(max_length=150)
    auteur = models.CharField(max_length=100)
    nombre_de_pages = models.IntegerField()
    date_insertion = models.DateTimeField( auto_now_add=True)
    description = models.TextField()
    Format = models.IntegerField(choices=FORMAT_CHOICES, default=1)
    photo = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None)
    fichier = models.FileField(upload_to='media')
    def __str__(self):
        return self.titre


class Action(models.Model):
    nom_action = models.CharField(max_length=150)
    type_action = models.IntegerField(choices=TYPE_ACTION_CHOICES, default=1)
    theme = models.IntegerField(choices=THEME_CHOICES, default=1)
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    Objectifs_de_développement_durable  = models.IntegerField(choices=SDGS_CHOICES, default=1)
    date_action = models.DateField()
    description = models.TextField()
    Location = models.IntegerField(choices=LOCATION_CHOICES, default=1)
    def __str__(self):
        return self.nom_action
   
class Entreprise(models.Model):
    nom = models.CharField(max_length=150)
    nombre_employes = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    secteur_activité = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
    
   
    
   
class Investisseur(models.Model):
    nom = models.CharField(max_length=150)
    nombre_employes = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    secteur_activité = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
   

class Organisation(models.Model):
    nom = models.CharField(max_length=150)
    nombre_employes = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    secteur_activité = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class RegionAction(models.Model):
    nom = models.ForeignKey(region, on_delete=models.CASCADE,default="")
    action = models.ForeignKey(Action, on_delete=models.CASCADE,default="")

class EntrepriseAction(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE,default="")
    action = models.ForeignKey(Action, on_delete=models.CASCADE,default="")

class InvestisseurAction(models.Model):
    investisseur = models.ForeignKey(Investisseur, on_delete=models.CASCADE,default="")
    action = models.ForeignKey(Action, on_delete=models.CASCADE,default="")

class OrganisationAction(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE,default="")
    action = models.ForeignKey(Action, on_delete=models.CASCADE,default="")


class Indicateur(models.Model):
    region = models.ForeignKey(region, on_delete=models.CASCADE,default="")
    nom = models.CharField(max_length=150)
    secteur = models.CharField(max_length=100)
    horizon = models.CharField(max_length=100)
    valeur = models.FloatField()
    nombre_actions_conditionnelles= IntegerField()
    nombre_actions_inconditionnelles= IntegerField()
    cout = models.FloatField()
    def __str__(self):
        return self.nom
    


