from tkinter import *
import random


def verificar_chute():
    global tentativas, numero_secreto
    chute = int(chute_entry.get())
    chute_entry.delete(0, END)

    if chute == numero_secreto:
        resultado_label.config(text='Parabéns! Você acertou o número!')
        chute_entry.config(state='disabled')
        botao_verificar.config(state='disabled')
    elif chute < numero_secreto:
        resultado_label.config(text='Tente um número maior.')
    else:
        resultado_label.config(text='Tente um número menor.')

    tentativas -= 1
    if tentativas == 0 and chute != numero_secreto:
        resultado_label.config(text=f'Você perdeu! O número correto era {numero_secreto}.')
        chute_entry.config(state='disabled')
        botao_verificar.config(state='disabled')


tentativas = 10
numero_secreto = random.randint(1, 100)


janela = Tk()
janela.title('Jogo de Adivinhação de Números')
janela.geometry('400x300')


texto_orientacao = Label(janela, text='Tente adivinhar o número entre 1 e 100:')
texto_orientacao.pack(padx=10, pady=10)

chute_entry = Entry(janela)
chute_entry.pack(padx=10, pady=10)

botao_verificar = Button(janela, text='Verificar', command=verificar_chute)
botao_verificar.pack(padx=10, pady=10)

resultado_label = Label(janela, text=f'Número de tentativas restantes: {tentativas}')
resultado_label.pack(padx=10, pady=10)


janela.mainloop()
