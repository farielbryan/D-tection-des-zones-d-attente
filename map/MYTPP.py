import folium


carte = folium.Map(location=[1.15, 103.34], zoom_start=13)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


polygone_1 = [
    [1.277833, 103.582667],  
    [1.252667, 103.582667],  
    [1.225000, 103.577500],  
    [1.256000, 103.550000]   
]
ajouter_polygone(carte, polygone_1, 'blue')


polygone_2 = [
    [1.277833, 103.582667],  
    [1.277833, 103.593167],  
    [1.257667, 103.593167],  
    [1.252667, 103.582667]   
]
ajouter_polygone(carte, polygone_2, 'red')


points_reference = {
    'A': [1.277833, 103.582667],
    'B': [1.252667, 103.582667],
    'C': [1.225000, 103.577500],
    'D': [1.256000, 103.550000]
}


carte.save("MYTPP.html")