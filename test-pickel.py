import pickle
from sklearn.metrics import accuracy_score

text = 'Fantastic talk! Was looking for a good explanation of Python bytecode, and this was absolutely perfect.'

# Cargar el modelo desde el archivo pickle
with open('modelo.pkl', 'rb') as archivo_pickle_cargado:
    modelo_cargado = pickle.load(archivo_pickle_cargado)

# Puedes usar el modelo cargado para realizar predicciones
y_pred_cargado = modelo_cargado.predict(text)

# Calcular la precisión del modelo cargado
precision_cargado = accuracy_score(y_test, y_pred_cargado)
print(f"Precisión del modelo cargado: {precision_cargado}")