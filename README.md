# 🚗 Interactive Highway Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Folium-43AA8B?logo=leaflet&logoColor=white" alt="Folium" />
  <img src="https://img.shields.io/badge/Leafmap-4CBB17?logo=leaflet&logoColor=white" alt="Leafmap" />
  <img src="https://img.shields.io/badge/GeoPandas-3276B1?logo=geopandas&logoColor=white" alt="GeoPandas" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white" alt="Matplotlib" />
</p>

---

This project is an **Interactive Highway Dashboard** built with [Streamlit](https://streamlit.io/), [Folium](https://python-visualization.github.io/folium/), and [leafmap](https://leafmap.org/). It allows users to explore highway statistics for districts in Karnataka, India, using an interactive map and dynamic charts.

## Features

- **Interactive Map:** Visualize Karnataka's districts and highways on a web map.
- **District Selection:** Click on any district to view its highway statistics.
- **Dynamic Sidebar:** The sidebar updates to show the currently selected district.
- **Bar Chart:** Displays the length of highways by category for the selected district.
- **Live Updates:** Both the sidebar and chart update instantly as you interact with the map.

## Tech Stack

- **Python**
- **Streamlit**
- **Folium**
- **Leafmap**
- **GeoPandas**
- **Pandas**
- **Matplotlib**

## How It Works

1. **Data Loading:**  
   - Loads district and highway data from a GeoPackage file.
   - Loads highway length statistics from a CSV file.

2. **Map Rendering:**  
   - Displays Karnataka districts on an interactive map.
   - Allows users to click on a district to select it.

3. **Sidebar & Chart:**  
   - The sidebar shows information about the dashboard and the currently selected district.
   - A bar chart visualizes highway lengths by category for the selected district.

## Getting Started

### Prerequisites

- Python 3.8+
- The following Python packages:
  - `streamlit`
  - `folium`
  - `leafmap`
  - `geopandas`
  - `pandas`
  - `matplotlib`

Install dependencies with:

```
pip install streamlit folium leafmap geopandas pandas matplotlib
```

### Running the App

1. Clone this repository:

   ```
   git clone https://github.com/shettysushanth933/interactive-mapping-dashboard.git
   cd interactive-mapping-dashboard
   ```

2. Start the Streamlit app:

   ```
   streamlit run app.py
   ```

3. Open the provided local URL in your browser to interact with the dashboard.

## Data Sources

- **Districts and Highways:**  
  [karnataka.gpkg](https://github.com/spatialthoughts/python-dataviz-web/releases/download/osm/karnataka.gpkg)
- **Highway Lengths by District:**  
  [highway_lengths_by_district.csv](https://github.com/spatialthoughts/python-dataviz-web/releases/download/osm/highway_lengths_by_district.csv)

## File Structure

- `app.py` — Main Streamlit application file.

## License

This project is for educational and demonstration purposes.

---