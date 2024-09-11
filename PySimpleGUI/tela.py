# criando tela em python usando o PythonSimpleGUI
import PySimpleGUI as sg

class TelaPython:
    def _init_(self):
        sg.change_look_and_feel('DarkBlue2')
        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'), sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao').sg.Radio('Não', 'cartoes',key='naoAceitaCartao')],
            [sg.Slider(range(0,255), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]

        #janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
    
    def Iniciar(self):
        while True:
            #Extrair os dados da tela
            self.Button, self.values = self.janela.Read()   
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'Aceita Cartao:{aceita_cartao}')
            print(f'Não aceita cartão:{nao_aceita_cartao}')
            print(f'Velocidade script:{velocidade_script}')



tela = TelaPython()
tela.Iniciar()