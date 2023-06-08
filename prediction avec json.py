from math import exp
import numpy as np
import json

# Charger les poids et les biais à partir du fichier JSON
with open('WB.json') as fichier:
    donnees = json.load(fichier)
poids = donnees['Weights']
biais = donnees['Biases']

# Définir l'architecture du modèle
def relu(x):
    return np.maximum(0, x)

# Définir la fonction de prédiction
def predict(inputs):
    # Effectuer la propagation avant
    sortie_couche = inputs
    for i in range(len(poids)):
        sortie_couche = np.dot(sortie_couche, poids[str(i+1)]) + biais[str(i+1)]
        sortie_couche = relu(sortie_couche)
    
    # Retourner la prédiction finale
    return sortie_couche

# Définir les données d'entrée pour la prédiction
donnees_entree = np.array([[200.0, 1.2, 800.0]])

# Effectuer la prédiction
sortie = exp(predict(donnees_entree))
print(sortie)
