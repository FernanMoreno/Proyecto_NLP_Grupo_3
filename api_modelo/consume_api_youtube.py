import requests

class APIConsumer:
    def __init__(self, server_url):
        self.server_url = server_url


    def scrap_comments(self, urls):
        endpoint = f"{self.server_url}/api/scrap-comments"
        data = {'urls': urls}
        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            comentarios_data = response.json()
            # Aquí puedes trabajar con los datos de comentarios recibidos
            return comentarios_data
        else:
            print(f"Error: {response.status_code}")
            return None


    def search_and_scrap_videos(self, query):
        endpoint = f"{self.server_url}/api/search-and-scrap-videos"
        data = {'query': query}
        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            comentarios_data = response.json()
            # Aquí puedes trabajar con los datos de comentarios recibidos
            return comentarios_data
        else:
            print(f"Error: {response.status_code}")
            return None


