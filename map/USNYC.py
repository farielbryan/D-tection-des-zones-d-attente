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
    sec = float(rest[1].replace('″', '').strip())
    return deg + min/60 + sec/3600


carte = folium.Map(location=[40.65, -74.05], zoom_start=11)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.6,
    ).add_to(carte)




anchorage_19e = [
    [parse_dms("40°49′42.6″"), -parse_dms("73°57′14.7″")],  
    [parse_dms("40°49′45.9″"), -parse_dms("73°57′22.0″")],  
    [parse_dms("40°49′52.0″"), -parse_dms("73°57′22.0″")],  
    [parse_dms("40°50′08.3″"), -parse_dms("73°57′10.8″")],  
    [parse_dms("40°50′55.4″"), -parse_dms("73°56′59.7″")],  
    [parse_dms("40°51′02.5″"), -parse_dms("73°56′57.4″")], 
    [parse_dms("40°51′00.8″"), -parse_dms("73°56′49.4″")]  
]
ajouter_polygone(carte, anchorage_19e, 'blue')


anchorage_19w = [
    [parse_dms("40°46′56.3″"), -parse_dms("73°59′42.2″")], 
    [parse_dms("40°47′36.9″"), -parse_dms("73°59′11.7″")],
    [parse_dms("40°47′49.6″"), -parse_dms("73°59′11.7″")], 
    [parse_dms("40°48′25.0″"), -parse_dms("73°59′11.7″")], 
    [parse_dms("40°48′51.2″"), -parse_dms("73°59′11.7″")],
    [parse_dms("40°48′56.7″"), -parse_dms("73°59′11.7″")], 
    [parse_dms("40°48′51.5″"), -parse_dms("73°59′38.3″")],
    [parse_dms("40°48′43.4″"), -parse_dms("73°59′57.4″")],
    [parse_dms("40°47′02.7″"), -parse_dms("73°59′57.4″")] 
]
ajouter_polygone(carte, anchorage_19w, 'red')


anchorage_20e = [
    [parse_dms("40°40′38.2″"), -parse_dms("74°02′59.6″")],  
    [parse_dms("40°40′39.4″"), -parse_dms("74°02′40.9″")],  
    [parse_dms("40°40′09.2″"), -parse_dms("74°03′00.7″")],  
    [parse_dms("40°40′24.4″"), -parse_dms("74°03′24.6″")]  
]
ajouter_polygone(carte, anchorage_20e, 'green')


anchorage_25 = [
    [parse_dms("40°35′58.2″"), -parse_dms("74°02′18.4″")],  
    [parse_dms("40°35′23.9″"), -parse_dms("74°02′04.8″")],  
    [parse_dms("40°35′00.0″"), -parse_dms("74°02′30.0″")],  
    [parse_dms("40°35′30.0″"), -parse_dms("74°03′00.0″")]  
]
ajouter_polygone(carte, anchorage_25, 'purple')


anchorage_26 = [
    [parse_dms("40°30′06.7″"), -parse_dms("74°10′04.9″")],  
    [parse_dms("40°28′59.4″"), -parse_dms("74°05′00.0″")],  
    [parse_dms("40°28′44.9″"), -parse_dms("74°05′00.0″")],  
    [parse_dms("40°29′05.0″"), -parse_dms("74°07′30.6″")],  
    [parse_dms("40°29′17.5″"), -parse_dms("74°10′16.5″")]   
]
ajouter_polygone(carte, anchorage_26, 'orange')


anchorage_27 = [
    [parse_dms("40°28′49.3″"), -parse_dms("74°00′12.1″")],  
    [parse_dms("40°23′45.4″"), -parse_dms("73°58′32.1″")],  
    [parse_dms("40°23′30.0″"), -parse_dms("73°59′00.0″")],
    [parse_dms("40°28′30.0″"), -parse_dms("74°01′00.0″")]   
]
ajouter_polygone(carte, anchorage_27, 'darkblue')


anchorage_28 = [
    [parse_dms("40°30′02.3″"), -parse_dms("74°08′52.7″")],  
    [parse_dms("40°30′21.5″"), -parse_dms("74°08′46.2″")],  
    [parse_dms("40°29′45.0″"), -parse_dms("74°09′15.0″")],  
    [parse_dms("40°30′15.0″"), -parse_dms("74°08′15.0″")]   
]
ajouter_polygone(carte, anchorage_28, 'pink')


anchorage_44 = [
    [parse_dms("40°30′07″"), -parse_dms("74°15′30″")],  
    [parse_dms("40°30′01″"), -parse_dms("74°15′30″")],  
    [parse_dms("40°29′27″"), -parse_dms("74°15′06″")],  
    [parse_dms("40°29′24″"), -parse_dms("74°15′01″")],  
    [parse_dms("40°29′15″"), -parse_dms("74°14′55″")],  
    [parse_dms("40°29′14″"), -parse_dms("74°15′25″")],  
    [parse_dms("40°29′48″"), -parse_dms("74°15′48″")]   
]
ajouter_polygone(carte, anchorage_44, 'gray')


carte.save("USNYC.html")

