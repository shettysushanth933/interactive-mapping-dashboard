import streamlit as st
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

if 'selected_district' not in st.session_state:
    st.session_state['selected_district'] = 'Bidar'
    
st.set_page_config(page_title="Dashboard", layout="wide")

st.title('Interactive Highway Dashboard')

st.sidebar.title("About")
st.sidebar.info('Explore the Roads')
st.sidebar.markdown('Click on any feature to see the stats. '
  'The text and chart below will update as you click on the map.')

selected = st.sidebar.markdown(f'Current selection: :red[{st.session_state.selected_district}]')

data_url = 'https://github.com/spatialthoughts/python-dataviz-web/releases/' \
        'download/osm/'
gpkg_file = 'karnataka.gpkg'
csv_file = 'highway_lengths_by_district.csv'

@st.cache_data
def read_gdf(url, layer):
    gdf = gpd.read_file(url, layer=layer)
    return gdf

@st.cache_data
def read_csv(url):
    df = pd.read_csv(url)
    return df
    
   
gpkg_url = data_url + gpkg_file
csv_url = data_url + csv_file
districts_gdf = read_gdf(gpkg_url, 'karnataka_districts')
roads_gdf = read_gdf(gpkg_url, 'karnataka_highways')
lengths_df = read_csv(csv_url)



m = leafmap.Map(
    layers_control=True,
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
)

m.add_gdf(
    gdf=districts_gdf,
    layer_name='districts',
    zoom_to_layer=True,
    info_mode='none',
    style={'color': 'blue', 'fillOpacity': 0.3, 'weight': 0.5},
    )

 
map_data = m.to_streamlit(800, 600, bidirectional=True)



district_lengths = lengths_df[lengths_df['DISTRICT'] == st.session_state.selected_district]

fig, ax = plt.subplots(1, 1)
district_lengths.plot(kind='bar', ax=ax, color=['blue', 'red', 'white'], 
  ylabel='Kilometers', xlabel='Category')
ax.get_xaxis().set_ticklabels([])
ax.set_ylim(0, 2500)
stats = st.sidebar.pyplot(fig)

if map_data['last_object_clicked']:
    clicked_district = map_data['last_active_drawing']['properties']['DISTRICT']
    st.session_state.selected_district = clicked_district
    selected.write(f'Current selection: :red[{st.session_state.selected_district}]')