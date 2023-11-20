import pickle
from googletrans import Translator
from modelo_analyzer.modelo import Modelo_analyzer_class

class ModeloClass:
    def __init__(self):
        # instancio el modelo 
        self.modelo = Modelo_analyzer_class()
        
    # tradusco todo a ingles
    def traductor(self, texto):
        translator = Translator()
        texto_traducido = translator.translate(str(texto), dest='en').text
        return texto_traducido
    

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
            # Itero a traves de los comentarios de varios videos
            for video in comentarios:
                video_comentarios = video['comentarios']
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
                        "comentario": comentario_texto,
                        "link_video": link_video,
                        "sentimiento": self.predictor(comentario_texto)
                    }
                    comentarios_con_sentimiento.append(comentario_con_sentimiento)
            return comentarios_con_sentimiento
        else:
            print("No se recibieron comentarios de la API")




