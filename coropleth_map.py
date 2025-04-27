import pandas as pd
import plotly.express as px
import requests
import json
import plotly.io as pio

# Read the data
file = 'sorted_data.csv'
df = pd.read_csv(file)

# Filter data for 2019 and 2020
df = df[df['Year'].isin([2019, 2020])]

# Count crashes by borough and year
crashes_by_borough_year = df.groupby(['Year', 'BOROUGH']).size().reset_index(name='value')
crashes_by_borough_year['BOROUGH'] = crashes_by_borough_year['BOROUGH'].str.title()  # Standardize borough names
crashes_by_borough_year.rename(columns={'BOROUGH': 'borough'}, inplace=True)

geojson_url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/new-york-city-boroughs.geojson"
geojson_data = requests.get(geojson_url).json()

# Plotting with animation
fig = px.choropleth(
    crashes_by_borough_year,
    geojson=geojson_data,
    locations='borough',
    featureidkey='properties.name',  # This is the GeoJSON field that matches the borough name
    color='value',
    color_continuous_scale="Viridis",
    range_color=(0, crashes_by_borough_year['value'].max()),
    scope="usa",
    hover_name='borough',
    hover_data=['Year'],
    # Add animation frame
    animation_frame='Year',  # Add animation by year
    labels={'value': 'Crashes'},
    title='Crashes by Borough (2019 and 2020)',
)

fig.update_geos(fitbounds="locations", visible=False)  

# Save the figure as an HTML file
pio.write_html(fig, file="crashes_by_borough.html", auto_open=True)