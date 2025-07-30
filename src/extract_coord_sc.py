import geopandas as gpd
import pandas as pd
#Defining the path to the shapefile folder with files
shapefile_path = "C:/Users/gusta/Git/projetos/rodovias_files/Rodovias SC/Rodovias_SC_04.24/Rodovias_SC.shp"
#Turning to GeoDataframe and then to Dataframe to visualize data
gdf = gpd.read_file(shapefile_path)
df = pd.DataFrame(gdf)
print("")