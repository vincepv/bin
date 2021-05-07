#!/usr/bin/env python3
import PySimpleGUI as sg
import cv2
import numpy as np
from matplotlib import pyplot as plt

sg.theme('BluePurple')

layout = [[sg.Text("Saisir le chemin de l'image :"), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Valider'), sg.Button('Quitter')]]

window = sg.Window('Detect Object', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Quitter':
        break
    if event == 'Valider':
        image_source = values['-IN-'] 
        image = cv2.imread(image_source)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray,cmap='gray')
        blur = cv2.GaussianBlur(gray, (11,11),0)
        canny = cv2.Canny(blur, 100, 200,3)
        dilated = cv2.dilate(canny,(1,1), iterations =2)
# plt.imshow(dilated,cmap='gray')
        (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.drawContours(rgb, cnt, -1, (0,255,0), 3)
# plt.imshow(rgb)
        resultat = len(cnt), "objets détéctés dans la photo"
        window['-OUTPUT-'].update(resultat)

window.close()