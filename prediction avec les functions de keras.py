import numpy as np
from tensorflow import keras
from math import exp
def predict_from_h5(inputs):
    # Architecture du modèle
    model = keras.Sequential([
        keras.layers.Dense(3, activation='relu', input_shape=(3,)),
        keras.layers.Dense(18, activation='relu'),
        keras.layers.Dense(36, activation='relu'),
        keras.layers.Dense(6, activation='relu'),
        keras.layers.Dense(2, activation='relu'),
        keras.layers.Dense(1)
    ])
    # Charger les poids à partir du fichier H5
    model.load_weights('wb.h5')
    # Faire des prédictions
    predictions = model.predict(inputs)
    return predictions
# Exemple d'utilisation
input_data = np.array([[200.0, 1.2, 800.0]])
prediction = exp(predict_from_h5(input_data))
print(prediction)
