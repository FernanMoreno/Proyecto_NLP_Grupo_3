import pickle
import re
from googletrans import Translator
from modelo_analyzer.modelo import Modelo_analyzer_class

class ModeloClass:
    def __init__(self):
        # instancio el modelo 
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
            prediccion = "Negativo"
        return prediccion

    def analizar_comentarios(self, comentarios_data):
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
                    comentario_texto = self.traductor(comentario["comentario"])
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
