#Code to extract coordinates for federal highways in SC
import geopandas as gpd
from shapely.geometry import Point, Polygon
import pandas as pd
import fiona
from lxml import etree
import xml.etree.ElementTree as ET
uf = []
ds_coinc = []
tree = ET.parse("C:/Users/gusta/Git/projetos/rodovias_files/snv_202504A.kml")
root = tree.getroot()
namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}
xpath_1 = ".//kml:Placemark//kml:ExtendedData//kml:SchemaData//kml:SimpleData[@name='sg_uf']"
for elem in root.findall(xpath_1, namespaces):
    print("sg_uf", elem.text)
    uf.append(elem.text)
xpath_2 = ".//kml:Placemark//kml:ExtendedData//kml:SchemaData//kml:SimpleData[@name='ds_coinc']"
for elem in root.findall(xpath_2, namespaces):
    ds_coinc.append(elem.text)
coord_df = pd.DataFrame({'uf':uf, 'ds_coinc':ds_coinc})
print("ok")
#fiona.drvsupport.supported_drivers['KML'] = 'rw'
#tree = etree.parse("C:/Users/gusta/Git/projetos/rodovias_files/snv_202504A.kml")

#for simple_data in tree.xpath("/kml:kml/kml:Document/kml:Folder/kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name='sg_uf']"):
 #   print(simple_data.text)
#my_map = gpd.read_file('C:/Users/gusta/Git/projetos/rodovias_files/snv_202504A.kml', driver='KML')
#my_map
#df_map = pd.DataFrame(my_map)
#df_map