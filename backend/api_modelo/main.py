from fastapi import FastAPI, Form
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pydantic import BaseModel
from consume_api_scrapping import API_scrapping_class
from modelo import ModeloClass
import os


# Crea una instancia de FastAPI
app = FastAPI()

# Configura el middleware de CORS
origins = ["*"]  # Cambia esto a los orígenes permitidos en tu caso.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URL del servidor Express
server_url = 'http://localhost:3000'  # Cambia esto si tu servidor se ejecuta en un host o puerto diferente

# Crea una instancia de la clase APIConsumer
api_consumer = API_scrapping_class(server_url)

class VideoUrls(BaseModel):
    video_urls: List[str]

# Ruta para analizar comentarios
@app.post("/analizar-comentarios/")
def analizar_comentarios(video_data: VideoUrls):
    video_urls = video_data.video_urls
    # Scrap comments from YouTube
    result = api_consumer.scrap_comments(video_urls)
    # Clase AnalizadorComentarios para analizar los comentarios
    modelo = ModeloClass()
    # Analizar los comentarios y devolverlos
    comentarios_con_sentimiento = modelo.analizar_comentarios(result)
    return comentarios_con_sentimiento


















# # Ejemplos de uso por tema de busqueda
# search_query = 'politica'  # Reemplaza con tu consulta de búsqueda
# result = api_consumer.search_and_scrap_videos(search_query)
# print('Esperando respuesta de la API')


# {
#   "video_urls": [
#     "https://www.youtube.com/watch?v=hBfZzCO-Y7s",
#     "https://www.youtube.com/watch?v=6T7vXd3hd-0"
#   ]
# }