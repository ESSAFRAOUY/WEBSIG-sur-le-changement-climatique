from django.contrib.gis import admin
from .models import  region,Temperature,Precipitation,Document,Action,Investisseur,Entreprise,Organisation,RegionAction,EntrepriseAction,InvestisseurAction,OrganisationAction,Indicateur,Station
# Register your models here.
admin.site.register(region,admin.GeoModelAdmin)
admin.site.register(Temperature,admin.GeoModelAdmin)
admin.site.register(Precipitation,admin.GeoModelAdmin)
admin.site.register(Document,admin.GeoModelAdmin)
admin.site.register(Action,admin.GeoModelAdmin)
admin.site.register(Entreprise,admin.GeoModelAdmin)
admin.site.register(Investisseur,admin.GeoModelAdmin)
admin.site.register(Organisation,admin.GeoModelAdmin)
admin.site.register(RegionAction,admin.GeoModelAdmin)
admin.site.register(EntrepriseAction,admin.GeoModelAdmin)
admin.site.register(InvestisseurAction,admin.GeoModelAdmin)
admin.site.register(OrganisationAction,admin.GeoModelAdmin)
admin.site.register(Indicateur,admin.GeoModelAdmin)
admin.site.register(Station,admin.GeoModelAdmin)


