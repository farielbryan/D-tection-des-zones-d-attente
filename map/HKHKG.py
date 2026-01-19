import folium


carte = folium.Map(location=[22.3, 114.1], zoom_start=11)

def ajouter_polygone(carte, points, couleur):
    folium.Polygon(
        locations=points,
        color=couleur,
        fill=True,
        fill_opacity=0.4,
    ).add_to(carte)


eastern_quarantine = [
    [22.305833, 114.2],     
    [22.301111, 114.2],      
    [22.301111, 114.205278], 
    [22.305833, 114.208056]  
]
ajouter_polygone(carte, eastern_quarantine, 'blue')


western_quarantine = [
    [22.3225, 114.104583],   
    [22.310278, 114.105833], 
    [22.305833, 114.100833], 
    [22.318611, 114.095]     
]
ajouter_polygone(carte, western_quarantine, 'red')


pun_shan = [
    [22.323333, 114.056667], 
    [22.323333, 114.066667], 
    [22.3, 114.056667],      
    [22.3, 114.075]          
]
ajouter_polygone(carte, pun_shan, 'green')


western_dg = [
    [22.315278, 114.123333], 
    [22.316944, 114.1225],   
    [22.316667, 114.113333], 
    [22.3225, 114.104722],   
    [22.313056, 114.105556], 
    [22.306944, 114.1175]    
]
ajouter_polygone(carte, western_dg, 'orange')


rocky_harbour = [
    [22.346667, 114.335833], 
    [22.346667, 114.340833], 
    [22.341944, 114.340833], 
    [22.341944, 114.335833]  
]
ajouter_polygone(carte, rocky_harbour, 'purple')


bay_dg = [
    [22.2925, 114.25],      
    [22.2925, 114.255833],  
    [22.286667, 114.255833], 
    [22.286667, 114.25]     
]
ajouter_polygone(carte, bay_dg, 'pink')


yau_ma_tei = [
    [22.319583, 114.154167], 
    [22.319861, 114.145278], 
    [22.326667, 114.143333], 
    [22.323472, 114.15]      
]
ajouter_polygone(carte, yau_ma_tei, 'darkblue')


carte.save("HKHKG.html")