import folium


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


carte = folium.Map(location=[38.85, 26.95], zoom_start=11)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)




zone1_points = [
    [dms_to_decimal(38, 49, 0, 'N'), dms_to_decimal(26, 57, 48, 'E')],   
    [dms_to_decimal(38, 49, 0, 'N'), dms_to_decimal(26, 58, 24, 'E')],  
    [dms_to_decimal(38, 49, 39, 'N'), dms_to_decimal(26, 58, 24, 'E')], 
    [dms_to_decimal(38, 49, 39, 'N'), dms_to_decimal(26, 57, 48, 'E')] 
]
ajouter_polygone(carte, zone1_points, 'red')


zone2_points = [
    [dms_to_decimal(38, 53, 0, 'N'), dms_to_decimal(26, 59, 30, 'E')],  
    [dms_to_decimal(38, 52, 12, 'N'), dms_to_decimal(26, 59, 30, 'E')], 
    [dms_to_decimal(38, 51, 36, 'N'), dms_to_decimal(26, 57, 48, 'E')], 
    [dms_to_decimal(38, 53, 0, 'N'), dms_to_decimal(26, 57, 48, 'E')]  
]
ajouter_polygone(carte, zone2_points, 'blue')


zone3_points = [
    [dms_to_decimal(38, 53, 0, 'N'), dms_to_decimal(26, 57, 48, 'E')],   
    [dms_to_decimal(38, 53, 0, 'N'), dms_to_decimal(26, 56, 0, 'E')],   
    [dms_to_decimal(38, 51, 36, 'N'), dms_to_decimal(26, 57, 48, 'E')] 
]
ajouter_polygone(carte, zone3_points, 'orange')


zone4_points = [
    [dms_to_decimal(38, 46, 15, 'N'), dms_to_decimal(26, 54, 21, 'E')], 
    [dms_to_decimal(38, 46, 0, 'N'), dms_to_decimal(26, 53, 54, 'E')],  
    [dms_to_decimal(38, 45, 15, 'N'), dms_to_decimal(26, 53, 54, 'E')], 
    [dms_to_decimal(38, 46, 35, 'N'), dms_to_decimal(26, 51, 56, 'E')], 
    [dms_to_decimal(38, 46, 51, 'N'), dms_to_decimal(26, 52, 24, 'E')] 
]
ajouter_polygone(carte, zone4_points, 'green')


zone5_points = [
    [dms_to_decimal(38, 47, 39, 'N'), dms_to_decimal(26, 52, 30, 'E')], 
    [dms_to_decimal(38, 48, 24, 'N'), dms_to_decimal(26, 52, 18, 'E')], 
    [dms_to_decimal(38, 48, 24, 'N'), dms_to_decimal(26, 53, 42, 'E')], 
    [dms_to_decimal(38, 47, 39, 'N'), dms_to_decimal(26, 54, 12, 'E')] 
]
ajouter_polygone(carte, zone5_points, 'purple')


zone6_points = [
    [dms_to_decimal(38, 49, 6, 'N'), dms_to_decimal(26, 52, 6, 'E')],   
    [dms_to_decimal(38, 48, 24, 'N'), dms_to_decimal(26, 52, 18, 'E')], 
    [dms_to_decimal(38, 48, 24, 'N'), dms_to_decimal(26, 53, 42, 'E')], 
    [dms_to_decimal(38, 49, 6, 'N'), dms_to_decimal(26, 53, 12, 'E')]   
]
ajouter_polygone(carte, zone6_points, 'darkred')


zone7_points = [
    [dms_to_decimal(38, 51, 30, 'N'), dms_to_decimal(26, 53, 30, 'E')], 
    [dms_to_decimal(38, 51, 20, 'N'), dms_to_decimal(26, 54, 12, 'E')], 
    [dms_to_decimal(38, 51, 0, 'N'), dms_to_decimal(26, 53, 24, 'E')]  
]
ajouter_polygone(carte, zone7_points, 'gray')




carte.save("TRALI.html")

