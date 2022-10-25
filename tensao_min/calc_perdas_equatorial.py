import shutil
import py_dss_interface
import pandas as pd
import os
import winsound
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def clique_abrir():
    global caminho
    caminho = filedialog.askdirectory()

    if caminho != '':

        abrir["state"] = "disabled"
        status["text"] = "status: Carregando os arquivos"
        progress_bar.place(x=10, y=100)
        progresso = 0.0
        percentual.config(text=str(0.0) + " %")
        progress_bar = 0.0
        root.update()

        dss = py_dss_interface.DSSDLL()



        arquivos = os.listdir(fr"{caminho}")
        alimentadores = list()
        i=0



        for i in range(len(arquivos)):
            alimentadores.append(arquivos[i])
            i += 1

        perdas_alimentadores = pd.read_csv(fr'{caminho}.csv', delimiter=',')
        progresso += 1
        percentual.config(text=str(round(progresso / len(alimentadores) * 100, 1)) + " %")
        progress_bar['value'] = progresso / len(alimentadores) * 100
        root.update()
        i += 1

    winsound.MessageBeep()
    status["text"] = "Status: Fim!! Arquivo salvo na pasta selecionada.                      "
    root.update()


# Criação da Interface Gráfica

caminho = ''
root = tk.Tk()
root.title("Perdas Equatorial")
root.geometry("360x160")
root.resizable(False, False)
texto = Label(root, text="Selecione a pasta em que se encontram todos os alimentadores.")
texto.place(x=8, y=5)
abrir = tk.Button(root, text="Selecionar", padx=10, pady=2, command=clique_abrir)
abrir.place(x=135, y=40)
nome_arquivo = Label(root, text="")
nome_arquivo.place(x=110, y=75)
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
percentual = Label(root, text="")
percentual.place(x=315, y=100)
status = Label(root, text="Status: Aguardando a seleção da pasta.                                           ",
               borderwidth=2, relief='groove')
status.place(x=10, y=130)
root.mainloop()

print("")