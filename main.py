import PySimpleGUI as sg
from getpass import getpass

layout = [
    [sg.Text('Digite seu login: '), sg.Input(key='-LOGIN-')],
    [sg.Text('Digite sua senha: '),sg.Input(key='-PASSWORD-', password_char= '*')],
    [sg.Button('Exibir senha'), sg.Button('Sair'), sg.Button('Entrar', size = (10,2))]
]


window = sg.Window("Site da Pituxa - Login", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Exibir senha':
        password = values['-PASSWORD-']
        secret_password = '*' * len(password)
        sg.popup('A senha digitada foi:'+password)

window.close()




