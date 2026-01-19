import folium


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


def parse_dms(coord_str):
    parts = coord_str.split('°')
    deg = int(parts[0])
    rest = parts[1].split('′')
    min = int(rest[0])
    sec = float(rest[1].replace('″', '').replace('N', '').replace('E', '').strip())
    dir_char = coord_str[-1] if coord_str[-1] in ['N', 'S', 'E', 'W'] else 'N'
    return dms_to_decimal(deg, min, sec, dir_char)


carte = folium.Map(location=[35.9, 120.2], zoom_start=10)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)


chaoliandao_points = [
    [parse_dms("35°50′00″ N"), parse_dms("120°16′00″ E")],  
    [parse_dms("35°48′30″ N"), parse_dms("120°16′00″ E")],  
    [parse_dms("35°47′00″ N"), parse_dms("120°15′00″ E")],  
    [parse_dms("35°48′00″ N"), parse_dms("120°14′30″ E")]   
]
ajouter_polygone(carte, chaoliandao_points, 'blue')


qianhai1_points = [
    [parse_dms("36°00′46″ N"), parse_dms("120°20′41″ E")],
    [parse_dms("36°00′40″ N"), parse_dms("120°21′58″ E")],
    [parse_dms("36°00′12″ N"), parse_dms("120°21′42″ E")],
    [parse_dms("36°00′12″ N"), parse_dms("120°20′51″ E")]
]
ajouter_polygone(carte, qianhai1_points, 'green')


qianhai2_points = [
    [parse_dms("35°57′30″ N"), parse_dms("120°21′54″ E")],
    [parse_dms("35°57′30″ N"), parse_dms("120°22′42″ E")],
    [parse_dms("35°58′54″ N"), parse_dms("120°23′36″ E")],
    [parse_dms("35°58′54″ N"), parse_dms("120°21′24″ E")]
]
ajouter_polygone(carte, qianhai2_points, 'orange')


qianhai3_points = [
    [parse_dms("35°57′30″ N"), parse_dms("120°24′30″ E")],
    [parse_dms("35°57′30″ N"), parse_dms("120°26′30″ E")],
    [parse_dms("35°58′54″ N"), parse_dms("120°27′18″ E")],
    [parse_dms("35°58′54″ N"), parse_dms("120°25′18″ E")]
]
ajouter_polygone(carte, qianhai3_points, 'red')


tanker_points = [
    [parse_dms("36°05′42″ N"), parse_dms("120°13′06″ E")],
    [parse_dms("36°05′42″ N"), parse_dms("120°14′00″ E")],
    [parse_dms("36°04′51″ N"), parse_dms("120°14′00″ E")],
    [parse_dms("36°04′51″ N"), parse_dms("120°13′06″ E")]
]
ajouter_polygone(carte, tanker_points, 'purple')


inner_points = [
    [parse_dms("36°06′00″ N"), parse_dms("120°14′30″ E")],
    [parse_dms("36°06′00″ N"), parse_dms("120°16′50″ E")],
    [parse_dms("36°04′18″ N"), parse_dms("120°16′50″ E")],
    [parse_dms("36°04′18″ N"), parse_dms("120°14′30″ E")]
]
ajouter_polygone(carte, inner_points, 'darkblue')


dongjiakou_points = [
    [parse_dms("35°29′00″ N"), parse_dms("119°50′15″ E")],
    [parse_dms("35°29′50″ N"), parse_dms("119°53′50″ E")],
    [parse_dms("35°28′10″ N"), parse_dms("119°50′40″ E")],
    [parse_dms("35°30′30″ N"), parse_dms("119°52′50″ E")]
]
ajouter_polygone(carte, dongjiakou_points, 'darkgreen')


points_importants = {
    'Port de Qingdao': [36.066, 120.382],
    'Île de Chaoliandao': [35.88, 120.18],
    'Dongjiakou Port': [35.60, 119.90],
    'Jiaozhou Bay': [36.10, 120.25],
    'Qingdao City': [36.067, 120.383]
}

cote_points = [
    [36.15, 120.40],
    [36.05, 120.35],
    [35.95, 120.30],
    [35.85, 120.25],
    [35.75, 120.20],
    [35.65, 120.15],
    [35.55, 120.10],
    [35.45, 120.05]
]

folium.PolyLine(
    cote_points,
    color='brown',
    weight=4,
    opacity=0.7,
    popup='Ligne côtière approximative',
    tooltip='Côte'
).add_to(carte)


carte.save("CNQDG.html")

