from tkinter import *
from tkinter import Tk, ttk

# importando Pillow
from PIL import Image, ImageTk
# cores 

co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = "#6e8faf" # 
co11 = "#f2f4f2" # 

# Crinndo janela ---------------------------------------------------------------------------------------------------------------
janela =  Tk()
janela.title("")
janela.geometry('380x500')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')


# Frames -----------------------------------------------------------------------------------------------------------------------
frameCima = Frame(janela, width=380, height=50, bg=co1)
frameCima.grid(row=0, column=0, columnspan=2)

frameResultado = Frame(janela, width=380, height=50, bg=co3)
frameResultado.grid(row=1, column=0, pady=10)

frameBaixo = Frame(janela, width=380, height=50, bg=co1)
frameBaixo.grid(row=2, column=0, pady=10)

# Dividindo o frame baixo
frameAtivos = Frame(frameBaixo, width=180, height=370, bg=co9)
frameAtivos.grid(row=0, column=0, padx=5)

framePassivos = Frame(frameBaixo, width=180, height=370, bg=co9)
framePassivos.grid(row=0, column=1)


# Logo ------------------------------------------------------------------------------------------------------------------------

# abrindo a  imagem
app_img = Image.open('logo.png')
app_img = app_img.resize(50,50)
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, Image=app_img, width=900, compound=LEFT,  padx=5, anchor=NW,  bg=co1, fg=c04)
app_logo.place(x=5, y=0)

app_logo = Label(frameCima, text='Calculadora de patrimonio liquido', width=900, compound=LEFT,  padx=5, anchor=NW, font=('Ivy, 12'),  bg=co1, fg=c04)
app_logo.place(x=50, y=0)

l_linha = Label(frameCima, width=900, compound=LEFT, anchor=NW, font=('Verdana, 1'),  bg=co1, fg=c04)
l_linha.place(x=0, y=47)

# Função patrimonio líquido

def calcular():

    # Obtendo os valores Ativos
    ativo_1 = e_valor_casa.get()
    ativo_2 = e_valor_imoveis.get()
    ativo_3 = e_valor_veiculuos.get()
    ativo_4 = e_valor_investimentos.get()
    ativo_5 = e_valor_outros.get()

    # Obtendo os valores Passivos
    passivo_1 = e_valor_hipoteca.get()
    passivo_2 = e_valor_carro.get()
    passivo_3 = e_valor_estudante.get()
    passivo_4 = e_valor_dívidas.get()

    # verificando as entradas se estão vazias 
    if ativo_1 == '' or ativo_2 == '' or ativo_3 == '' or ativo_4 == '' or ativo_5 == '' or passivo_1 == '' or passivo_2 == '' or passivo_3 == '' or passivo_4 == '':
        print('Introduza algum valor nos campos vazios!')
        return

    else:
        # Calculando o Total de ativos
        Total_ativos = float(ativo_1) + float(ativo_2) + float(ativo_3) + float(ativo_4) + float(ativo_5)

        # Calculando o Total de passivos
        Total_passivos = float(passivo_1) + float(passivo_2) + float(passivo_3) + float(passivo_4)

        # Calculando o patrimonio líquido
        Patrimonio_liquido = Total_ativos - Total_passivos

        l_resultado['text '] = 'R${:,.2f}'.format(Patrimonio_liquido)
        

# Entradas Ativos ----------------------------------------------------------------------------------

l_nome = Label(frameAtivos, text='Insira Ativos', padx=10, width=35,  height=1, anchor=NW, font=(('Verdana 11')), bg=co2, fg=c01)
l_nome.place(x=0, y=0)

# valor da casa 
l_nome = Label(frameAtivos, text='Valor Casa', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=40)
e_valor_casa = Entry(frameCima, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_casa.place(x=10, y=65)

# imóveis 
l_nome = Label(frameAtivos, text='Imóveis', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=105)
e_valor_imoveis = Entry(frameCima, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_imoveis.place(x=10, y=125)

# veículos
l_nome = Label(frameAtivos, text='Veiculos', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=165)
e_valor_veiculuos = Entry(frameCima, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_veiculuos.place(x=10, y=195)

# Investimentos
l_nome = Label(frameAtivos, text='Investimentos', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=230)
e_valor_investimentos = Entry(frameCima, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_investimentos.place(x=10, y=255)

# Outros ativos 
l_nome = Label(frameAtivos, text='Outros ativos', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=295)
e_valor_outros = Entry(frameCima, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_outros.place(x=10, y=315)


# Entradas Passivos ----------------------------------------------------------------------------------

l_nome = Label(framePassivos, text='Insira Ativos', padx=10, width=35,  height=1, anchor=NW, font=(('Verdana 11')), bg=co5, fg=c01)
l_nome.place(x=0, y=0)

# Hipoteca
l_nome = Label(framePassivos, text='Valor Casa', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=40)
e_valor_hipoteca = Entry(framePassivos, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_hipoteca.place(x=10, y=65)

# Empréstimos de carros
l_nome = Label(framePassivos, text='Empréstimos de carros', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=105)
e_valor_carro = Entry(framePassivos, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_carro.place(x=10, y=125)

# Empréstimos estudantis
l_nome = Label(framePassivos, text='Empréstimos estudantis', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=165)
e_valor_estudante = Entry(framePassivos, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_estudante.place(x=10, y=195)

# Outras Dívidas
l_nome = Label(framePassivos, text='Outras Dívidas', anchor=E, font=(('Verdana 9')), bg=co9, fg=co0)
l_nome.place(x=10, y=230)
e_valor_dívidas = Entry(framePassivos, width=10, font=('Ivy 12'), justify='center', relief='solid')
e_valor_dívidas.place(x=10, y=255)

# Resultado----------------------------------------------------------------------------------------------------
l_resultado = Label(frameResultado, text='R${:,.2f}'.format(00), padx=10, width=15, anchor=NEW, font=('Verdana 25 bold'), bg=co3, fg=co1)
l_resultado.place(x=0, y=7)

botao_calcular = Button(framePassivos, command=calcular, text='Calcular'.upper(), padx=10, width=12, anchor='CENTER', font=('Ivy 9 bold'), bg=co3, fg=co0)
botao_calcular.place(x=10, y=310)

janela.mainloop()