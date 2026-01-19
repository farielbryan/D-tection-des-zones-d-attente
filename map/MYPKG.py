import folium
import math


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


carte = folium.Map(location=[2.85, 101.17], zoom_start=12)

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
        fill_opacity=0.6,
    ).add_to(carte)


polygone_points = [
    [dms_to_decimal(2, 47, 28, 'N'), dms_to_decimal(101, 15, 11, 'E')],  
    [dms_to_decimal(2, 50, 31, 'N'), dms_to_decimal(101, 15, 47, 'E')],  
    [dms_to_decimal(2, 48, 40, 'N'), dms_to_decimal(101, 19, 7, 'E')],  
    [dms_to_decimal(2, 47, 28, 'N'), dms_to_decimal(101, 19, 7, 'E')],   
    [dms_to_decimal(2, 48, 36, 'N'), dms_to_decimal(101, 16, 53, 'E')],  
    [dms_to_decimal(2, 46, 35, 'N'), dms_to_decimal(101, 16, 53, 'E')]   
]


ajouter_polygone(carte, polygone_points, 'blue')


point_pilotage_nord = [
    dm_to_decimal(3, 12.0, 'N'),  
    dm_to_decimal(101, 13.1, 'E') 
]


zone_attente_centre = [
    point_pilotage_nord[0], 
    point_pilotage_nord[1] + (0.5 / 60)  
]

ajouter_cercle(carte, zone_attente_centre, 0.5, 'red')




points_polygone = [
    'Point A: 02°47′28″ N, 101°15′11″ E',
    'Point B: 02°50′31″ N, 101°15′47″ E', 
    'Point C: 02°48′40″ N, 101°19′07″ E',
    'Point D: 02°47′28″ N, 101°19′07″ E',
    'Point E: 02°48′36″ N, 101°16′53″ E',
    'Point F: 02°46′35″ N, 101°16′53″ E'
]


carte.save("MYPKG.html")

