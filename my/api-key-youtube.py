from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# mi credencial de api-key-youtube
API_KEY = 'AIzaSyCqYbUz1RgapEy3QG3ABHqUphIssNy0X4g'

# objeto de servicio de la API
youtube = build('youtube', 'v3', developerKey=API_KEY)

# ID del video del cual deseas obtener los comentarios
video_id = 'zVJKcbjE52w'

try:
    # hago una solicitud a la API para obtener los comentarios del video
    comments_response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    # itero los comentarios
    for comment in comments_response['items']:
        snippet = comment['snippet']['topLevelComment']['snippet']
        author = snippet['authorDisplayName']
        text = snippet['textDisplay']
        print(f'Usuario: {author}\nComentario: {text}\n')

except HttpError as e:
    print(f'Error al obtener los comentarios: {e}')















# import requests
# import xml.etree.ElementTree as ET

# url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCAJN1nBM1_ulpv-mWEVdNWw'

# try:
#     request = requests.get(url, headers={'User-Agent': 'Chrome/50.0.2661.94'})
#     request.raise_for_status()  # Verifica si la solicitud fue exitosa
#     contenido = request.content
#     root = ET.fromstring(contenido.decode('utf-8'))  # Especifica la codificación
#     print(contenido)
#     # Realiza el análisis del XML y otras operaciones aquí
# except requests.exceptions.RequestException as e:
#     print(f"Error al hacer la solicitud: {e}")
# except ET.ParseError as e:
#     print(f"Error al analizar el XML: {e}")




# import re
# from colorama import Fore
# import requests


# url = "https://google.com"
# resultado = requests.get('https://www.youtube.com/watch?v=98LadkdwJOQ')
# content = resultado.text
# print(content)



# from bs4 import BeautifulSoup

# # Supongamos que tienes el HTML del comentario
# html = '''
# <yt-formatted-string id="content-text" slot="content" split-lines="" user-input="" class="style-scope ytd-comment-renderer">
#     <span dir="auto" class="style-scope yt-formatted-string">Me gustan mucho tus videos y aprendo mucho como lo explicas paso a paso, me gusta mucho python por que en pocas lineas se pueden hacer muchas cosas y con tu permiso me gustaria aportar una expresion regular para este caso</span>
#     <span dir="auto" class="style-scope yt-formatted-string"></span>
#     <span dir="auto" class="style-scope yt-formatted-string">print(list(set([x.group(2) for x in re.finditer( r'(href="\/entry\/)(.*)(?=,)', content)])))</span>
#     <span dir="auto" class="style-scope yt-formatted-string"></span>
#     <span dir="auto" class="style-scope yt-formatted-string">Gracias.</span>
#     <span dir="auto" class="style-scope yt-formatted-string"></span>
#     <span dir="auto" class="style-scope yt-formatted-string">Un saludo.</span>
# </yt-formatted-string>
# '''

# # Parsea el HTML con BeautifulSoup
# soup = BeautifulSoup(content, 'html.parser')

# # Encuentra el elemento <yt-formatted-string> por su id
# comment_element = soup.find('yt-formatted-string', id='content-text')

# # Extrae el texto del elemento
# comment_text = comment_element.get_text(strip=True)

# # Imprime el texto del comentario
# print(comment_text)