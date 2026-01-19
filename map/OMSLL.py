import folium


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


carte = folium.Map(location=[16.93, 54.05], zoom_start=12)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)




zone_a_points = [
    [dms_to_decimal(16, 56, 5, 'N'), dms_to_decimal(54, 2, 0, 'E')], 
    [dms_to_decimal(16, 56, 5, 'N'), dms_to_decimal(54, 4, 0, 'E')], 
    [dms_to_decimal(16, 55, 5, 'N'), dms_to_decimal(54, 4, 0, 'E')],  
    [dms_to_decimal(16, 55, 5, 'N'), dms_to_decimal(54, 2, 0, 'E')]   
]
ajouter_polygone(carte, zone_a_points, 'blue')


zone_b_points = [
    [dms_to_decimal(16, 55, 5, 'N'), dms_to_decimal(54, 4, 0, 'E')],  
    [dms_to_decimal(16, 55, 5, 'N'), dms_to_decimal(54, 2, 0, 'E')],  
    [dms_to_decimal(16, 55, 0, 'N'), dms_to_decimal(54, 2, 0, 'E')],  
    [dms_to_decimal(16, 55, 0, 'N'), dms_to_decimal(54, 4, 0, 'E')]   
]
ajouter_polygone(carte, zone_b_points, 'green')


zone_c_points = [
    [dms_to_decimal(16, 55, 0, 'N'), dms_to_decimal(54, 2, 0, 'E')],   
    [dms_to_decimal(16, 55, 0, 'N'), dms_to_decimal(54, 4, 0, 'E')],   
    [dms_to_decimal(16, 54, 0, 'N'), dms_to_decimal(54, 4, 0, 'E')],  
    [dms_to_decimal(16, 54, 0, 'N'), dms_to_decimal(54, 2, 0, 'E')]    
]
ajouter_polygone(carte, zone_c_points, 'orange')


zone_d_points = [
    [dms_to_decimal(16, 56, 0, 'N'), dms_to_decimal(54, 4, 0, 'E')],   
    [dms_to_decimal(16, 56, 0, 'N'), dms_to_decimal(54, 5, 40, 'E')],  
    [dms_to_decimal(16, 54, 0, 'N'), dms_to_decimal(54, 4, 0, 'E')],  
    [dms_to_decimal(16, 54, 0, 'N'), dms_to_decimal(54, 5, 40, 'E')]   
]
ajouter_polygone(carte, zone_d_points, 'red')





carte.save("OMSLL.html")

