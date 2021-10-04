from json.decoder import JSONDecodeError, JSONDecoder
from typing import ContextManager
from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import render
from django.http.response import Http404, HttpResponse
import json
from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.fields import GeometryField
from .models import Action, Document, Entreprise, EntrepriseAction, Investisseur, InvestisseurAction, Organisation, OrganisationAction, RegionAction, Station, admin,region,Temperature,Precipitation,Indicateur
import requests
from django import template
from django.views.generic import TemplateView
import os
from django.conf import settings
from .filters import FilterDocument,FilterAction




# Create your views here.
def index(request):

    region4 = list(region.objects.values())
    indicateurs = Indicateur.objects.all()
    #select st_asgeojson(polygon)from climatechange_region where id = 5  limit 1

    regions=[]
    reg= []
    for r in region.objects.raw('''select id, 
    region_name,
    surface,
    st_asgeojson(polygon) as geometrie
    from climatechange_region '''):

        #print(r.surface)
        i=0
        regions.append(r)
        i=i+1
        #reg=[regions[0].id,regions[0].region_name,regions[0].surface,regions[0].geometrie]
       
    #for i in range (len(region4)):
      #  regions[i-1]=region4[i].polygon
        #print(reg.polygon)
    #print(regions[0].geometrie)
   
    
    reg1=[regions[0].geometrie]
    reg2=[regions[1].geometrie]
    reg3=[regions[2].geometrie]
    reg4=[regions[3].geometrie]
    reg5=[regions[4].geometrie]
    reg6=[regions[5].geometrie]
    reg7=[regions[6].geometrie]
    reg8=[regions[7].geometrie]
    reg9=[regions[8].geometrie]
    reg10=[regions[9].geometrie]
    reg11=[regions[10].geometrie]
    reg12=[regions[11].geometrie]
    for i in range(11):
        reg.append(regions[i].geometrie)


    
    #***********************add

    data1 =  json.dumps(
            [
                {
                    'id': obj.id,
                    'valeur_min': obj.valeur_min,
                    'valeur_max' : obj.valeur_max,
                    'valeur_moyenne' :obj.valeur_moyenne,
                    'month' : obj.month,
                    'year' : obj.year,
                    'id_region' : obj.region_id,
                    'id_station' : obj.station_id

                    
                }
                for obj in Temperature.objects.all()
            ]
        )
    data2 =  json.dumps(
            [
                {
                    'id': obj.id,
                    'valeur_min': obj.valeur_min,
                    'valeur_max' : obj.valeur_max,
                    'valeur_moyenne' :obj.valeur_moyenne,
                    'month' : obj.month,
                    'year' : obj.year,
                    'id_region' : obj.region_id,
                    'id_station':obj.station.id

                    
                }
                for obj in Precipitation.objects.all()
            ]
        )
    
    dataIndicateur1 =  json.dumps(
            [
                {
                    'id_region' : obj.region_id,
                    'nom': obj.nom,
                    'secteur': obj.secteur,
                    'horizon' : obj.horizon,
                    'AC' :obj.nombre_actions_conditionnelles,
                    'AIC' : obj.nombre_actions_inconditionnelles,
                    'cout' : obj.cout,
                    'valeur' : obj.valeur

                    
                }
                for obj in Indicateur.objects.all()
            ]
        )

    dataStations =  json.dumps(
            [
                {   'id':obj.id,
                    'id_region' : obj.region_id,
                    'nom': obj.nom,
                    'longitude' : obj.longitude,
                    'latitude' : obj.latitude

                    
                }
                for obj in Station.objects.all()
            ]
        )
    dataRegions =  json.dumps(
        [
            {   'id':obj.id,
                'region_name' : obj.region_name,
                'surface': obj.surface,

                
            }
            for obj in region.objects.all()
        ]
    )
    

    #***********************end
    valeurIndicateur=[]
    for i in indicateurs:
        valeurIndicateur.append(i.valeur)

    context={
        'dataRegions' :dataRegions,
        'stations':dataStations,
        'dataIndicateur1':dataIndicateur1,
        'indicateurs':indicateurs,
        'reg1':reg1,
        'reg2':reg2,
        'reg3':reg3,
        'reg4':reg4,
        'reg5':reg5,
        'reg6':reg6,
        'reg7':reg7,
        'reg8':reg8,
        'reg9':reg9,
        'reg10':reg10,
        'reg11':reg11,
        'reg12':reg12,
        'data1':data1,
        'data2':data2
      
     }
    
    #return  render(request,'index.html',{'regions':context})
    return  render(request,'index.html',{'regions':context})
   
def json1(request):
    regions=[]
    for r in region.objects.raw('''select id, 
    region_name,
    surface,
    st_asgeojson(polygon) as geometrie
    from climatechange_region '''):

        print(r.surface)
        i=0
        regions.append(r)
        i=i+1
        reg=[regions[0].id,regions[0].region_name,regions[0].surface,regions[0].geometrie]
       
    
    reg1=[regions[0].geometrie]
    reg2=[regions[1].geometrie]
    reg3=[regions[2].geometrie]
    reg4=[regions[3].geometrie]
    reg5=[regions[4].geometrie]
    reg6=[regions[5].geometrie]
    reg7=[regions[6].geometrie]
    reg8=[regions[7].geometrie]
    reg9=[regions[7].geometrie]
    reg10=[regions[7].geometrie]
    reg11=[regions[7].geometrie]
    reg12=[regions[7].geometrie]

    payload = reg1
    r=requests.post('https://reqres.in//api/users',json=payload)
    print(r.url)
    
    context={
        'reg1':reg1,
        'reg2':reg2,
        'reg3':reg3,
        'reg4':reg4,
        'reg5':reg5,
        'reg6':reg6,
        'reg7':reg7,
        'reg8':reg8,
        'reg9':reg9,
        'reg10':reg10,
        'reg11':reg11,
        'reg12':reg12
      
        }
    return JsonResponse(context,safe=False)




def charts(request):

    temperature_regions=[]
    for r in Temperature.objects.raw('''SELECT * FROM climatechange_Temperature
    WHERE region_id=12
     '''):

        i=0
        temperature_regions.append(r)
        i=i+1

    data1 =  json.dumps(
            [
                {
                    'id': obj.id,
                    'valeur_min': obj.valeur_min,
                    'valeur_max' : obj.valeur_max,
                    'valeur_moyenne' :obj.valeur_moyenne,
                    'month' : obj.month,
                    'year' : obj.year,
                    'id_region' : obj.region_id

                    
                }
                for obj in Temperature.objects.all()
            ]
        )
    
    context = {
        'data':temperature_regions,
        'data1':data1
    }
    #return render(request,'index.html',context)
    return render(request,'charts.html',context)



def documents(request):

    doc = Document.objects.all()
    filter1 = FilterDocument(request.GET,queryset=doc)
    doc = filter1.qs
    context={
        'filter':filter1,
        'documents':doc
    }

    return render(request,'document.html',context)



def download_documents(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type ='application/fichier')
            response['Content-Disposition'] = 'inline;filename='+ os.path.basename(file_path)
            return response
    
    return Http404


class ActorActions:
    def __init__(self,name,coop,indiv):
        self.nom = name
        self.cooperative = coop
        self.individuelle = indiv


def actors(request):
    organisationActions = OrganisationAction.objects.all()
    investisseurActions = InvestisseurAction.objects.all()
    entrepriseActions = EntrepriseAction.objects.all()
    regionsActions = RegionAction.objects.all()
    entreprises = Entreprise.objects.all()
    actions = Action.objects.all()
    investisseurs = Investisseur.objects.all()
    regions = region.objects.all()
    organisations = Organisation.objects.all()
    
    i=0
    j=0
    listEntreprises =[]
    obj1 = ActorActions('',0,0)
    for z in entreprises:
        for y in actions:
            for x in entrepriseActions:
                if x.action_id==y.id and x.entreprise_id==z.id:
                    if y.type_action==2:
                        i=i+1
                    else:
                        j=j+1
                    if obj1.nom == z.nom :
                        obj1.nom = z.nom
                        obj1.cooperative=obj1.cooperative + i
                        obj1.individuelle=obj1.individuelle + j
                        
                    else:
                        obj1=ActorActions(z.nom,i,j)
                        listEntreprises.append(obj1)
                    i=0
                    j=0
                    
        
    i1=0
    j1 = 0
    obj = ActorActions('',0,0)
    listeInvestisseurs=[]
    for z in investisseurs :
        for y in actions :
            for x in investisseurActions:
                if x.action_id==y.id and x.investisseur_id==z.id:
                    if y.type_action==2:
                        i1=i1+1
                    else:
                        j1=j1+1
                    if obj.nom == z.nom :
                        obj.nom = z.nom
                        obj.cooperative=obj.cooperative + i1
                        obj.individuelle=obj.individuelle + j1
                        
                    else:
                        obj=ActorActions(z.nom,i1,j1)
                        listeInvestisseurs.append(obj)
                
                    i1=0
                    j1=0


    i2=0
    j2 = 0
    obj2 = ActorActions('',0,0)
    listeOrganisations=[]
    for z in organisations:
        for y in actions :
            for x in organisationActions :
                if x.action_id==y.id and x.organisation_id==z.id:
                    if y.type_action==2:
                        i2=i2+1
                    else:
                        j2=j2+1
                    if obj2.nom == z.nom :
                        obj2.nom = z.nom
                        obj2.cooperative=obj2.cooperative + i2
                        obj2.individuelle=obj2.individuelle + j2
                        
                    else:
                        obj2=ActorActions(z.nom,i2,j2)
                        listeOrganisations.append(obj2)
                
                    i2=0
                    j2=0
                                   
    i3=0
    j3 = 0
    obj3 = ActorActions('',0,0)
    listeRegions=[]
    for z in regions:
        for y in  actions:
            for x in regionsActions:
                if x.action_id==y.id and x.nom_id==z.id:
                    if y.type_action==2:
                        i3=i3+1
                    else:
                        j3=j3+1
                    if obj3.nom == z.region_name :
                        obj3.nom = z.region_name
                        obj3.cooperative=obj3.cooperative + i3
                        obj3.individuelle=obj3.individuelle + j3
                        
                    else:
                        obj3=ActorActions(z.region_name ,i3,j3)
                        listeRegions.append(obj3)
                
                    i3=0
                    j3=0
    


    context={
        'listeRegions':listeRegions,
        'listeOrganisations': listeOrganisations,
        'listeInvestisseurs':listeInvestisseurs,
        'listEntreprises' : listEntreprises,
        'regionsActions':regions,
        'entreprise' : entreprises,
        'actions' : actions,
        'investisseurs' : investisseurs,
        'regions' : regions,
        
        }

    return  render(request,'acteurs.html',{'data':context})

class ActionsCoopInd:
    def __init__(self,name,theme,type,odd):
        self.nom = name
        self.theme = theme
        self.type = type
        self.odd = odd

def actions(request):

    organisationActions = OrganisationAction.objects.all()
    investisseurActions = InvestisseurAction.objects.all()
    entrepriseActions = EntrepriseAction.objects.all()
    regionsActions = RegionAction.objects.all()
    entreprises = Entreprise.objects.all()
    actions = Action.objects.all()
    investisseurs = Investisseur.objects.all()
    regions = region.objects.all()
    organisations = Organisation.objects.all()
    
   
    listeCooperatives=[]
    listeIndividuelles=[]
    for x in actions:
        if x.type_action==1:
            if x.theme == 1:
                x.theme = 'Occupation du sol'
            else:
                if x.theme == 2:
                    x.theme = "Eau"
                else:
                    if x.theme == 3:
                        x.theme = "Energie"
                    else:
                        if x.theme == 4:
                            x.theme = "Industrie"
                        else:
                            if x.theme == 5:
                                x.theme = "Transport"
                            else:
                                if x.theme == 6:
                                    x.theme = "Océan et zones cotières"
            if x.Objectifs_de_développement_durable == 1:
                x.Objectifs_de_développement_durable = "Énergie abordable et propre"
            else:
                if x.Objectifs_de_développement_durable == 2:
                    x.Objectifs_de_développement_durable = "Innovation et infrastructure de l'industrie"
                else:
                    if x.Objectifs_de_développement_durable == 3:
                        x.tObjectifs_de_développement_durable = "Pas de pauvreté"
                    else:
                        if x.Objectifs_de_développement_durable== 4:
                            x.Objectifs_de_développement_durable = "Éducation de qualité"
                        else:
                            if x.Objectifs_de_développement_durable == 5:
                                x.Objectifs_de_développement_durable = "Villes et communautés durables"
                            else:
                                if x.Objectifs_de_développement_durable == 6:
                                    x.Objectifs_de_développement_durable = "Consommation et production responsables"
            objCooperative = ActionsCoopInd(x.nom_action,x.theme,x.type,x.Objectifs_de_développement_durable)
            listeCooperatives.append(objCooperative)
        else:
            if x.theme == 1:
                x.theme = 'Occupation du sol'
            else:
                if x.theme == 2:
                    x.theme = "Eau"
                else:
                    if x.theme == 3:
                        x.theme = "Energie"
                    else:
                        if x.theme == 4:
                            x.theme = "Industrie"
                        else:
                            if x.theme == 5:
                                x.theme = "Transport"
                            else:
                                if x.theme == 6:
                                    x.theme = "Océan et zones cotières"
            if x.Objectifs_de_développement_durable == 1:
                x.Objectifs_de_développement_durable = "Énergie abordable et propre"
            else:
                if x.Objectifs_de_développement_durable == 2:
                    x.Objectifs_de_développement_durable = "Innovation et infrastructure de l'industrie"
                else:
                    if x.Objectifs_de_développement_durable == 3:
                        x.tObjectifs_de_développement_durable = "Pas de pauvreté"
                    else:
                        if x.Objectifs_de_développement_durable== 4:
                            x.Objectifs_de_développement_durable = "Éducation de qualité"
                        else:
                            if x.Objectifs_de_développement_durable == 5:
                                x.Objectifs_de_développement_durable = "Villes et communautés durables"
                            else:
                                if x.Objectifs_de_développement_durable == 6:
                                    x.Objectifs_de_développement_durable = "Consommation et production responsables"
            objIndividuelle = ActionsCoopInd(x.nom_action,x.theme,x.type,x.Objectifs_de_développement_durable)
            listeIndividuelles.append(objIndividuelle)

    listeOccSol1=[]
    listeEau1=[]
    listeOcean1=[]
    listeEnergie1=[]
    listeIndustrie1=[]
    listeTransport1=[]
    listeOccSol=[]
    listeEau=[]
    listeOcean=[]
    listeEnergie=[]
    listeIndustrie=[]
    listeTransport=[]

    for x in listeCooperatives:
        if x.theme== 'Occupation du sol':
            listeOccSol.append(x)
        else:
            if x.theme== 'Eau': 
                listeEau.append(x) 
            else:
                if x.theme== 'Energie': 
                    listeEnergie.append(x)   
                else:
                    if x.theme== 'Industrie':   
                        listeIndustrie.append(x)
                    else:
                        if x.theme== 'Transport':
                            listeTransport.append(x)
                        else:
                            if  x.theme== 'Océan et zones cotières':
                                listeOcean.append(x)

    for x in listeIndividuelles:
        if x.theme== 'Occupation du sol':
            listeOccSol1.append(x)
        else:
            if x.theme== 'Eau': 
                listeEau1.append(x) 
            else:
                if x.theme== 'Energie': 
                    listeEnergie1.append(x)   
                else:
                    if x.theme== 'Industrie':   
                        listeIndustrie1.append(x)
                    else:
                        if x.theme== 'Transport':
                            listeTransport1.append(x)
                        else:
                            if  x.theme== 'Océan et zones cotières':
                                listeOcean1.append(x)                           
    nbrActions = 0
    nbrInvest = 0
    nbrEntreprise = 0
    nbrOrganisation = 0
    nbrRegion = 0
    nbrActeurs = 0
    for a in actions:
        nbrActions = nbrActions+1
    
       
    
       
    
    
    #count the number of regions
    id_reg = 0
    for z in regions:
        for y in actions:
            for  x in regionsActions:
                if x.action_id==y.id and x.nom_id==z.id:
                    if id_reg==x.nom_id:
                        nbrRegion  = nbrRegion
                        id_reg = x.nom_id
                    else:
                        nbrRegion  = nbrRegion +1 
                        id_reg =x.nom_id
    
    #count the number of ivestors
    id_invest =0
    for z in investisseurs:
        for y in actions:
            for  x in investisseurActions:
                if x.action_id==y.id and x.investisseur_id==z.id:
                    
                    if id_invest==x.investisseur_id:
                        nbrInvest = nbrInvest 
                        id_invest=x.investisseur_id
                    else:
                        nbrInvest = nbrInvest + 1 
                        id_invest=x.investisseur_id


    #count the number of entreprises
    id_entrep =0
    for z in entreprises:
        for y in actions:
            for  x in entrepriseActions:
                if x.action_id==y.id and x.entreprise_id==z.id:
                    
                    if id_entrep==x.entreprise_id:
                        nbrEntreprise = nbrEntreprise
                        id_entrep=x.entreprise_id
                    else:
                        nbrEntreprise = nbrEntreprise+1 
                        id_entrep=x.entreprise_id

    #count the number of organisations
    id_orga =0
    for z in entreprises:
        for y in actions:
            for  x in organisationActions:
                if x.action_id==y.id and x.organisation_id==z.id:                  
                    if id_orga==x.organisation_id:
                        nbrOrganisation = nbrOrganisation
                        id_entrep=x.organisation_id
                    else:
                        nbrOrganisation = nbrOrganisation+1 
                        id_entrep=x.organisation_id                   

    nbrActeurs = nbrOrganisation + nbrEntreprise + nbrInvest +nbrRegion
                          
    filter = FilterAction(request.GET,queryset=actions)
    actions = filter.qs                              

    context={
        'filter': filter,
        'nbrRegion' : nbrRegion ,
        'nbrInvestisseur' : nbrInvest,
        'nbrEntreprise' : nbrEntreprise,
        'nbrOrganisation' : nbrOrganisation,
        'nbrActions' : nbrActions,
        'nbrActeurs' : nbrActeurs,
        'listeOccSol' : listeOccSol,
        'listeEau' : listeEau,
        'listeEnergie': listeEnergie,
        'listeIndustrie': listeIndustrie,
        'listeTransport':listeTransport,
        'listeOcean':listeOcean,
        'listeOccSol1' : listeOccSol1,
        'listeEau1' : listeEau1,
        'listeEnergie1': listeEnergie1,
        'listeIndustrie1': listeIndustrie1,
        'listeTransport1':listeTransport1,
        'listeOcean1':listeOcean1,
        'listeCooperatives':listeCooperatives,
        'isteIndividuelles':listeIndividuelles,
        'regionsActions':regionsActions,
        'entreprises' : entreprises,
        'actions' : actions,
        'investisseurs' : investisseurs,
        'regions' : regions,
        'organisationActions': organisationActions,
        'investisseurActions' : investisseurActions,
        'entrepriseActions' : entrepriseActions,
        'organisations' : organisations
        
        }

    return render(request,'actions.html',{'data':context})