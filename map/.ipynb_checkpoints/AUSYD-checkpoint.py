import folium


def dm_to_decimal(coord_str, hemisphere):
    parts = coord_str.split('°')
    degrees = float(parts[0])
    minutes = float(parts[1].replace('′', '').replace('"', '').strip())
    decimal_degrees = degrees + minutes / 60.0
    if hemisphere in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees


carte = folium.Map(location=[-33.85, 151.25], zoom_start=13)

def ajouter_cercle(carte, centre, rayon_metres, couleur):
    folium.Circle(
        location=centre,
        radius=rayon_metres,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


bank1_centre = [dm_to_decimal("33°50.8085′", 'S'), dm_to_decimal("151°15.6484′", 'E')]
bank2_centre = [dm_to_decimal("33°50.7239′", 'S'), dm_to_decimal("151°15.5722′", 'E')]
triangle_centre = [dm_to_decimal("33°50.6548′", 'S'), dm_to_decimal("151°15.9246′", 'E')]
watsons_centre = [dm_to_decimal("33°50.6735′", 'S'), dm_to_decimal("151°16.4702′", 'E')]
point_piper_centre = [dm_to_decimal("33°51.6492′", 'S'), dm_to_decimal("151°14.8297′", 'E')]
athol_centre = [dm_to_decimal("33°51.1165′", 'S'), dm_to_decimal("151°14.2313′", 'E')]


ajouter_cercle(carte, bank1_centre, 300, 'blue')
ajouter_cercle(carte, bank2_centre, 450, 'red')
ajouter_cercle(carte, triangle_centre, 250, 'green')
ajouter_cercle(carte, watsons_centre, 310, 'orange')
ajouter_cercle(carte, point_piper_centre, 350, 'purple')
ajouter_cercle(carte, athol_centre, 500, 'darkblue')





carte.save("AUSYD.html")