import django_filters
from django_filters import DateFilter, CharFilter
from .models import *
class FilterDocument(django_filters.FilterSet):
	
	class Meta:
		model = Document
		#fields = '__all__'
		fields = ['region','titre', 'auteur']
		#exclude = ['photo', 'fichier']
        #exclude = ['photo','fichier','description','date_insertion']

class FilterAction(django_filters.FilterSet):
	
	class Meta:
		model = Action
		#fields = '__all__'
		fields = ['Location','type','nom_action']
		

		