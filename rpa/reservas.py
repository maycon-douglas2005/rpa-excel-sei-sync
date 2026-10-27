import pyautogui
import time
import pyperclip
import datetime
import Helpers 


numero_do_registro =  0


"""

Pré-requisitos / Limitações temporárias: 

- Estar com o dia desejado já selecionado no filtro de dia na planilha das reservas 
- Estar com navegador aberto logado no SEI.
- NÃO estar com mais nenhuma planilha excel aberta.

""" 

# Recomendações: Estar com  apenas uma janela do navegador aberta. 

# ACESSANDO SEI 

pyautogui.hotkey('ctrl', 'shift', 'esc')
time.sleep(1)
pyautogui.hotkey('alt', 'n')
time.sleep(1)
pyautogui.write("https://sei.pentagonoedu.com.br/visaoAdministrativo/patrimonio/ocorrenciaPatrimonioForm.xhtml")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)


while True:
    numero_do_registro += 1 
    ##selecionando 'Tipo Ocorrência'
    print("selecionando 'Tipo Ocorrência'")
    
    pyautogui.click(x=188, y=622)
    pyautogui.press('tab', presses=4,  interval=0.9)
    pyautogui.press('space')
    time.sleep(0.5)
    pyautogui.press('down', presses=7, interval=0.2)
    time.sleep(0.5)
    pyautogui.press('enter')


    # PEGANDO DADOS DA PLANILHA E COLOCANDO NO FORM DE OCORRENCIA

    ##acessando planilha de reserva
    
    print("selecionando 'Tipo Ocorrência'")
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("Documentos: AGENDAMENTO-MANHÃ-1SEM2026")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)



    ##pegando dados da planilha e colocando no form

    ###pegando motivo na planilha
    print("pegando motivo na planilha")
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write("AGENDAMENTO")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('down', presses=numero_do_registro, interval=0.3)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    valor_copiado = pyperclip.paste().strip()
    if valor_copiado == "":
        print("Automação Acabou. Acabaram as Reservas")
        break




    ###inserindo motivo no form
    print("inserindo motivo no form")
    pyautogui.hotkey('alt', 'tab')                      
    time.sleep(1)
    pyautogui.click(x=235, y=800)
    time.sleep(0.5)
    pyautogui.press('tab', presses=5, interval=0.5)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')




    ###abrindo campo nome no form
    print("abrindo campo nome no form")
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)
    pyautogui.press('del')
    time.sleep(0.3)



    ###copiando nome na planilha
    print("copiando nome na planilha")
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)
    pyautogui.press('F5')
    time.sleep(1)
    pyautogui.write("Professor")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('down', presses=numero_do_registro, interval=0.3)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    ###inserindo nome no form
    print("inserindo nome no form")
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    ###buscando prof
    print("buscando prof")
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)


    ###selecionando prof
    print("selecionando prof")
    pyautogui.press('tab', presses=6, interval=0.3)
    time.sleep(0.5)
    pyautogui.press('space')
    


    #DESCOBRIR SEMANA E PEGAR NUMERO DA SALA
    print("DESCOBRIR SEMANA E PEGAR NUMERO DA SALA")
    coluna_semana = Helpers.retornarSemana()
    ##copiando sala
    pyautogui.hotkey('alt', 'tab') #volta pra planilha de reservas
    time.sleep(1)
    pyautogui.press('F5')
    time.sleep(1)
    pyautogui.write("Horario")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('down', presses=numero_do_registro, interval=0.3)
    time.sleep(1)
    pyautogui.press('right', presses=coluna_semana, interval=0.3)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.click(x=235, y=800)
    time.sleep(1)
    pyautogui.press('tab', presses=10, interval=0.6)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    ##escrevendo sala no form 
    print("escrevendo sala no form ")
    pyautogui.press('tab', presses=2, interval=0.5)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('space')
    

    ##selecionando sala no form
    print("selecionando sala no form")
    pyautogui.press('tab', presses=7, interval=0.6)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    

    #DESCOBRIR DIA DA RESERVA
    ##copiando dia da semana da reserva
    print("copiando dia da semana da reserva")
    time.sleep(1)
    pyautogui.press('F5')
    time.sleep(1)
    pyautogui.write('DIa')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('down', presses=numero_do_registro, interval=0.3)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    ##colocando dia da semana no python
    print("colocando dia da semana no python")
    dia_copiado_planilha = str(pyperclip.paste().strip())
    data_reserva = Helpers.retornaDataReserva(dia_copiado_planilha)
    pyautogui.hotkey('alt', 'tab') # <--- ALTERADO: Volta para o SEI
    time.sleep(1)
    pyautogui.press('tab', presses=12, interval=0.3)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('del')
    time.sleep(1)
    print("colando dia da semana no form")
    pyautogui.write(data_reserva)
    time.sleep(1)
    pyautogui.press('enter')
    


    #PEGANDO HORARIO INICIAL E FINAL

    ##copiando horário
    print("copiando horário")
    pyautogui.hotkey('alt', 'tab') # <--- ALTERADO: Volta para a planilha (antes era x=2816, y=387)
    time.sleep(1)
    pyautogui.press('F5')
    time.sleep(1)
    pyautogui.write("Horario")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('down', presses=numero_do_registro, interval=0.3)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')


    ##trazendo horario para o python e tratando
    print("trazendo horario para o python e tratando")
    horario_completo = pyperclip.paste()
    horario_separado = horario_completo.split()

    horario_inicial = horario_separado[0]
    horario_final = horario_separado[2]

    ###diminuindo 5 minutos do horário final
    horario_objeto = datetime.datetime.strptime(horario_final, "%H:%M")#esse código é para indicar q é no formato hora minuto
    
    novo_horario_final = horario_objeto - datetime.timedelta(minutes=5)

    horario_final_pronto = novo_horario_final.strftime("%H:%M")

    ##colando hora inicial
    print("colando hora inicial")
    pyautogui.hotkey('alt', 'tab') # <--- ALTERADO: Volta para o SEI
    time.sleep(1)
    pyautogui.click()
    pyautogui.press('tab', presses=13, interval=0.5)
    time.sleep(1)
    pyautogui.press('del')
    pyautogui.write(horario_inicial)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(horario_final_pronto)
    pyautogui.press('tab', presses=5, interval=0.3)
    pyautogui.press('space')
    time.sleep(3)
    pyautogui.click(x=328, y=759) # Mantido: Presumo que seja um clique de confirmação ou pop-up do formulário
    time.sleep(0.5)



    ##REINICIANDO PROCESSO
    print("REINICIANDO PROCESSO")
    pyautogui.press('tab', presses=11, interval=0.5)
    time.sleep(0.8)
    pyautogui.press('space')
    time.sleep(1)