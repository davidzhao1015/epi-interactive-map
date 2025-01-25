#================================================================
# This script creates an interactive map using Plotly.
#================================================================

# Reference: https://plotly.com/python/choropleth-maps/ 

#---------------------------------------------------------------
# Step 1 - Read the GeoJSON data from the URL 
#---------------------------------------------------------------
from urllib.request import urlopen # To read the data from the URL
import json # To read the data in JSON format 
# Read the GeoJSON data from the URL
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

#---------------------------------------------------------------
# Read the unemployment data from CSV file
#---------------------------------------------------------------
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv", dtype={"fips": str})    

#---------------------------------------------------------------
# Step 3 - Create the map
#---------------------------------------------------------------
import plotly.express as px
import plotly.io as pio
import kaleido # This package is required to save the map as a static image
fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa", # The scope of the map 
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#---------------------------------------------------------------
# Step 4 - Save the map as a static image
#---------------------------------------------------------------
# Save the map as a static image
pio.write_image(fig, 'first-interactive-map-plotly.png') 