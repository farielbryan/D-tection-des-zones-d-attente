import folium


carte = folium.Map(location=[43.22, 4.98], zoom_start=12)


def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


zone_est = [
    [43.37567, 5.00005],  
    [43.37567, 4.97817],  
    [43.36315, 4.97290],  
    [43.32567, 4.99142],  
    [43.32567, 5.03950],  
    [43.32750, 5.04122]   
]
ajouter_polygone(carte, zone_est, 'red')


zone_ouest = [
    [43.39027, 4.93390],  
    [43.32567, 4.92285],  
    [43.32567, 4.97003],  
    [43.37795, 4.95503],  
    [43.38665, 4.94223]   
]
ajouter_polygone(carte, zone_ouest, 'blue')


zone_nord = [
    [43.41990, 4.90627],  
    [43.41780, 4.90540],  
    [43.40232, 4.90622],  
    [43.39732, 4.94040],  
    [43.39913, 4.94040],  
    [43.38323, 4.95772],  
    [43.39623, 4.97890]   
]
ajouter_polygone(carte, zone_nord, 'green')


carte.save("FRFOS.html")
