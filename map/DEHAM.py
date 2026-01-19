import folium


carte = folium.Map(location=[53.88, 8.8], zoom_start=10)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)

def ajouter_ligne(carte, points, couleur):
    folium.PolyLine(
        locations=points,
        color=couleur,
        weight=3,
    ).add_to(carte)


neuwerk_points = [
    [53.96133, 8.54042],  
    [53.96938, 8.47165],  
    [53.95000, 8.48000],  
    [53.94500, 8.53000]   
]
ajouter_polygone(carte, neuwerk_points, 'blue')

medem_points = [
    [53.87180, 8.73333],  
    [53.87980, 8.72510],  
    [53.88708, 8.71764],  
    [53.88000, 8.74000]   
]
ajouter_polygone(carte, medem_points, 'green')


neufeld_points = [
    [53.88459, 9.08021], 
    [53.87958, 9.06377],  
    [53.87430, 9.04593],  
    [53.86797, 9.02177],  
    [53.86318, 8.99515], 
    [53.85880, 8.96543],  
    [53.85714, 8.93611]  
]
ajouter_ligne(carte, neufeld_points, 'red')




carte.save("DEHAM.html")

