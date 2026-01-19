import folium


def dm_to_decimal(coord_str):
    parts = coord_str.split('°')
    degrees = float(parts[0])
    rest = parts[1].split('′')
    minutes = float(rest[0])
    direction = rest[1].strip()
    
    decimal = degrees + minutes/60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


carte = folium.Map(location=[56.1575, 10.215], zoom_start=15)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


point1 = [dm_to_decimal("56°09.462′ N"), dm_to_decimal("10°12.912′ E")]
point2 = [dm_to_decimal("56°09.455′ N"), dm_to_decimal("10°12.949′ E")]
point3 = [dm_to_decimal("56°09.451′ N"), dm_to_decimal("10°12.980′ E")]
point4 = [dm_to_decimal("56°09.457′ N"), dm_to_decimal("10°13.029′ E")]


zone_points = [point1, point2, point3, point4]

ajouter_polygone(carte, zone_points, 'blue')
carte.save("DRAAK.html")