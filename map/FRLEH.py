import folium

carte = folium.Map(location=[49.5, -0.2], zoom_start=10)


def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)

def conversion(coord, hemisphere):
    parts = coord.split('°')
    degrees = float(parts[0])
    minutes = float(parts[1].replace('’', '').replace('"', '').strip())
    decimal_degrees = degrees + minutes / 60.0
    if hemisphere in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

c1 = conversion("49°30.17’", 'N')
c2 = conversion("00°04.80’", 'W')
c3 = conversion("49°28.79’", 'N')
c4 = conversion("00°01.42’", 'W')
c5 = conversion("49°29.44’", 'N')
c6 = conversion("00°01.13’", 'W')
c7 = conversion("49°29.52’", 'N')
c8 = conversion("00°05.10’", 'W')
zone_1_points = [
    [c1, c2],
    [c3, c4],
    [c5, c6],
    [c7, c8]
]

d1 = conversion("49°37.50’", 'N')
d2 = conversion("00°17.40’", 'W')
d3 = conversion("49°34.50’", 'N')
d4 = conversion("00°17.40’", 'W')
d5 = conversion("49°37.50’", 'N')
d6 = conversion("00°12.40’", 'W')
d7 = conversion("49°34.50’", 'N')
d8 = conversion("00°12.40’", 'W')
zone_2_points = [
    [d1, d2],
    [d3, d4],
    [d5, d6],  
    [d7, d8]
]

e1 = conversion("49°35.00’", 'N')
e2 = conversion("00°10.00’", 'W')
e3 = conversion("49°33.00’", 'N')
e4 = conversion("00°06.95’", 'W')
e5 = conversion("49°35.00’", 'N')
e6 = conversion("00°06.95’", 'W')
e7 = conversion("49°33.00’", 'N')
e8 = conversion("00°10.00’", 'W')
zone_3_points = [
    [e1, e2],
    [e3, e4],
    [e5, e6],  
    [e7,e8]
]

ajouter_polygone(carte, zone_1_points, 'blue')
ajouter_polygone(carte, zone_2_points, 'red')
ajouter_polygone(carte, zone_3_points, 'green')
carte.save("FRLEH.html")