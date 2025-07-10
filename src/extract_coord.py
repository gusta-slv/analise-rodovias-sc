#Code to extract coordinates for federal highways in SC
import geopandas as gpd
from shapely.geometry import Point, Polygon
import pandas as pd
import fiona
fiona.drvsupport.supported_drivers['KML'] = 'rw'
my_map = gpd.read_file('C:/Users/gusta/Git/projetos/rodovias_files/snv_202504A.kml', driver='KML')
my_map
df_map = pd.DataFrame(my_map)
df_map