import requests
from bs4 import BeautifulSoup
from random import choice

URL = 'https://www.mundodasmensagens.com/frases-bom-dia/'

def get_sentence():
    soup = load_and_sanitize_page()
    sentences = extract_sentences(soup)
    chosen = choice(sentences)
    return chosen


def load_and_sanitize_page():
    content = requests.get(URL).text
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_sentences(soup):
    sentences_container = soup.find(id='list')
    sentences = [sentence_tag.get_text().strip() for sentence_tag in sentences_container.find_all('p')]
    return sentences
