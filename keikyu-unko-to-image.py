# coding=utf-8

import requests
from os import path
from PIL import Image, ImageFont, ImageDraw

FONT_PATH = path.dirname(path.abspath(__file__)) + '/mplus-2p-heavy.ttf'
IMAGE_FILE = path.dirname(path.abspath(__file__)) + "/image.png"
FONT = ImageFont.truetype(FONT_PATH, 24, encoding='unic')
URL = 'https://unkou.keikyu.co.jp/'


def get_text_length(text):
    return FONT.getsize(text)[0]


def text_to_image(text):
    image = Image.new("RGB", (get_text_length(text), 32), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.font = FONT
    draw.text((0, 0), text, (255, 255, 255))
    return image


def get_unko():
    response = requests.get(URL)
    text = response.text.replace('\n', '').split('<div class=unko-panel>')[1].split('</div>')[0]
    text = '          ' + text + '          '
    return text

if __name__ == '__main__':
    text_to_image(get_unko()).save(IMAGE_FILE)
