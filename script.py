from PIL import Image, ImageFont, ImageDraw
import os
from io import BytesIO
import numpy as np
import pandas as pd
from time import sleep

sheet = pd.read_excel(open('data/database/database.xlsx', 'rb'), engine='openpyxl', sheet_name='A')
index = int(input("Where do you want to start? (starts from 2):_"))
index = index-2

for i in sheet['Name']:
    temp = Image.open("data/template.jpg")
    name = str(sheet['Name'][index])
    ins = sheet['Institution'][index]
    nam = ''
    p = 0
    flex = name.split(' ')
    for f in flex:
        nam = nam+flex[p]+' '
        if p == 5:
            break
        p=p+1    
    draw = ImageDraw.Draw(temp)
    f64 = ImageFont.truetype("./data/fonts/GOTHICB.TTF",115)
    w, h = f64.getsize(name)
    draw.text(((3310-w),886), name, (255,255,255), font=f64)    
    w, h = f64.getsize(ins)
    draw.text(((3310-w),1145), ins, (255,255,255), font=f64)
    index += 1
    temp.save(f"output/main/{nam}.jpg")
    print(f'Successfully generated {index+1} at output/main/{nam}.jpg')
anykey = input("'q' to quit program:_")