# Modèle RNA pour la prédiction du module d'élasticité des métaux à différentes températures

Ce dépôt contient un modèle de réseau de neurones artificiels (RNA) conçu pour prédire le module d'élasticité des métaux à différentes températures. Le modèle est entraîné à l'aide de données obtenues par simulation Abaqus, qui sont stockées dans le fichier data.csv.

## Fichiers inclus

- `data.csv`: Un ensemble de données contenant les propriétés des matériaux et le module d'élasticité (E) obtenu par simulation Abaqus à différentes températures. Les colonnes du fichier comprennent les attributs suivants : E [GPa], υ, Conductivité [W/m-K], CTE [µm/m-°C], Température [°C], E(T) [GPa].
- `notebook.ipynb`: Un notebook Jupyter qui présente le processus de chargement des données, la visualisation, le traitement des données, la construction du modèle, l'évaluation et la validation.
- `weights.h5`: Un fichier contenant les poids et les biais du modèle entraîné au format H5.
- `weights.json`: Un fichier contenant les poids et les biais du modèle entraîné au format JSON.
- `prediction_avec_keras.py`: Un script Python qui utilise la bibliothèque TensorFlow-Keras pour charger le modèle à partir du fichier weights.h5 et effectuer des prédictions sur de nouvelles données.
- `prediction_avec_json.py`: Un script Python qui utilise uniquement la bibliothèque NumPy pour charger les poids et les biais à partir du fichier weights.json et effectuer des prédictions sur de nouvelles données.

## Prérequis

Assurez-vous d'avoir les dépendances suivantes installées :
- tensorflow
- scikit-learn
- matplotlib
- numpy
- pandas
- seaborn
- tensorflow-docs

Vous pouvez les installer en exécutant la commande suivante :
  pip install -r requirements.txt

## Utilisation

- Exécutez le notebook `notebook.ipynb` pour suivre le processus complet, y compris le chargement des données, la construction du modèle, l'entraînement, l'évaluation et la visualisation des résultats.
- Utilisez le script `prediction_avec_keras.py` pour effectuer des prédictions en utilisant le modèle et les poids enregistrés au format H5.
- Utilisez le script `prediction_avec_json.py` pour effectuer des prédictions en utilisant uniquement la bibliothèque NumPy et les poids enregistrés au format JSON.

## Contribution

Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue pour signaler des problèmes ou à soumettre une demande de fusion pour proposer des améliorations.

## Auteur

Ce projet a été développé par Syphax Zennouche. Vous pouvez me contacter par e-mail à syphaxszi@gmail.com.
