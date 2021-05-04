#!/usr/bin/env python3
import PySimpleGUI as sg

sg.theme('Material2')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Programme de test VPV',font='20')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok', font='30'), sg.Button('Cancel', font='30')] ]

# Create the Window
window = sg.Window('Entrez votre image', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()