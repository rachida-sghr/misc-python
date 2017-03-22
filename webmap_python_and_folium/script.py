import folium
import pandas

# read date from csv file
data_frame=pandas.read_csv('Volcanoes-USA.txt')

#create a map centered at the mean latitude and longitude from volcanoes data
map = folium.Map(location=[data_frame['LAT'].mean(),data_frame['LON'].mean()], zoom_start=4, tiles= 'Mapbox Bright')


def marker_color(elevation):
	"""
	returns a maker color according to volcanoes elevetion
	"""
	minimum = int(min(data_frame['ELEV'])) #minimum of all volcanoes elevations
	step= int((max(data_frame['ELEV'])-min(data_frame['ELEV']))/3)

	if elevation in range(minimum,minimum+step):
		return 'green'
	elif elevation in range(minimum+step,minimum+step*2):
		return 'orange'
	else:
		return 'red'

#create a feature group to group markers and then add in as a layer		
feature_group= folium.FeatureGroup(name='Volcanoes location')

#add volcanoes markers to feature_group using maker_color function
for lat,lon,name,elevation in zip(data_frame['LAT'], data_frame['LON'], data_frame['NAME'], data_frame['ELEV']):
	folium.Marker([lat,lon],
		   popup = name,
		   icon = folium.Icon(color= marker_color(elevation))
		   ).add_to(feature_group)

feature_group.add_to(map)

# add polygon map and color countries according to their population 
data = open('world_population.json')
name = 'Wold population'
worldpop=folium.GeoJson(data=data,
						name=name,
						style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005']<=10000000
						 						 else 'orange' if 10000000<x['properties']['POP2005']<=20000000
						 						 else 'red'})

worldpop.add_to(map)

folium.LayerControl().add_to(map)

#create html visualization
map.save('test.html') 










