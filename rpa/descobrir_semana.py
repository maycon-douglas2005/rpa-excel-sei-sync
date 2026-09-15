import datetime
import calendar 

dia_atual = datetime.date.today().day

mes = datetime.date.today().month

ano = datetime.date.today().year

matriz_mes_atual = calendar.monthcalendar(ano, mes)




def retornarSemana():
    semana_atual = 0
    
    
    if dia_atual  in  matriz_mes_atual[0]:
        semana_atual = 1
        
    elif dia_atual in matriz_mes_atual[1]:
        semana_atual = 2
        
    elif dia_atual in matriz_mes_atual[2]:
        semana_atual = 3
        
    elif dia_atual in matriz_mes_atual[3]:
        semana_atual = 4
        
    elif dia_atual in matriz_mes_atual[4]:
        semana_atual = 1
        
    elif dia_atual in matriz_mes_atual[5]:
        semana_atual = 2
        
    else:
        print("Erro na função")
        
    return semana_atual