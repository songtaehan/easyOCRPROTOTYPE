import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

#src is gray scale of image
image = cv2.imread('cocoa.jpg')
src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

reader = easyocr.Reader(['ko','en'])
result =  reader.readtext('cocoa.jpg')


image = Image.fromarray(image)
font = ImageFont.truetype("malgun.ttf", 15)  # Adjusted font size to 5
draw = ImageDraw.Draw(image)

for i in result:
  x = i[0][0][0]
  y = i[0][0][1]
  w = i[0][1][0] - i[0][0][0]
  h = i[0][2][1] - i[0][1][1]

  draw.rectangle(((x, y), (x+w, y+h)), outline="blue", width=2)
  draw.text((int((x+x+w)/2), y-20), str(i[1]), font=font, fill="black")  # Adjusted font color to black
#figsize 20 12
plt.figure(figsize=(20,12))
plt.imshow(image)
plt.show()