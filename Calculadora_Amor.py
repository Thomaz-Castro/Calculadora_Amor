from PySimpleGUI import PySimpleGUI as sg
from random import randrange
from time import sleep

#layout
sg.theme('DarkBlue13')
font = ('Arial', 50)
layout_column = [
    [sg.Text('Nome 1'), sg.Input(key='nomeUm', size=(7,1)),sg.Image('Coracion.png'),sg.Text('Nome 2'), sg.Input(key='nomeDois', size=(7,1))],
    [sg.Button('Calcular'), sg.Text('', key='percent', font=font)]
]

layout = [[sg.Column(layout_column, element_justification='center')]]

#Janela
janela = sg.Window('Calculadora do Amor', layout=layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Calcular':
        for c in range(0, 50):
            per= str(randrange(0,100))
            per = per + '%'
            janela['percent'].update(per)
