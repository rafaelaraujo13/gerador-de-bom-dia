import json
import os
import requests
from googleapiclient.discovery import build
from random import choice

dir = os.path.dirname(__file__)
queries = ['flower', 'rose', 'nature', 'sunrise', 'blue sky', 'heart', 'coffee', 'landscape', 'sea']


def get_and_download_image():
    api_key, search_engine_id = get_credentials()
    service = build('customsearch', 'v1', developerKey=api_key)
    image_links = get_image_links(service, search_engine_id)
    download_image(image_links)


def get_credentials():
    with open(os.path.join(dir, '../', 'credentials', 'google.json')) as file:
        file_content = json.loads(file.read())

        return file_content['api_key'], file_content['search_engine_id']


def get_image_links(service, search_engine_id):
    results = service.cse().list(cx=search_engine_id, q=choice(queries), searchType="image").execute()
    return [image['link'] for image in results['items']]

def download_image(image_links):
    selected_link = choice(image_links)
    downloaded = False

    while not downloaded:
        try:
            image = requests.get(selected_link)
            with open(os.path.join(dir, '../', 'images', 'original.png'), 'wb') as file:
                file.write(image.content)
                downloaded = True

        except:
            selected_link = choice(image_links)
