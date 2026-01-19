import folium


def dms_to_dd(degrees, minutes, seconds, direction):
    dd = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        dd *= -1
    return dd


main_zone_coords_dms = [
    ((33, 43, 0, 'N'), (7, 33, 12, 'W')),
    ((33, 43, 0, 'N'), (7, 30, 0, 'W')),
    ((33, 40, 30, 'N'), (7, 30, 0, 'W')),
    ((33, 39, 0, 'N'), (7, 33, 12, 'W'))
]

west_zone_coords_dms = [
    ((33, 43, 0, 'N'), (7, 35, 0, 'W')),
    ((33, 43, 0, 'N'), (7, 39, 24, 'W')),
    ((33, 38, 54, 'N'), (7, 39, 24, 'W')),
    ((33, 38, 54, 'N'), (7, 37, 12, 'W')),
    ((33, 38, 0, 'N'), (7, 37, 12, 'W')),
    ((33, 38, 0, 'N'), (7, 35, 0, 'W'))
]


main_zone_coords = [
    [dms_to_dd(*lat), dms_to_dd(*lon)] for lat, lon in main_zone_coords_dms
]
west_zone_coords = [
    [dms_to_dd(*lat), dms_to_dd(*lon)] for lat, lon in west_zone_coords_dms
]


map_center = [dms_to_dd(33, 41, 0, 'N'), dms_to_dd(7, 34, 0, 'W')]
m = folium.Map(location=map_center, zoom_start=11)

folium.Polygon(
    locations=main_zone_coords,
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity=0.4,
    popup='Zone de mouillage principale'
).add_to(m)

folium.Polygon(
    locations=west_zone_coords,
    color='green',
    fill=True,
    fill_color='green',
    fill_opacity=0.4,
    popup='Zone de mouillage Ouest'
).add_to(m)


m.save('MACAS.html')
