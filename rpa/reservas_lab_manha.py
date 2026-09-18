import pyautogui
import time
import pyperclip

import Helpers 

"""

Pré-requisitos / Limitações temporárias: 

- Estar com o dia desejado já selecionado no filtro de dia na planilha das reservas 
- Estar com navegador aberto logado no SEI.
- NÃO estar com mais nenhuma planilha excel aberta.

"""

# Recomendações: Estar com  apenas uma janela do navegador aberta.


# ACESSANDO OCORRENCIA PATRIMONIO
pyautogui.hotkey('ctrl', 'shift', 'esc')
time.sleep(1)
pyautogui.hotkey('alt', 'n')
time.sleep(1)
pyautogui.write("https://sei.pentagonoedu.com.br/visaoAdministrativo/patrimonio/ocorrenciaPatrimonioForm.xhtml")
pyautogui.press('enter')
time.sleep(1)



##selecionando 'Tipo Ocorrência'
pyautogui.press('tab', presses=4,  interval=0.5)
time.sleep(1)
pyautogui.press('space')
time.sleep(1)
pyautogui.press('down', presses=7, interval=0.1)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)


# PEGANDO DADOS DA PLANILHA E COLOCANDO NO FORM DE OCORRENCIA

##acessando planilha de reserva
pyautogui.press("win")
time.sleep(2)
pyautogui.write("Documentos: AGENDAMENTO-MANHÃ-1SEM2026")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)



##pegando dados da planilha e colocando no form

###pegando motivo na planilha

pyautogui.hotkey('ctrl', 'l')
time.sleep(2)
pyautogui.write("AGENDAMENTO")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('esc')
time.sleep(2)
pyautogui.press('down')
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)





###inserindo motivo no form

pyautogui.hotkey('alt', 'tab')                      
time.sleep(2)
pyautogui.click(x=235, y=800)
pyautogui.press('tab', presses=5, interval=0.7)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')




###abrindo campo nome no form
time.sleep(2)
pyautogui.press('tab', presses=2, interval=0.5)
time.sleep(2)
pyautogui.press('space')
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(2)
pyautogui.press('del')
time.sleep(2)



###copiando nome na planilha
pyautogui.hotkey('alt', 'tab')
time.sleep(2)



pyautogui.press('F5')
time.sleep(2)
pyautogui.write("Professor")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('down')
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

###inserindo nome no form
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

###buscando prof
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('space')
time.sleep(2)


###selecionando prof
pyautogui.press('tab', presses=6, interval=0.5)
time.sleep(2)
pyautogui.press('space')


#DESCOBRIR SEMANA E PEGAR NUMERO DA SALA
time.sleep(2)
coluna_semana = Helpers.retornarSemana()
time.sleep(2)
##copiando sala
pyautogui.hotkey('alt', 'tab') #volta pra planilha de reservas
time.sleep(2)
pyautogui.press('F5')
time.sleep(2)
pyautogui.write("Horario")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('down')
time.sleep(2)
pyautogui.press('right', presses=coluna_semana, interval=0.2)
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.click(x=235, y=800)
time.sleep(2)
pyautogui.press('tab', presses=10, interval=0.3)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

##escrevendo sala no form 
pyautogui.press('tab', presses=2, interval=0.2)
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('space')
time.sleep(2)

##selecionando sala no form
pyautogui.press('tab', presses=7, interval=0.2)
time.sleep(2)
pyautogui.press('space')
time.sleep(2)



#DESCOBRIR DIA DA RESERVA
##copiando dia da semana da reserva
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('F5')
time.sleep(2)
pyautogui.write('DIa')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('down')
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

##colocando dia da semana no python
dia_copiado_planilha = str(pyperclip.paste().strip())
time.sleep(2)
data_reserva = Helpers.retornaDataReserva(dia_copiado_planilha)
time.sleep(2)
pyautogui.click(x=382, y=740)
time.sleep(2)
pyautogui.press('tab', presses=12, interval=0.5)
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(2)
pyautogui.press('del')
time.sleep(2)
pyautogui.write(data_reserva, interval=0.2)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)


#PEGANDO HORARIO INICIAL E FINAL

##copiando horário
pyautogui.click(x=2816, y=387)
time.sleep(2)
pyautogui.press('F5')
time.sleep(2)
pyautogui.write("Horario")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('down')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')


##trazendo horario para o python e tratando
horario_completo = pyperclip.paste()
horario_separado = horario_completo.split()

horario_inicial = horario_separado[0]
horario_final = horario_separado[2]


##colando hora inicial
time.sleep(2)
pyautogui.click(x=382, y=740)
time.sleep(2)
pyautogui.press('tab', presses=13, interval=0.5)
time.sleep(1)
pyautogui.press('del')
pyautogui.write(horario_inicial)
time.sleep(2)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(horario_final)
pyautogui.press('tab', presses=5, interval=0.3)
pyautogui.press('space')