import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint, Polygon
import folium
from streamlit_folium import st_folium
import os
import io

# --- Configuration de la page ---
st.set_page_config(page_title="Geospatial Clustering", layout="wide")
st.title("📍 Analyse de Clusters Géospatiaux (DBSCAN)")

# --- Sidebar : Paramètres ---
st.sidebar.header("Configuration")
eps = st.sidebar.slider("Rayon (EPS) en degrés", 0.001, 0.100, 0.005, format="%.3f")
min_samples = st.sidebar.number_input("Min points par cluster", min_value=1, value=20)
sample_limit = st.sidebar.slider("Limite d'échantillonnage", 1000, 100000, 45000)

# --- Fonctions Utilitaires ---
def detect_lon_lat(df):
    cols_lower = {c.lower(): c for c in df.columns}
    lon_keys = ["longitude", "lon", "long", "lng"]
    lat_keys = ["latitude", "lat", "y"]
    lon_col = next((cols_lower[k] for k in lon_keys if k in cols_lower), None)
    lat_col = next((cols_lower[k] for k in lat_keys if k in cols_lower), None)
    if lon_col and lat_col: return lon_col, lat_col
    if df.shape[1] >= 3: return df.columns[1], df.columns[2]
    return None, None

def extract_coords(df, lon_col, lat_col):
    coords = df[[lon_col, lat_col]].copy()
    coords.columns = ["lon", "lat"]
    for col in ["lon", "lat"]:
        coords[col] = pd.to_numeric(coords[col].astype(str).str.replace(',', '.'), errors="coerce")
    coords = coords.dropna().reset_index(drop=True)
    coords = coords[coords["lon"].between(-180, 180) & coords["lat"].between(-90, 90)]
    return coords

def cluster_and_hulls(coords, eps, min_samples):
    if len(coords) == 0: return coords, {}, 0, 0
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords[["lon", "lat"]].values)
    coords = coords.copy()
    coords["cluster"] = db.labels_
    polygons = {}
    for cid in sorted(set(db.labels_)):
        if cid == -1: continue
        pts = coords[coords["cluster"] == cid][["lon", "lat"]].values
        polygons[cid] = MultiPoint(pts).convex_hull if len(pts) > 1 else pts[0]
    n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
    n_noise = list(db.labels_).count(-1)
    return coords, polygons, n_clusters, n_noise

# --- Gestion des Données ---
DATA_DIR = "data"
available_ports = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")] if os.path.exists(DATA_DIR) else []

st.sidebar.header("Source des données")
source_mode = st.sidebar.radio("Choisir la source :", ["Fichier pré-chargé", "Uploader un fichier"])

df = None
file_name = "resultats"

try:
    if source_mode == "Fichier pré-chargé":
        if available_ports:
            selected_file = st.sidebar.selectbox("Sélectionnez un port :", available_ports)
            file_path = os.path.join(DATA_DIR, selected_file)
            # Lecture du CSV local
            with open(file_path, 'r', encoding='utf-8') as f:
                first_line = f.readline()
                sep = ',' if first_line.count(',') >= first_line.count(';') else ';'
            df = pd.read_csv(file_path, sep=sep)
            file_name = os.path.splitext(selected_file)[0]
        else:
            st.warning("Aucun fichier CSV trouvé dans le dossier 'data/'.")

    else:
        uploaded_file = st.file_uploader("Glissez votre fichier ici", type=["csv", "xlsx"])
        if uploaded_file:
            file_name = os.path.splitext(uploaded_file.name)[0]
            if uploaded_file.name.endswith('.csv'):
                content = uploaded_file.getvalue().decode("utf-8").splitlines()
                sep = ',' if content[0].count(',') >= content[0].count(';') else ';'
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, sep=sep)
            else:
                df = pd.read_excel(uploaded_file)

    # --- Traitement ---
    if df is not None:
        if len(df) > sample_limit:
            df = df.sample(n=sample_limit, random_state=42)
            st.info(f"Données échantillonnées à {sample_limit} lignes pour la performance.")

        lon_col, lat_col = detect_lon_lat(df)
        
        if lon_col and lat_col:
            coords = extract_coords(df, lon_col, lat_col)
            
            with st.spinner('Calcul des clusters en cours...'):
                coords, polygons, n_clusters, n_noise = cluster_and_hulls(coords, eps, min_samples)

            # --- Résultats ---
            col1, col2, col3 = st.columns(3)
            col1.metric("Points total", len(coords))
            col2.metric("Clusters", n_clusters)
            col3.metric("Bruit", n_noise)

            # --- Carte ---
            center = [coords["lat"].mean(), coords["lon"].mean()]
            m = folium.Map(location=center, zoom_start=11, tiles="Cartodb Positron")
            
            # Points (échantillon pour la carte pour ne pas lagger)
            viz_sample = coords.sample(min(len(coords), 2000))
            for _, row in viz_sample.iterrows():
                c = "red" if row['cluster'] == -1 else "blue"
                folium.CircleMarker([row['lat'], row['lon']], radius=1, color=c, fill=True).add_to(m)

            # Polygones
            for cid, poly in polygons.items():
                if isinstance(poly, Polygon):
                    locations = [(y, x) for x, y in poly.exterior.coords]
                    folium.Polygon(locations, color="orange", fill=True, fill_opacity=0.4).add_to(m)

            st_folium(m, width=None, height=500)

            # --- Export CSV ---
            csv = coords.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Télécharger les résultats (CSV)",
                data=csv,
                file_name=f"{file_name}_clustered.csv",
                mime="text/csv",
            )
        else:
            st.error("Impossible de détecter les colonnes longitude/latitude.")

except Exception as e:
    st.error(f"Une erreur est survenue : {e}")
