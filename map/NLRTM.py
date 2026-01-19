import folium

def dm_to_decimal(coord_str):
    parts = coord_str.split('°')
    degrees = float(parts[0])
    rest = parts[1].replace("′", "").split()
    minutes = float(rest[0])
    direction = rest[1] if len(rest) > 1 else rest[0]
    decimal = degrees + minutes/60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


carte = folium.Map(location=[52.03, 3.6], zoom_start=10)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)

def ajouter_cercle(carte, centre, rayon_nm, couleur):
    rayon_metres = rayon_nm * 1852
    folium.Circle(
        location=centre,
        radius=rayon_metres,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)




c1 = [52.0584, 3.3783]
ajouter_cercle(carte, c1, 1.5, 'blue')

c2 = [52.0150, 3.8133]  
ajouter_cercle(carte, c2, 0.8, 'red')

c3 = [51.9600, 3.1667]  
ajouter_cercle(carte, c3, 0.5, 'green')

c4 = [52.05, 3.9333]  
ajouter_cercle(carte, c4, 0.6, 'orange')



eurogeul_points = [
    [51.96, 3.17],  
    [52.02, 3.45],  
    [52.05, 3.80]   
]

maasgeul_points = [
    [52.05, 3.80],  
    [52.02, 4.00],  
    [51.98, 4.20]  
]


folium.PolyLine(
    eurogeul_points,
    color='navy',
    weight=3,
    opacity=0.7,
    popup='Chenal Eurogeul',
    tooltip='Eurogeul'
).add_to(carte)

folium.PolyLine(
    maasgeul_points,
    color='navy', 
    weight=3,
    opacity=0.7,
    popup='Chenal Maasgeul',
    tooltip='Maasgeul'
).add_to(carte)


carte.save("NLRTM.html")
