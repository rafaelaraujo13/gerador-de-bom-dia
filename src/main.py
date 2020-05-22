from functions.get_sentence import get_sentence
from functions.get_and_download_image import get_and_download_image

def main():
    sentence = get_sentence()
    get_and_download_image(sentence)

main()
