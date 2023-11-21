import requests

class Database:

    def insert(self, comentarios):
        database_url = 'http://localhost:5000/insertar-datos'
        comentarios_list = []
        for comentario in comentarios:
            data = {
                    "id": 1,
                    "comentario": comentario['comentario'],
                    "nombre_usuario": comentario['autor'],
                    "foto_usuario": comentario['img_autor'],
                    "link_usuario": comentario['link_autor'],
                    "url_video": comentario['link_video'],
                    "sentimiento": comentario['sentimiento']
            }

            comentarios_list.append(data)


        try:
            # Enviar solicitud POST al servidor
            response = requests.post(database_url, json=comentarios_list)

            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:
                print(f'Datos enviados correctamente para el comentario: {comentario["comentario"]}')
            else:
                print(f'Error al enviar datos para el comentario: {comentario["comentario"]}. Código de respuesta: {response.status_code}')
        except Exception as e:
            print(f'Error al enviar datos para el comentario: {comentario["comentario"]}. Error: {str(e)}')

        

        return 'Comentarios enviados a la api database'