import folium


def convert_coord(coord_str):
    parts = coord_str.replace('N ', '').replace('E ', '').split('-')
    deg = int(parts[0])
    min = int(parts[1])
    sec = float(parts[2])
    return deg + min/60 + sec/3600


carte = folium.Map(location=[35.03, 129.04], zoom_start=12)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)


zone_n1 = [
    [convert_coord("N 35-04-35.1"), convert_coord("E 129-02-00.0")],  
    [convert_coord("N 35-04-35.1"), convert_coord("E 129-02-21.5")],  
    [convert_coord("N 35-04-01.7"), convert_coord("E 129-03-11.1")],  
    [convert_coord("N 35-04-01.7"), convert_coord("E 129-02-03.9")]   
]
ajouter_polygone(carte, zone_n1, 'blue')


zone_n2 = [
    [convert_coord("N 35-04-35.2"), convert_coord("E 129-01-35.5")],  
    [convert_coord("N 35-04-35.2"), convert_coord("E 129-01-53.4")],  
    [convert_coord("N 35-03-10.8"), convert_coord("E 129-01-52.4")],  
    [convert_coord("N 35-03-10.6"), convert_coord("E 129-01-02.2")],  
    [convert_coord("N 35-03-41.3"), convert_coord("E 129-01-29.7")],  
    [convert_coord("N 35-04-26.9"), convert_coord("E 129-01-29.7")]   
]
ajouter_polygone(carte, zone_n2, 'red')


zone_n3 = [
    [convert_coord("N 35-04-01.7"), convert_coord("E 129-02-03.9")],  
    [convert_coord("N 35-04-01.7"), convert_coord("E 129-03-11.1")],  
    [convert_coord("N 35-02-55.9"), convert_coord("E 129-04-48.2")],  
    [convert_coord("N 35-02-39.5"), convert_coord("E 129-02-13.5")]   
]
ajouter_polygone(carte, zone_n3, 'green')


zone_n4 = [
    [convert_coord("N 35-02-39.5"), convert_coord("E 129-02-13.5")], 
    [convert_coord("N 35-02-55.9"), convert_coord("E 129-04-48.2")],  
    [convert_coord("N 35-02-09.6"), convert_coord("E 129-05-23.7")],  
    [convert_coord("N 35-01-36.7"), convert_coord("E 129-02-38.1")]   
]
ajouter_polygone(carte, zone_n4, 'purple')


zone_n5 = [
    [convert_coord("N 35-01-36.7"), convert_coord("E 129-02-38.1")],  
    [convert_coord("N 35-02-09.6"), convert_coord("E 129-05-23.7")],  
    [convert_coord("N 35-02-02.5"), convert_coord("E 129-05-32.3")],  
    [convert_coord("N 35-00-11.3"), convert_coord("E 129-04-48.1")],  
    [convert_coord("N 35-00-11.5"), convert_coord("E 129-02-38.1")]   #
]
ajouter_polygone(carte, zone_n5, 'orange')


points_importants = {
    'N1-P1': [convert_coord("N 35-04-35.1"), convert_coord("E 129-02-00.0")],
    'N2-P1': [convert_coord("N 35-04-35.2"), convert_coord("E 129-01-35.5")],
    'N3-P4': [convert_coord("N 35-02-39.5"), convert_coord("E 129-02-13.5")],
    'N4-P4': [convert_coord("N 35-01-36.7"), convert_coord("E 129-02-38.1")],
    'N5-P5': [convert_coord("N 35-00-11.5"), convert_coord("E 129-02-38.1")]
}

<<<<<<< HEAD
=======



>>>>>>> 90c139c4e5474c9e0810867539cb2523a6b259dc
carte.save("KRPUS.html")

