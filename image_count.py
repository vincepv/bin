#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
#https://www.youtube.com/watch?v=rRcwuQGDFOA

image_source = input('Quel est la source ? Mettre le chemin entier du fichier.')
image = cv2.imread(image_source)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray,cmap='gray')
blur = cv2.GaussianBlur(gray, (11,11),0)
canny = cv2.Canny(blur,30 ,100,3)
dilated = cv2.dilate(canny,(1,1), iterations =3)
# plt.imshow(dilated,cmap='gray')

(cnt,heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0,255,0), 3)
#plt.imshow(rgb)

print('Il y a ', len(cnt), 'objets détectés dans la photo.')