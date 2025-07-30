import geopandas as gpd
import pandas as pd
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
#Defining the path to the shapefile folder with files
shapefile_path = "C:/Users/gusta/Git/projetos/rodovias_files/Rodovias SC/Rodovias_SC_04.24/Rodovias_SC.shp"
#Turning to GeoDataframe and then to Dataframe to visualize data
gdf = gpd.read_file(shapefile_path)
df = pd.DataFrame(gdf)
#Ploting to visualize coordinates
gdf.plot()
plt.show()

#Exploding coordinates from GeoDataframe to latitude/longitude
test = gdf.explode(ignore_index=True)
a = test.get_coordinates(index_parts=True)
#Adding column for the highway codename
a["rodovia"] = ""

#Adding highway codename to the latitude/longitude dataframe
len_df = len(gdf.index.unique())
for i in range(len_df):
    #print(i)
    for j in range(len(a.loc[i])):
        a.loc[([i],[j]), "rodovia"] = gdf.iloc[i,0]
print("")