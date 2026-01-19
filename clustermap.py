import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint, Polygon
import folium


cluster1 = np.random.normal(loc=[2.15, 41.35], scale=0.01, size=(300, 2))
cluster2 = np.random.normal(loc=[2.20, 41.40], scale=0.01, size=(300, 2))
cluster3 = np.random.normal(loc=[2.25, 41.32], scale=0.01, size=(300, 2))
coords = np.vstack((cluster1, cluster2, cluster3))
data = pd.DataFrame(coords, columns=["lon", "lat"])


db = DBSCAN(eps=0.01, min_samples=20).fit(coords)
data["cluster"] = db.labels_


polygons = []
for i in set(db.labels_):
    if i == -1:
        continue
    cluster_points = coords[data["cluster"] == i]
    trace = MultiPoint(cluster_points).convex_hull
    polygons.append(trace)


center_lat = data['lat'].mean()
center_lon = data['lon'].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles='OpenStreetMap')


colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'pink', 'brown', 'gray', 'olive']


def get_cluster_color(cluster_id, colors_list):
    if cluster_id == -1:
        return 'gray'
    return colors_list[int(cluster_id) % len(colors_list)]


for idx, row in data.iterrows():
    color = get_cluster_color(row['cluster'], colors)
    
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=3 ,
        color=color,
        fill=True,
        fillColor=color,
        fillOpacity=0.6 ,
    ).add_to(m)


for i, polygon in enumerate(polygons):
    if isinstance(polygon, Polygon):
        coords_list = [(lat, lon) for lon, lat in polygon.exterior.coords]
        color = colors[i % len(colors)]
        folium.Polygon(
            locations=coords_list,
            color=color,
            weight=3,
            fill=True,
            fillColor=color,
            fillOpacity=0.2,
        ).add_to(m)

m.save('zones_attente_port.html')