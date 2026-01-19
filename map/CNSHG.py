import folium


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


def parse_dms(coord_str):
    parts = coord_str.split('°')
    deg = int(parts[0])
    rest = parts[1].split('′')
    min = int(rest[0])
    sec = float(rest[1].replace('″', '').replace('N', '').replace('E', '').strip())
    dir_char = coord_str[-1]
    return dms_to_decimal(deg, min, sec, dir_char)


carte = folium.Map(location=[31.2, 121.8], zoom_start=11)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)


south_channel_1 = [
    [parse_dms("31°00′43.4″N"), parse_dms("122°20′44.0″E")],
    [parse_dms("30°58′12.0″N"), parse_dms("122°18′00″E")],
    [parse_dms("30°58′00″N"), parse_dms("122°19′00″E")],  
    [parse_dms("31°00′30″N"), parse_dms("122°21′00″E")]   
]
ajouter_polygone(carte, south_channel_1, 'blue')

south_channel_2 = [
    [parse_dms("30°58′12″N"), parse_dms("122°20′44″E")],
    [parse_dms("31°01′16.5″N"), parse_dms("122°18′00″E")],
    [parse_dms("31°01′00″N"), parse_dms("122°19′30″E")],  
    [parse_dms("30°59′00″N"), parse_dms("122°21′00″E")]
]   
ajouter_polygone(carte, south_channel_2, 'lightblue')


jiangya_general = [
    [parse_dms("31°16′35.3″N"), parse_dms("121°45′12.5″E")],
    [parse_dms("31°17′32.3″N"), parse_dms("121°44′16.0″E")],
    [parse_dms("31°17′57.7″N"), parse_dms("121°44′41.9″E")],
    [parse_dms("31°16′59.3″N"), parse_dms("121°45′42.0″E")]
]
ajouter_polygone(carte, jiangya_general, 'green')


jiangya_danger = [
    [parse_dms("31°14′22.3″N"), parse_dms("121°47′30.9″E")],
    [parse_dms("31°15′40.3″N"), parse_dms("121°46′08.0″E")],
    [parse_dms("31°16′02.4″N"), parse_dms("121°46′37.8″E")],
    [parse_dms("31°14′59.3″N"), parse_dms("121°47′40.0″E")]
]
ajouter_polygone(carte, jiangya_danger, 'red')


hengsa_est = [
    [parse_dms("31°17′44.5″N"), parse_dms("121°47′55.3″E")],
    [parse_dms("31°18′26.3″N"), parse_dms("121°48′16.0″E")],  
    [parse_dms("31°17′50.5″N"), parse_dms("121°49′39.3″E")],
    [parse_dms("31°17′13.4″N"), parse_dms("121°49′20.0″E")]
]
ajouter_polygone(carte, hengsa_est, 'orange')




hengsa_ouest = [
    [parse_dms("31°18′19.4″N"), parse_dms("121°47′31.3″E")],
    [parse_dms("31°17′57.5″N"), parse_dms("121°47′20.4″E")],
    [parse_dms("31°18′32.3″N"), parse_dms("121°45′45.0″E")],
    [parse_dms("31°18′54.5″N"), parse_dms("121°45′55.0″E")]
]
ajouter_polygone(carte, hengsa_ouest, 'purple')


yangshan_danger = [
    [parse_dms("31°17′07.0″N"), parse_dms("121°49′38.2″E")],
    [parse_dms("31°17′25.8″N"), parse_dms("121°49′47.5″E")],
    [parse_dms("31°17′12.4″N"), parse_dms("121°50′38.7″E")],
    [parse_dms("31°17′22.9″N"), parse_dms("121°50′42.3″E")]
]
ajouter_polygone(carte, yangshan_danger, 'darkred')


baoshan_center = [31.4667, 121.4667]  
folium.Circle(
    location=baoshan_center,
    radius=2000, 
    color='gray',
    fill=True,
    fill_opacity=0.5,
    popup='Baoshan Maodi<br>Zone près de Baosteel / Shidongkou',
    tooltip='Baoshan Maodi'
).add_to(carte)

carte.save("CNSHG.html")
