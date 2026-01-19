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
    sec = float(rest[1].replace('″', '').replace('E', '').replace('N', '').strip())
    dir_char = coord_str[-1] if coord_str[-1] in ['N', 'S', 'E', 'W'] else 'E'
    return dms_to_decimal(deg, min, sec, dir_char)


carte = folium.Map(location=[22.68, 113.71], zoom_start=13)

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
        fill_opacity=0.5,
    ).add_to(carte)


polygone1_points = [
    [parse_dms("22°40′00″N"), parse_dms("113°41′33″E")], 
    [parse_dms("22°40′00″N"), parse_dms("113°43′01″E")], 
    [parse_dms("22°38′40″N"), parse_dms("113°41′55″E")], 
    [parse_dms("22°38′40″N"), parse_dms("113°43′21″E")]   
]
ajouter_polygone(carte, polygone1_points, 'blue')


polygone2_points = [
    [parse_dms("22°41′18″N"), parse_dms("113°41′10″E")],  
    [parse_dms("22°41′18″N"), parse_dms("113°41′54″E")],  
    [parse_dms("22°40′00″N"), parse_dms("113°41′33″E")],  
    [parse_dms("22°40′00″N"), parse_dms("113°42′18″E")]   
]
ajouter_polygone(carte, polygone2_points, 'green')


shajiao1_center = [parse_dms("22°40′48″N"), parse_dms("113°42′30″E")]
ajouter_cercle(carte, shajiao1_center, 0.22, 'red')

shajiao2_center = [parse_dms("22°41′18″N"), parse_dms("113°42′12″E")]
ajouter_cercle(carte, shajiao2_center, 0.22, 'orange')

shajiao3_center = [parse_dms("22°41′37″N"), parse_dms("113°41′54″E")]
ajouter_cercle(carte, shajiao3_center, 0.20, 'purple')

shajiao4_center = [parse_dms("22°41′57″N"), parse_dms("113°41′38″E")]
ajouter_cercle(carte, shajiao4_center, 0.20, 'darkred')

shajiao10_center = [parse_dms("22°43′59″N"), parse_dms("113°40′01″E")]
ajouter_cercle(carte, shajiao10_center, 0.20, 'darkblue')


shajiao_centers = {
    '34SJ': shajiao1_center,
    '35SJ': shajiao2_center,
    '36SJ': shajiao3_center,
    '37SJ': shajiao4_center,
    '43SJ': shajiao10_center
}




points_importants = {
    'Shajiao (沙角)': [22.72, 113.68],
    'Dongguan (东莞)': [23.02, 113.75],
    'Guangzhou (广州)': [23.13, 113.26],
    'Baie de Guangzhou': [22.60, 113.80],
    'Rivière des Perles': [22.75, 113.60]
}




cote_points = [
    [22.65, 113.85],
    [22.70, 113.75],
    [22.75, 113.65],
    [22.80, 113.55],
    [22.85, 113.45]
]

riviere_points = [
    [22.70, 113.60],
    [22.75, 113.55],
    [22.80, 113.50],
    [22.85, 113.45]
]

folium.PolyLine(
    cote_points,
    color='brown',
    weight=4,
    opacity=0.7,
    popup='Ligne côtière approximative',
    tooltip='Côte'
).add_to(carte)

folium.PolyLine(
    riviere_points,
    color='blue',
    weight=3,
    opacity=0.6,
    popup='Rivière des Perles',
    tooltip='Rivière'
).add_to(carte)



carte.save("CNNSA.html")

