#ARQUIVO USADO PARA TESTAR SCRIPTS ANTES DE INSERIR NOS ARQUIVOS PRINCIPAIS
"""
import pyautogui
import time
import descobrir_semana


time.sleep(3)
print(pyautogui.position())



teste = descobrir_semana.retornarSemana() + 1

print(teste)

"""

import datetime
import calendar 

dia_atual = datetime.date.today().day

mes = datetime.date.today().month

ano = datetime.date.today().year

matriz_mes_atual = calendar.monthcalendar(ano, mes)

print(matriz_mes_atual)