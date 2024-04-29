import streamlit as st
import numpy as np

# Générer des données aléatoires pour l'exemple
np.random.seed(0)
X_train = np.random.rand(100, 1) * 10
y_train = 3 * X_train ** 2 - 5 * X_train + 2 + np.random.randn(100, 1) * 5

# Entraîner le modèle
coefficients = np.polyfit(X_train.flatten(), y_train.flatten(), 2)

# Définir la page Streamlit
st.title('Déploiement de modèle avec Streamlit')

# Widget pour saisir une valeur d'entrée
input_value = st.slider('Valeur d\'entrée', min_value=0.0, max_value=10.0, step=0.1)

# Prédiction avec le modèle entraîné
prediction = coefficients[0] * input_value ** 2 + coefficients[1] * input_value + coefficients[2]

# Affichage de la prédiction
st.write(f'Prédiction pour la valeur d\'entrée {input_value}: {prediction}')
