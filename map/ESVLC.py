import folium


carte = folium.Map(location=[39.27, -0.14], zoom_start=5)


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
    minutes = float(parts[1].replace(',', '.').replace('’', '').replace('"', '').strip())
    decimal_degrees = degrees + minutes / 60.0
    if hemisphere in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

n1 = conversion("39°27.251", 'N')
n2 = conversion("000°14.804", 'W')
n3 = conversion("39°27.251", 'N')
n4 = conversion("000°12.714", 'W')
n5 = conversion("39°26.170", 'N')
n6 = conversion("000°12.714", 'W')
n7 = conversion("39°26.170", 'N')
n8 = conversion("000°14.804", 'W')
zone_nord_points = [
    [n1, n2],
    [n3, n4],
    [n5, n6],
    [n7, n8]
]


s1 = conversion("39°24.297", 'N')
s2 = conversion("000°17.029", 'W')
s3 = conversion("39°24.297", 'N')
s4 = conversion("000°12.714", 'W')
s5 = conversion("39°23.000", 'N')
s6 = conversion("000°12.714", 'W')
s7 = conversion("39°23.000", 'N')
s8 = conversion("000°17.029", 'W')
zone_sud_points = [
    [s1, s2],
    [s3, s4],
    [s5, s6],
    [s7, s8]
]


ajouter_polygone(carte, zone_nord_points, 'blue')
ajouter_polygone(carte, zone_sud_points, 'green')


carte.save("ESVLC.html")
