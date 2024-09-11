import PySimpleGUI as sg

# 1º Criar as Janelas e os estilos(layout)
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Peperoni', key='pizza1'), sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido',  layout=layout, finalize=True)

# Criar as janelas iniciais
janela1,janela2 = janela_login(), None
# Criar um loop de leitura de eventos
while True:
    Window,event,values = sg.read_all_windows()
    # Quando a janela for fechada
    if Window == janela1 and event == sg.WIN_CLOSED:
        break 
    # Quando queremos ir para proxima janela
    if Window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if Window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if Window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma pizza Peperoni e uma Pizza Catupiri c/ Frango')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitada uma pizza Peperoni')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitada uma pizza Catupiri c/ Frango')
    # Quando queremos voltar para janela anterior
# lógica de o que deve acontecer ao clicar no botões


