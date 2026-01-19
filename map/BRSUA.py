import folium


carte = folium.Map(location=[-8.39, -34.89], zoom_start=12)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6
    ).add_to(carte)



zone1_points = [
    [-8.389683, -34.927333],  
    [-8.375700, -34.870183],  
    [-8.380717, -34.866667],  
    [-8.391717, -34.866667], 
    [-8.404100, -34.917250]  
]
ajouter_polygone(carte, zone1_points, 'blue')


zone2_points = [
    [-8.375700, -34.870183],  
    [-8.374850, -34.866667], 
    [-8.380717, -34.866667], 
    [-8.413333, -34.873417]  
]
ajouter_polygone(carte, zone2_points, 'green')


carte.save("BRSUA.html")
