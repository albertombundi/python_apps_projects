# Importando o Tkinter
from tkinter import *

# Importando Pillow
from PIL import Image, ImageTk

import random

# cores -----------------------------------------------------
co0 = "#f0f3f5" # cinzenta/ grey
co1 = "#feffff" # Branca/ white
co2 = "#3fb5a3" # Verde/ green
co3 = "#38576b" # azul escuro/ dark blue
co4 = "#403d3d" # preta/ black

# criando janela ---------------------------------------------
janela = Tk()
janela.title(" ")
janela.geometry('400x260')
janela.configure(background=co1)
janela.resizable(width=False, height=False)


# criando frames ---------------------------------------------
frame_cima = Frame(janela, width=500, height=50, bg=co2)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela, width=500, height=210, bg=co4)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frames ---------------------------------------------
l_app = Label(frame_cima, text='Acenda a Lampada', anchor=NE, font=('Ivy 20'), bg=co2, fg=co0)
l_app.place(x=5, y=5)


# Configurando frame baixo ---------------------------------------------
img_2 = Image.open('2.png')
img_2 = img_2.resize((40,40))
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open('3.png')
img_3 = img_3.resize((40,40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('4.png')
img_4 = img_4.resize((40,40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('5.png')
img_5 = img_5.resize((40,40))
img_5 = ImageTk.PhotoImage(img_5)

l_img = Label(frame_baixo, image=img_2, bg=co4)
l_img.place(x=30, y=5)

l_estado = Label(frame_baixo, text='Estou com medo', anchor=NW, font=('Ivy 20 bold'), bg=co4, fg=white)
l_estado.place(x=80, y=20)


global control
global contador


def ligar_lampada(i):
    global control

    lista = i


# Desabilitando o botão que foi desligado
if lista[1] == 'interuptor - 1':
    b_interuptor_1['state'] = 'disable'

elif lista[1] == 'interuptor - 2':
    b_interuptor_2['state'] = 'disable'

elif lista[1] == 'interuptor - 3':
    b_interuptor_3['state'] = 'disable'

elif lista[1] == 'interuptor - 4':
    b_interuptor_4['state'] = 'disable'

else:
    b_interuptor_5['state'] = 'disable'


def substituir_valor(i):
    global control
    nova_lista = []

    for string in control:
        novo_valor = string.replice(i[0], i[1])
        nova_lista.append(novo_valor)
    
    control = nova_lista

# selecionar valor aleatoriamente
valor_selecionado = random.sample(lista[0],1)[0]

if int(valor_selecionado) == 1:
    if control[0] == 'lampada_1':
        l_img_1['image'] = img_lampada_on
        l_img['image'] = img_3
        l_estado['text'] = 'Ok obrigado'
        substituir_valor(['lampada_1', str(1)])
    else:
        if control[1] == 'lampada_2':
            l_img_2['image'] = img_lampada_on
            l_img['image'] = img_4
            l_estado['text'] = 'Por favor, acenda a última'
            substituir_valor(['lampada_2', str(2)])
        else:
            if control[2] == 'lampada_3':
                l_img_2['image'] = img_lampada_on
                l_img['image'] = img_5
                l_estado['text'] = 'Muito, obrigado'
                substituir_valor(['lampada_3', str(3)])
        

control = ['lampada_1', 'lampada_2', 'lampada_4']


img_lampada_off = Image.open('0.png')
img_lampada_off = img_lampada_off.resize((110, 110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

img_lampada_on = Image.open('1.png')
img_lampada_on = img_lampada_on.resize((110, 110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)


l_img_1 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_img_1.place(x=5, y=70)

l_img_2 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_img_2.place(x=105, y=70)

l_img_3 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_img_3.place(x=205, y=70)

lista = [0, 1, 1, 1, 0]

b_interuptor_1 = Button(frame_baixo, command=lambda i=[lista, 'interuptor - 1']:ligar_lampada(), text='Interuptor - 1', anchor=NW, overrelief=RIDGE, relief=RAIZED, font=('Ivy 20 bold'), bg=co4, fg=white)
b_interuptor_1.place(x=300, y=50)

b_interuptor_2 = Button(frame_baixo, command=lambda i=[lista, 'interuptor - 2']:ligar_lampada(), text='Interuptor - 2', anchor=NW, overrelief=RIDGE, relief=RAIZED, font=('Ivy 20 bold'), bg=co4, fg=white)
b_interuptor_2.place(x=300, y=50)

b_interuptor_3 = Button(frame_baixo, command=lambda i=[lista, 'interuptor - 3']:ligar_lampada(i), text='Interuptor - 3', anchor=NW, overrelief=RIDGE, relief=RAIZED, font=('Ivy 20 bold'), bg=co4, fg=white)
b_interuptor_3.place(x=300, y=50)

b_interuptor_4 = Button(frame_baixo, command=lambda i=[lista, 'interuptor - 4']:ligar_lampada(i), text='Interuptor - 4', anchor=NW, overrelief=RIDGE, relief=RAIZED, font=('Ivy 20 bold'), bg=co4, fg=white)
b_interuptor_4.place(x=300, y=50)

b_interuptor_5 = Button(frame_baixo, command=lambda i=[lista, 'interuptor - 5']:ligar_lampada(i), text='Interuptor - 5', anchor=NW, overrelief=RIDGE, relief=RAIZED, font=('Ivy 20 bold'), bg=co4, fg=white)
b_interuptor_5.place(x=300, y=50)



janela.mainloop()