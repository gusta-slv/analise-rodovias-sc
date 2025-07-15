#Code to extract coordinates for federal highways in SC
import geopandas as gpd
from shapely.geometry import Point, Polygon
import pandas as pd
import fiona
from lxml import etree
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
import numpy as np
#Creating empty lists for uf e ds_coinc
uf = []
ds_coinc = []
#Starting to read the kml file
tree = ET.parse("C:/Users/gusta/Git/projetos/rodovias_files/snv_202504A.kml")
root = tree.getroot()
namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}
#Defining which elements info to get inside the SimpleData in the kml. First is the sd_uf
xpath_1 = ".//kml:Placemark//kml:ExtendedData//kml:SchemaData//kml:SimpleData[@name='sg_uf']"
for elem in root.findall(xpath_1, namespaces):
    uf.append(elem.text)
#Second is the ds_coinc
xpath_2 = ".//kml:Placemark//kml:ExtendedData//kml:SchemaData//kml:SimpleData[@name='ds_coinc']"
for elem in root.findall(xpath_2, namespaces):
    ds_coinc.append(elem.text)
#Creating dataframe with extracted info from the kml
coord_df = pd.DataFrame({'uf':uf, 'ds_coinc':ds_coinc})
print("ok")
#Reading  the kml file to a geodataframe
my_map = gpd.read_file('C:/Users/gusta/Git/projetos/rodovias_files/snv_202504A.kml', driver='KML')
my_map
#Joining the data from the dataframe and the data from the geodataframe
coord_map_df = my_map
coord_map_df.insert(0, "uf", coord_df["uf"])
coord_map_df.insert(1, "ds_coinc", coord_df["ds_coinc"])
#Ploting the full map
coord_map_df.plot()
plt.show()
#Filtering the geodataframe to show only data from SC and plotting the map
filt_coord_map_df = coord_map_df[coord_map_df.uf=="SC"]
filt_coord_map_df.plot()
plt.show()
print("ok")

test = filt_coord_map_df.explode(ignore_index=True)
a = test.get_coordinates(index_parts=True)

a["ds_coinc"] = ""

#Adding highway codename to the latitude/longitude dataframe
len_df = len(filt_coord_map_df.index.unique())
for i in range(len_df):
    print(i)
    for j in range(len(a.loc[i])):
        a.loc[([i],[j]), "ds_coinc"] = filt_coord_map_df.iloc[i,1]