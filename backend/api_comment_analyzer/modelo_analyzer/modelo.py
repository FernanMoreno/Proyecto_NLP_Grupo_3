import os
import pickle

class Modelo_analyzer_class:

    def analyzer(self, texto):
        # obtengo la ruta actual del directorio
        current_directory = os.path.dirname(os.path.realpath(__file__))
        # Combino la ruta del directorio actual con el nombre del archivo
        file_path = os.path.join(current_directory, 'model_pipeline.pkl')

        with open(file_path, 'rb') as archivo_pickle_cargado:
            modelo_cargado = pickle.load(archivo_pickle_cargado)

            prediccion = modelo_cargado.predict([texto])

        return prediccion

    