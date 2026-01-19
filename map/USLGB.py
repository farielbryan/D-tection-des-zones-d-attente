import folium
import math


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


def parse_dms(coord_str):
    parts = coord_str.split()
    deg = int(parts[0][:2])
    min = int(parts[0][3:5])
    sec = float(parts[0][6:-1])
    dir = parts[1]
    return dms_to_decimal(deg, min, sec, dir)


carte = folium.Map(location=[33.73, -118.15], zoom_start=13)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.5,
    ).add_to(carte)


zone_b = [
    [33.743611, -118.216667],  
    [33.736667, -118.210056], 
    [33.727278, -118.193583],  
    [33.723917, -118.196444], 
    [33.723917, -118.206306],  
    [33.716361, -118.231389],  
    [33.729444, -118.237111], 
    [33.731806, -118.230556], 
    [33.739667, -118.230833]  
]
ajouter_polygone(carte, zone_b, 'blue')


zone_d = [
    [33.739056, -118.125472],
    [33.736806, -118.121250], 
    [33.734667, -118.116944],
    [33.736417, -118.120278], 
    [33.740000, -118.117806], 
    [33.739583, -118.115833], 
    [33.727528, -118.101889], 
    [33.724389, -118.127750], 
    [33.727333, -118.130056]  
]
ajouter_polygone(carte, zone_d, 'red')


zone_e = [
    [33.747778, -118.175556], 
    [33.743611, -118.216667],  
    [33.740000, -118.220000],  
    [33.745000, -118.180000]  
]
ajouter_polygone(carte, zone_e, 'green')


zone_f = [
    [33.719000, -118.195833],  
    [33.725000, -118.212500],  
    [33.722500, -118.225500],  
    [33.712056, -118.212778]   
]
ajouter_polygone(carte, zone_f, 'purple')


zone_g = [
    [33.715000, -118.131667],  
    [33.714444, -118.161667],  
    [33.704194, -118.159167],  
    [33.704194, -118.145278]   
]
ajouter_polygone(carte, zone_g, 'orange')


zone_p = [
    [33.737361, -118.122000],  
    [33.737000, -118.121000],  
    [33.736500, -118.120000],  
    [33.736417, -118.120278],  
    [33.740000, -118.117806],  
    [33.739583, -118.115833],  
    [33.737500, -118.120000]  
]
ajouter_polygone(carte, zone_p, 'darkred')





carte.save("USLGB.html")

