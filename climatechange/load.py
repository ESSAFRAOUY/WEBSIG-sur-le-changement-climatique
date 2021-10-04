from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import region,Regions

layer_limites = {
    'region_name' : 'Region',
    'surface' : 'Surface_Km',
    'geometrie' : 'MULTIPOLYGON',
    
}
limites_administratives = Path(__file__).resolve().parent / 'data' / 'Dec_regions.shp'

def run(verbose=True):
    la = LayerMapping(region, limites_administratives, layer_limites, transform=False)
    la.save(strict=True, verbose=verbose)


