import pandas as pd
from pandas import *
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

a=1
dia_util = 'DU'
domingo = 'DO'
sabado = 'SA'

global caminho
caminho = filedialog.askdirectory()

arquivos_pasta = os.listdir(fr"{caminho}")
alimentadores = list()

# reading CSV file
#data = pd.read_csv(r"ACL01C1_5678_OpenDSS.csv")
perdas_alimentadores = pd.read_csv(r'C:\Users\Isabela\Documents\P&D EQUATORIAL\FINAL\Caso_0\Caso_0\ACL01C1_5678_OpenDSS.csv', delimiter=',')

# # converting column data to list
titulo = perdas_alimentadores['Arquivo'].tolist()
T = titulo.split("_")
energia_ativa = perdas_alimentadores['Energia ativa (MWh)'].tolist()
perdas = perdas_alimentadores['Perdas (MWh)'].tolist()

# for a in range (12):

    # if 'mes' == 1
    #     if dia == 'DU':
    #         enrgia_soma = energia_ativa*20
    #         perdas_soma = perdas*20
    #     if dia == 'DO':
    #         enrgia_soma = energia_ativa*6
    #         perdas_soma = perdas*6
    #     if dia == 'SA':
    #         enrgia_soma = energia_ativa*5
    #         perdas_soma = perdas*5




print("")