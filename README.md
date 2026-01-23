#  Analyseur de Clusters Géospatiaux (DBSCAN)

Une application web interactive pour détecter automatiquement les zones de haute densité (clusters) à partir de données GPS, utilisant l'algorithme **DBSCAN**.

Idéal pour identifier des zones de mouillage, des ports, ou analyser le trafic maritime.

🔗 **Démo en ligne :** [Cliquez ici pour accéder à l'application](https://share.streamlit.io/farielbryan/clustering_vessel)

---

##  Fonctionnalités

* **Carte Interactive :** Visualisation des points et des polygones de clusters sur une carte Folium.
* **Paramètres Ajustables :** Modifiez le rayon (`EPS`) et le nombre minimum de points (`Min Samples`) en temps réel.
* **Sources de Données Flexibles :**
    * Utilisez les fichiers de ports pré-chargés (Marseille, Le Havre, etc.).
    * Importez vos propres fichiers `.csv` ou `.xlsx`.
* **Export :** Téléchargez les résultats du clustering (avec les identifiants de clusters) au format CSV.
* **Statistiques :** Visualisez instantanément le nombre de clusters détectés et le bruit (points isolés).

---

## 🛠️ Installation Locale

Si vous souhaitez faire tourner l'application sur votre propre machine :

  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ou si vous utilisez uv : `uv sync`)*

  **Lancer l'application :**
    ```bash
    streamlit run app.py
    ```

---

## 📋 Format des Données

L'application détecte automatiquement les colonnes. Pour que vos fichiers CSV fonctionnent, ils doivent contenir des colonnes nommées de façon explicite, par exemple :
* **Latitude :** `lat`, `latitude`, `y`
* **Longitude :** `lon`, `longitude`, `lng`, `x`

---

## 🏗️ Structure du Projet

```text
clustering_vessel/
├── app.py               # Application principale Streamlit
├── data/                # Dossier contenant les CSV des ports par défaut
├── requirements.txt     # Dépendances Python pour le déploiement
└── README.md            # Documentation
