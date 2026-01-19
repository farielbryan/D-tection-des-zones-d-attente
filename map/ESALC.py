import folium


carte = folium.Map(location=[38.19, -0.27], zoom_start=12)


def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


centre_secteur_1 = [38.28833, -0.43583]
folium.Circle(
    location=centre_secteur_1,
    radius=926,  
    color='green',
    fill=True,
    fill_opacity=0.3,
).add_to(carte)



secteur_2 = [
    [38.31717, -0.46317],  
    [38.33150, -0.45450], 
    [38.32317, -0.43767],  
    [38.30850, -0.44617]  
]
ajouter_polygone(carte, secteur_2, 'red')


secteur_3 = [
    [38.32917, -0.47983],  
    [38.33633, -0.47467], 
    [38.33250, -0.46550],  
    [38.32517, -0.47100]   
]
ajouter_polygone(carte, secteur_3, 'blue')

carte.save("ESALC.html")
