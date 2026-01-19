import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint, Polygon

# --- Configuration globale ---
EPS = 0.003        # rayon en degrés pour DBSCAN 
MIN_SAMPLES = 15   # nb min de points pour former un cluster
FOLIUM_SAMPLE = 1000000
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


try:
    import folium
    FOLIUM_AVAILABLE = True
except Exception:
    FOLIUM_AVAILABLE = False

def read_table(path, sample_limit=45000, random_state=None):
    
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    # --- Lecture Excel --- 
    try:
        df = pd.read_excel(path, engine="openpyxl")
        print(f"{path} lu comme Excel ({len(df)} lignes)")
        return df

    except Exception:
        # --- Lecture CSV : détection du séparateur ---
        # lecture rapide des 5 premières lignes pour deviner le séparateur
        with open(path, 'r', encoding='utf-8') as f:
            first_lines = [next(f) for _ in range(5)]

        # compter le nombre de virgules et de points-virgules dans la première ligne
        n_comma = first_lines[0].count(',')
        n_semicolon = first_lines[0].count(';')
        sep = ',' if n_comma >= n_semicolon else ';'

        df = pd.read_csv(path, sep=sep)
        print(f"{path} CSV ({'virgule' if sep==',' else 'point-virgule'}) -> {len(df)} lignes ")

        # --- Échantillonnage si nécessaire ---
        if len(df) > sample_limit:
            original_len = len(df)
            # on échantillonne uniquement les lignes de données (header déjà exclu par pandas)
            df = df.sample(n=sample_limit, random_state=random_state).reset_index(drop=True)
            print(f"Le CSV contenait {original_len} lignes -> échantillonné à {sample_limit} lignes.")

        return df

def detect_lon_lat(df):

    cols_lower = {c.lower(): c for c in df.columns}
    lon_keys = ["longitude", "lon", "long", "lng"]
    lat_keys = ["latitude", "lat", "y"]
    lon_col = next((cols_lower[k] for k in lon_keys if k in cols_lower), None)
    lat_col = next((cols_lower[k] for k in lat_keys if k in cols_lower), None)
    if lon_col and lat_col:
        return lon_col, lat_col
    # fallback: prendre 2e et 3e colonne
    if df.shape[1] >= 3:
        return df.columns[1], df.columns[2]
    raise ValueError("Impossible de détecter les colonnes lon/lat")


def extract_coords(df, lon_col, lat_col):
    
    coords = df[[lon_col, lat_col]].copy()
    coords.columns = ["lon", "lat"]
    coords["lon"] = pd.to_numeric(coords["lon"].astype(str).str.replace(',', '.'), errors="coerce")
    coords["lat"] = pd.to_numeric(coords["lat"].astype(str).str.replace(',', '.'), errors="coerce")
    coords = coords.dropna().reset_index(drop=True)
    coords = coords[coords["lon"].between(-180, 180) & coords["lat"].between(-90, 90)].reset_index(drop=True)
    return coords


def cluster_and_hulls(coords, eps=EPS, min_samples=MIN_SAMPLES):
    """DBSCAN + calcul des convex hulls"""
    if len(coords) == 0:
        return coords, {}, 0, 0
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords[["lon", "lat"]].values)
    coords = coords.copy()
    coords["cluster"] = db.labels_
    polygons = {}
    for cid in sorted(set(db.labels_)):
        if cid == -1:
            continue
        pts = coords[coords["cluster"] == cid][["lon", "lat"]].values
        polygons[cid] = MultiPoint(pts).convex_hull if len(pts) > 1 else pts[0]
    n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
    n_noise = list(db.labels_).count(-1)
    return coords, polygons, n_clusters, n_noise


def save_png(coords, polygons, out_path):
  
    fig, ax = plt.subplots(figsize=(8, 8))
    if len(coords) > 0:
        ax.scatter(coords["lon"], coords["lat"], c=coords["cluster"], s=6, cmap="tab10")
    for cid, poly in polygons.items():
        if isinstance(poly, Polygon):
            x, y = poly.exterior.xy
            ax.plot(x, y, linewidth=2)
        else:
            ax.plot(poly[0], poly[1], marker='o', markersize=6)
    ax.set_title(f"DBSCAN (eps={EPS}, min_samples={MIN_SAMPLES})")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    plt.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"PNG sauvegardé: {out_path}")


def save_folium_map(coords, polygons, out_path, sample=FOLIUM_SAMPLE):

    if not FOLIUM_AVAILABLE:
        print("folium non installé — impossible de créer la carte HTML.")
        return
    if len(coords) == 0:
        print("Aucun point valide — carte non créée.")
        return
    center = [coords["lat"].mean(), coords["lon"].mean()]
    m = folium.Map(location=center, prefer_canvas= True, zoom_start=12)
    sample_df = coords.sample(sample, random_state=0) if len(coords) > sample else coords
    palette = ["red", "blue", "green", "purple", "orange", "darkred", "lightblue", "lightgreen", "cadetblue", "pink"]
    for _, row in sample_df.iterrows():
        cid = int(row["cluster"])
        color = "gray" if cid == -1 else palette[cid % len(palette)]
        folium.CircleMarker(location=[row["lat"], row["lon"]], radius=2, color=color, fill=True, fill_opacity=0.6).add_to(m)
    for cid, poly in polygons.items():
        if isinstance(poly, Polygon):
            folium.Polygon(locations=[(y, x) for x, y in poly.exterior.coords],
                           color=palette[cid % len(palette)], fill=True, fill_opacity=0.2).add_to(m)
    m.save(out_path)
    print(f"Carte HTML sauvegardée: {out_path}")


def process_one_csv(path, basename, eps=EPS, sample=MIN_SAMPLES ):
    
    print(f"\n=== Traitement: {path} ===")
    df = read_table(path)
    lon_col, lat_col = detect_lon_lat(df)
    print(f"Colonnes détectées -> lon: {lon_col}, lat: {lat_col}")
    coords = extract_coords(df, lon_col, lat_col)
    print(f"Points valides : {len(coords)}")
    coords, polygons, n_clusters, n_noise = cluster_and_hulls(coords)
    print(f"Clusters détectés: {n_clusters}  bruit: {n_noise}")
    png_out = os.path.join(OUTPUT_DIR, f"{basename}_clustering_{eps}_{sample}.png")
    html_out = os.path.join(OUTPUT_DIR, f"{basename}_map_{eps}_{sample}.html")
    save_png(coords, polygons, png_out)

    
    if FOLIUM_AVAILABLE:
        save_folium_map(coords, polygons, html_out)
    else:
        print("Pour générer la carte HTML, installe folium (uv add pp folium).")


def normalize_name(name):
    """retire .csv éventuel et espaces"""
    n = name.strip()
    if n.lower().endswith(".csv"):
        n = n[:-4]
    return n


def main():
    # liste les CSV présents
    csv_files = [f for f in os.listdir(".") if f.lower().endswith(".csv")]
    if not csv_files:
        print("Aucun fichier CSV trouvé dans le répertoire courant.")
        sys.exit(1)
    print("CSV disponibles :", csv_files)

    # demande à l'utilisateur quoi traiter

    user = input("Entrez le nom d'un CSV (sans .csv), plusieurs noms séparés par des virgules, ou 'all' pour tout traiter : ").strip()
    if user.lower() == "all":
        to_process = [os.path.splitext(f)[0] for f in csv_files]
    else:
        parts = [normalize_name(p) for p in user.split(",") if p.strip()]
        to_process = []
        for p in parts:
            matched = None
            # essayer match exact (basename)
            for f in csv_files:
                if os.path.splitext(f)[0].lower() == p.lower():
                    matched = f
                    break
            # si pas trouvé, essayer f contenant p (utile si l'utilisateur tape partie du nom)
            if matched is None:
                candidates = [f for f in csv_files if p.lower() in f.lower()]
                if len(candidates) == 1:
                    matched = candidates[0]
                elif len(candidates) > 1:
                    print(f"Plusieurs correspondances pour '{p}': {candidates}. Ignoré.")
                    matched = None
            if matched:
                to_process.append(os.path.splitext(matched)[0])
            else:
                print(f"Fichier pour '{p}' introuvable dans le répertoire courant. Ignoré.")

    if not to_process:
        print("Aucun fichier valide sélectionné. Sortie.")
        return

    # traiter chaque CSV demandé
    for basename in to_process:
        path = f"{basename}.csv"
        try:
            process_one_csv(path, basename)
        except Exception as e:
            print(f"Erreur lors du traitement de {path}: {e}")

    print("\nTraitement terminé. Résultats dans le dossier 'output/'.")


if __name__ == "__main__":
    main()
