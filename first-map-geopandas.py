#================================================================
# This is a simple script to create a map using geopandas
#================================================================

# Install geopandas following the instructions in the link below,
# https://geopandas.org/en/stable/getting_started/install.html 


#--------------------------
# Import libraries
#--------------------------
import geopandas as gpd 
from geodatasets import get_path # get_path is a function that returns the path to the datasets 
import matplotlib.pyplot as plt

#--------------------------
# Read files 
#--------------------------
# Reproduce the example map in the link below,
# https://geopandas.org/en/stable/getting_started/introduction.html

path_to_data = get_path('nybb') 
gdf = gpd.read_file(path_to_data) 

print(gdf.head())


#--------------------------
# Measure area 
#--------------------------

gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
print(gdf["area"]) 


#--------------------------
# Make a map 
#--------------------------
gdf.plot('area', legend=True)  # Plot the area of each borough 
plt.show() # Show the plot 
