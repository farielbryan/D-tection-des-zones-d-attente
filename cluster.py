import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint, Polygon
import matplotlib.pyplot as plt



#cluster1 = np.random.normal(loc=[2.15, 41.35], scale=0.01, size=(300, 2))
#cluster2 = np.random.normal(loc=[2.20, 41.40], scale=0.01, size=(300, 2))
#cluster3 = np.random.normal(loc=[2.25, 41.32], scale=0.01, size=(300, 2))



# Cluster centré sur A
clusterA = np.random.normal(loc=[29.888889, 122.208333], scale=0.001, size=(300, 2))

# Cluster centré sur B
clusterB = np.random.normal(loc=[29.888889, 122.225000], scale=0.001, size=(300, 2))

# Cluster centré sur C
clusterC = np.random.normal(loc=[29.875000, 122.225000], scale=0.001, size=(300, 2))

# Cluster centré sur D
clusterD = np.random.normal(loc=[29.875000, 122.203333], scale=0.001, size=(300, 2))
coords = np.vstack((cluster1, cluster2, cluster3))
data = pd.DataFrame(coords, columns=["lon", "lat"])


db = DBSCAN(eps=0.01, min_samples=20).fit(coords)
data["cluster"] = db.labels_


polygons = []
for i in db.labels_:
    if i == -1:  
        continue
    cluster_points = coords[data["cluster"] == i]
    trace = MultiPoint(cluster_points).convex_hull
    polygons.append(trace)


fig, ax = plt.subplots()
plt.scatter(data["lon"], data["lat"], c=data["cluster"], s=5, alpha=1)

for i in polygons:
    if isinstance(i, Polygon):
        x, y = i.exterior.xy
        ax.plot(x, y, color="black")
    else:
        for j in i.geoms:  
            if isinstance(j, Polygon):
                x, y = j.exterior.xy
                ax.plot(x, y, color="grey")

plt.title("Zones d'attente détectée")
plt.xlabel("Longitude")
plt.ylabel("Latitude")


plt.savefig('clustering_port.png')
plt.close()