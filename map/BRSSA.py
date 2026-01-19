import folium


carte = folium.Map(location=[-12.95, -38.55], zoom_start=11)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)

def ajouter_cercle(carte, centre, rayon_nm, couleur):
    rayon_metres = rayon_nm * 1852
    folium.Circle(
        location=centre,
        radius=rayon_metres,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)

def conversion(coord, hemisphere):
    parts = coord.split('°')
    degrees = float(parts[0])
    minutes = float(parts[1].replace('′', '').replace('"', '').replace(',', '.').strip())
    decimal_degrees = degrees + minutes / 60.0
    if hemisphere in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees


zone_i_points = [
    [-12.92533, -38.54800],  
    [-12.92533, -38.52433],  
    [-12.94250, -38.52433], 
    [-12.93683, -38.54800]  
]
ajouter_polygone(carte, zone_i_points, 'blue')


zone_ii_points = [
    [-12.98733, -38.56000],  
    [-12.97217, -38.56000], 
    [-12.94667, -38.54017], 
    [-12.95333, -38.51500], 
    [-12.96500, -38.53833],  
    [-12.98733, -38.54233]   
]
ajouter_polygone(carte, zone_ii_points, 'red')


zone_iii_points = [
    [-12.93283, -38.59300], 
    [-12.94050, -38.56450], 
    [-12.98733, -38.56450], 
    [-12.98733, -38.57850]  
]
ajouter_polygone(carte, zone_iii_points, 'green')


zone_iv_centre = [-12.91733, -38.59700]
ajouter_cercle(carte, zone_iv_centre, 0.25, 'orange')


zone_v_points = [
    [-13.00500, -38.61000], 
    [-13.02500, -38.58333], 
    [-13.06500, -38.61333], 
    [-13.04500, -38.64000]  
]
ajouter_polygone(carte, zone_v_points, 'purple')

zone_vi_centre = [-12.90800, -38.60533]
ajouter_cercle(carte, zone_vi_centre, 0.25, 'darkred')


zone_vii_points = [
    [-12.97183, -38.53917], 
    [-12.97183, -38.52850], 
    [-12.98250, -38.54150],
    [-12.98250, -38.52850] 
]
ajouter_polygone(carte, zone_vii_points, 'pink')


zone_viii_centre = [-12.85819, -38.66633]
ajouter_cercle(carte, zone_viii_centre, 0.35, 'darkblue')

zone_ix_centre = [-12.84572, -38.67478]
ajouter_cercle(carte, zone_ix_centre, 0.35, 'darkgreen')


zone_x_centre = [-12.84147, -38.65675]
ajouter_cercle(carte, zone_x_centre, 0.35, 'gray')

carte.save("BRSSA.html")