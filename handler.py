try:
    import unzip_requirements
except ImportError:
    pass

import numpy
from PIL import Image, ImageDraw, ImageFont

import json
import requests
import base64
import random
import uuid
import json
import re
from PIL import Image

import data_storage

font = ImageFont.truetype('./font.otf',
                          50,
                          encoding='unic')

def exec_gacha(event, context):
    if event:
        random.seed(re.sub(r'\D', '', event['path']))

    seed = random.randrange(99)

    l = [i for i in data_storage.lst_table if 0 <= seed - i - 1 ]
    rew = random.choice(data_storage.lst_rew[len(l)])
    W, H = (840, 400)
    #img_canvas = Image.new('RGBA', (960, 540), (0,0,0,0))
    img_canvas = Image.new('RGBA', (W, H), (20,20,20, 255))
    #img_back = Image.open('original.jpg')
    #img_sprite = Image.new('RGBA', (960, 540), (0,0,0,0))
    img_sprite = Image.new('RGBA', (W, H), (0,0,0,0))
    #img_canvas.paste(img_back)
    draw = ImageDraw.Draw(img_canvas)
    txt_rew = "{}\n{}".format(data_storage.lst_title[len(l)], rew)
    w, h = draw.textsize(txt_rew, font = font)
    draw.text(((W-w)/2,(H-h)/2), txt_rew, font = font, fill='#ffffff')
    
    img_canvas.paste(img_sprite,mask=img_sprite)
        
    save_file_path = "/tmp/test.png"
    img_canvas.save(save_file_path)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/apng",
        },
        "body": base64.b64encode(open(save_file_path, 'rb').read()).decode('utf-8'),
        "isBase64Encoded": True}
