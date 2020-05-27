from functions.get_sentence import get_sentence
from functions.get_and_download_image import get_and_download_image
from functions.convert_image import convert_image

def main():
    sentence = get_sentence()
    get_and_download_image()
    convert_image(sentence)

main()
