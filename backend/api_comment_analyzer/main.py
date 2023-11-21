from fastapi import FastAPI, Form
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from consume_scrapping import API_scrapping_class
from modelo_analyzer.analizer import ModeloClass
from consume_database import Database

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
    comentario_data = api_consumer.scrap_comments(video_urls)
    modelo = ModeloClass()
    # Analizar los comentarios y devolverlos
    comentarios_con_sentimiento = modelo.analizar_comentarios(comentario_data)

    Database().insert(comentarios_con_sentimiento)

    # print(comentarios_con_sentimiento)

    return comentarios_con_sentimiento















