from pathlib import Path
import json
from plotly import express as px

#Convert json object into python object
path = Path(r'D:\python\data_visualization_with_python\earthquake_data\eq_data_30_day\readable_eq_data.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Extract features
features = all_eq_data['features']

#Extract mag, latitude and longitude
mags, lats, longs, titles = [], [], [], []

for feature in features:
    mag = feature['properties']['mag']
    long = feature['geometry']['coordinates'][0]
    lat = feature['geometry']['coordinates'][1]
    title = feature['properties']['title']

    #Append into respective lists
    mags.append(mag)
    lats.append(lat)
    longs.append(long)
    titles.append(title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=longs, size=mags, title=title, color=mags, 
                     color_continuous_scale='Plasma', labels={'color':'Magnitude'},
                     projection = 'natural earth', hover_name=titles,
                     )
fig.show()


