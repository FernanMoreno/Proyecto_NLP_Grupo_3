import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class AnalizadorComentarios:
    def __init__(self):
        # Descargar los recursos necesarios (solo la primera vez)
        nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()

    def analizar_comentarios(self, comentarios_data):
        if comentarios_data:
            comentarios = comentarios_data

            # Lista para almacenar comentarios y sus análisis de sentimiento
            comentarios_con_sentimiento = []

            # Iterar a través de los comentarios de varios videos
            for video in comentarios:
                video_comentarios = video['comentarios']
                
                for comentario in video_comentarios:
                    autor = comentario["autor"]
                    comentario_texto = comentario["comentario"]
                    
                    # Analizar el sentimiento del comentario
                    sentiment = self.analyzer.polarity_scores(comentario_texto)

                    if sentiment['compound'] >= 0.05:
                        sentimiento = "Positivo"
                    elif sentiment['compound'] <= -0.05:
                        sentimiento = "Negativo"
                    else:
                        sentimiento = "Neutral"

                    # Crear un diccionario que almacena el comentario y su análisis de sentimiento
                    comentario_con_sentimiento = {
                        "autor": autor,
                        "comentario": comentario_texto,
                        "sentimiento": sentimiento
                    }

                    comentarios_con_sentimiento.append(comentario_con_sentimiento)

            return comentarios_con_sentimiento

        else:
            print("No se recibieron comentarios de la API")