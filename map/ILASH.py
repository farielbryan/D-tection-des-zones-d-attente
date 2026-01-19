import folium

carte = folium.Map(location=[31.815, 34.585], zoom_start=13)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


zone_points = [
    [31.83, 34.57],
    [31.83, 34.60],
    [31.80, 34.60],
    [31.80, 34.57],
    [31.83, 34.57] 
]

ajouter_polygone(carte, zone_points, 'blue')
carte.save("ILASH.html")