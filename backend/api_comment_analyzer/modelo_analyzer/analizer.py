<<<<<<< HEAD
from asyncio import exceptions
import os
import pickle
import re
from googletrans import Translator
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from modelo_analyzer.consume_modelo import ClasificadorTexto
# from modelo_analyzer.a import predecir
=======
import pickle
import re
from googletrans import Translator
from modelo_analyzer.modelo import Modelo_analyzer_class
>>>>>>> dad841917168f1cb9fa502b8e511c4ded2c46e64

class ModeloClass:
    def __init__(self):
        # instancio el modelo 
<<<<<<< HEAD
        self.modelo = ClasificadorTexto()
    

    def traductor(self, comentario):
        translator = Translator()

        # Verificar si el comentario es una cadena
        if not isinstance(comentario, str):
            return comentario

        # Eliminar caracteres especiales y convertir a minúsculas
        comentario = re.sub(r'[^a-zA-Z0-9\s]', '', comentario.lower())

        try:
            # Verificar si el comentario no está vacío
            if not comentario:
                return comentario

            # Intentar realizar la traducción
            traduccion = translator.translate(comentario, dest='en')

            # Verificar si la traducción fue exitosa
            if traduccion is not None and hasattr(traduccion, 'text'):
                return traduccion.text
            else:
                # Si no se pudo traducir, devolver el comentario original
                return comentario
        except Exception as e:
            # Manejar la excepción imprimiendo un mensaje
            print(f"Error al traducir: {e}")
            return comentario

        




    def predictor(self, comentario):

        # Analizar el sentimiento del comentario
        prediccion = self.modelo.predecir(comentario)
    
        # obtengo la respuesta de la prediccion en 0 y 1
        if prediccion == '0':
            prediccion = "Positivo"
        else:
=======
        self.modelo = Modelo_analyzer_class()
        
    # tradusco todo a ingles

    def traductor(self, comentario):
       translator = Translator()
       traduccion = translator.translate(comentario, dest='en')
       return traduccion.text



    # def traductor(self, comments_list):
    #     translator = Translator()

        # # Check if the separator is present in any of the comments
        # separator = ' &% ' 
        # for comment in comments_list:
        #     if separator in comment['comentario']:
        #         raise ValueError(f"El separador '{separator}' está presente en uno de los comentarios originales.")

        # # Limpiar comentarios de caracteres especiales
        # cleaned_comments = [re.sub(r'[\'"´`¨:,.&%$·"!?¿*+^[\]()_ªº¡¿-]', '', comment['comentario']) for comment in comments_list]

        # # Join comments with the separator
        # joined_comments = separator.join(cleaned_comments)

        # try:
        #     # Translate comments
        #     translation = translator.translate(joined_comments, dest='en')
        #     print(translation)

        #     # Check if the translation was successful
        #     if translation.text is not None:
        #         # Split the translated string back into individual comments
        #         translated_comments = translation.text.split(separator)
        #     else:
        #         print("¡Alerta! La traducción no fue exitosa.")
        #         translated_comments = []
        # except Exception as e:
        #     print(f"¡Error durante la traducción! {str(e)}")
        #     translated_comments = []

        # for i, comment in enumerate(comments_list):
        #     if i < len(translated_comments):
        #         comment['comentario'] = translated_comments[i].strip()
        #     else:
        #         # Manejar el caso donde i está fuera de los límites
        #         print(f"¡Alerta! El comentario '{comment['comentario']}' no se logró traducir.")
       
        # return comments_list

    def predictor(self, comentario):
        # Analizar el sentimiento del comentario
        prediccion = self.modelo.analyzer(comentario)
        # obtengo la respuesta de la prediccion en 0 y 1
        if prediccion == 0:
            prediccion = "Positivo"
        elif prediccion == 1:
>>>>>>> dad841917168f1cb9fa502b8e511c4ded2c46e64
            prediccion = "Negativo"
        return prediccion

    def analizar_comentarios(self, comentarios_data):
<<<<<<< HEAD

=======
>>>>>>> dad841917168f1cb9fa502b8e511c4ded2c46e64
        if comentarios_data:
            comentarios = comentarios_data
            # Lista para almacenar comentarios y sus análisis de sentimiento
            comentarios_con_sentimiento = []

            # Itero a través de los comentarios de varios videos
            for video in comentarios:
                video_comentarios = video['comentario_data']
                # video_comentarios = self.traductor(video_comentarios)

                for comentario in video_comentarios:
                    img_autor = comentario['img_autor']
                    link_autor = comentario['link_autor']
                    autor = comentario["autor"]
<<<<<<< HEAD
                    comentario_texto = comentario["comentario"]
                    # comentario_texto = self.traductor(comentario["comentario"])
=======
                    comentario_texto = self.traductor(comentario["comentario"])
>>>>>>> dad841917168f1cb9fa502b8e511c4ded2c46e64
                    link_video = comentario['link_video']
                    # Crear un diccionario que almacena el comentario y su análisis de sentimiento
                    comentario_con_sentimiento = {
                        "img_autor": img_autor,
                        "link_autor": link_autor,
                        "autor": autor,
                        "comentario":  comentario_texto,
                        "link_video": link_video,
                        "sentimiento": self.predictor(comentario_texto)
                    }
                    comentarios_con_sentimiento.append(comentario_con_sentimiento)
            return comentarios_con_sentimiento
        else:
            print("No se recibieron comentarios de la API")
