import folium


def dm_to_decimal(coord_str):
    parts = coord_str.split('°')
    degrees = float(parts[0])
    rest = parts[1].replace("'", "").split()
    minutes = float(rest[0])
    direction = rest[1] if len(rest) > 1 else rest[0]
    
    decimal = degrees + minutes/60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


def parse_coords(lat_str, lon_str):
    lat = dm_to_decimal(lat_str)
    lon = dm_to_decimal(lon_str)
    return [lat, lon]


carte = folium.Map(location=[51.35, 2.55], zoom_start=11)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)



westhinder_points = [
    parse_coords("51°25.95' N", "002°34.92' E"), 
    parse_coords("51°25.95' N", "002°40.30' E"),  
    parse_coords("51°24.40' N", "002°40.30' E"),  
    parse_coords("51°23.95' N", "002°36.90' E"),  
    parse_coords("51°23.95' N", "002°33.32' E")  
]


ajouter_polygone(carte, westhinder_points, 'blue')


westhinder_labels = [
    'WH-1: 51°25.95′ N, 002°34.92′ E',
    'WH-2: 51°25.95′ N, 002°40.30′ E',
    'WH-3: 51°24.40′ N, 002°40.30′ E',
    'WH-4: 51°23.95′ N, 002°36.90′ E',
    'WH-5: 51°23.95′ N, 002°33.32′ E'
]






oostdyck_points = [
    parse_coords("51°20.40' N", "002°31.50' E"), 
    parse_coords("51°20.40' N", "002°37.00' E"),  
    parse_coords("51°19.95' N", "002°34.50' E"),
    parse_coords("51°19.60' N", "002°33.80' E"), 
    parse_coords("51°19.60' N", "002°31.50' E")   
]


ajouter_polygone(carte, oostdyck_points, 'green')


oostdyck_labels = [
    'OD-1: 51°20.40′ N, 002°31.50′ E',
    'OD-2: 51°20.40′ N, 002°37.00′ E',
    'OD-3: 51°19.95′ N, 002°34.50′ E',
    'OD-4: 51°19.60′ N, 002°33.80′ E',
    'OD-5: 51°19.60′ N, 002°31.50′ E'
]



carte.save("BEANR.html")

