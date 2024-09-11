# importando o tkinter 
from tkinter import *
from tkinter import Tk, ttk

# importando o Pillow
from PIL import Image, ImageTk

import random


# cores -----------------------------------------------------

co0 = "#2e2d2b" # preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde

# criando a janela -------------------------------------------

janela = Tk()
janela.title("Calculadora de amor")
janela.geometry("410x400")
janela.configure(background=co1)
janela.resizable(height=FALSE, width=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# frames ------------------------------------------------------

frameCima = Frame(janela, width=418, height=200, bg=co1)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=418, height=200, bg=co1, relief='solid')
frameMeio.grid(row=1, column=0)


# logo---------------------------------------------------------

app_ = Label(frameCima, text='Calculadora do amor', width=400, padx=5, anchor=NW, font=('Fixedsys 20'), bg=co7, fg=co1)
app_.place(x=0, y=0)


# função calcular amor

def calcular_amor():
    # pegando nomes
    nome_1 = e_seu_nome.get()
    nome_2 = e_parceiro_nome.get()


    # valor conterá dígitos entre 0-9

    st = '0123456789'

    # resultado será em dois dígitos
    digitos = 2

    # variável que contém o resultado
    resultado = "".join(random.sample(st, digitos))
    print(resultado)

    l_resultado['text'] = 'Porcentagem de amor entre'
    l_resultado_1['text'] = nome_1 + " & " + nome_2
    l_resultado_2['text'] = resultado + " % "



# Função para escolher opções-----------------------------------

def escolher():

    # variaveis globais
    global app_img, app_love

    escolha_1 = selecionado_1.get()
    escolha_2 = selecionado_2.get()


    if escolha_1 == 'Homem' and escolha_2 == 'Mulher':
        imagem = 'casal_4.png'
        imagem_2 = 'coracao_2.png'

    elif escolha_1 == 'Homem' and escolha_2 == 'Homem':
        imagem = 'casal_1.png'
        imagem_2 = 'coracao_1.png'

    elif escolha_1 == 'Mulher' and escolha_2 == 'Mulher':
        imagem = 'casal_5.png'
        imagem_2 = 'coracao_2.png'

    else:
        print('Selecione os géneros')
        return

    # abrindo imagem casal
    app_img = Image.open(imagem)
    app_img = app_img.resize((140, 140))
    app_img = ImageTk.PhotoImage(app_img)
    app_logo['image'] = app_img

    # abrindo imagem botao
    app_love = Image.open(imagem_2)
    app_love = app_love.resize((30, 30))
    app_love = ImageTk.PhotoImage(app_love)
    botao_calcular['image'] = app_love


# abrindo imagens
app_img = Image.open('coracao.png')
app_img = app_img.resize((140, 140))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg=co7, fg=co1)
app_logo.place(x=10, y=50)


# Resultados ---------------------------------------------------

l_resultado = Label(frameCima, text='', width=35, padx=10, anchor=NW, font=('Verdana 10'), bg=co7, fg=co0)
l_resultado.place(x=170, y=100)

l_resultado_1 = Label(frameCima, text='', width=17, padx=10, anchor=CENTER, font=('Verdana 12 bold'), bg=co7, fg=co5)
l_resultado_1.place(x=170, y=70)

l_resultado_2 = Label(frameCima, text='', width=5, padx=10, anchor=CENTER, font=('Verdana 25 bold'), bg=co7, fg=co0)
l_resultado_2.place(x=210, y=140)


# Frame meio ---------------------------------------------------

l_nome = Label(frameMeio, text='Seu nome', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=6, y=15)

e_seu_nome = Entry(frameMeio, width=15, font=('Ivy 14'), justify='center', relief='solid' )
e_seu_nome.place(x=10, y=40)

selecionado_1 = StringVar()

rad_1 = RadioButton(frameMeio, command=escolher, text='Homem', bg=co1, font=('Ivy 10'), value='Homem', variable=selecionado_1).place(x=10, y=80)
rad_2 = RadioButton(frameMeio, command=escolher, text='Mulher', bg=co1, font=('Ivy 10'), value='Mulher', variable=selecionado_1).place(x=10, y=105)

l_linha = Label(frameMeio, width=1, height=10, anchor=NW, font=('verdana 1'), bg=co3, fg=co1)
l_linha.place(x=40, y=40)

l_linha = Label(frameMeio, width=1, height=10, anchor=NW, font=('verdana 1'), bg=co5, fg=co1)
l_linha.place(x=200, y=40)


l_nome = Label(frameMeio, text='Nome do/a Parceiro/a', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=217, y=15)

e_parceiro_nome = Entry(frameMeio, width=15, font=('Ivy 14'), justify='center', relief='solid' )
e_parceiro_nome.place(x=220, y=40)

selecionado_2 = StringVar()

rad_3 = RadioButton(frameMeio, command=escolher, text='Homem', bg=co1, font=('Ivy 10'), value='Homem', variable=selecionado_2).place(x=220, y=80)
rad_4 = RadioButton(frameMeio, command=escolher, text='Mulher', bg=co1, font=('Ivy 10'), value='Mulher', variable=selecionado_2).place(x=200, y=105)

# botão calcular --------------------------------

# abrindo imagem

app_love = Image.open('coracao_1.png')
app_love = app_love.resize((30, 30))
app_love = ImageTk.PhotoImage(app_love)


botao_calcular = Label(frameMeio, command=calcular_amor, image=app_love, width=200, compound=LEFT,  text='Calcular Amor'.upper(), anchor=CENTER, font=('Ivy 9'), bg=co7, fg=co0)
botao_calcular.place(x=110, y=140)

janela.mainloop()