import datetime
import calendar 

##VARIAVEIS USADAS NAS FUNÇÕES
dia_atual = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year
matriz_mes_atual = calendar.monthcalendar(ano, mes)
semana_atual = 0
array_matriz_semana_atual = 0

###DESCOBRIR QUAL SEMANA SEGUINTE PARA RESERVA
def retornarSemana():
    global semana_atual
    global array_matriz_semana_atual
    if dia_atual  in  matriz_mes_atual[0]:
        semana_atual = 1
        array_matriz_semana_atual = 0
        
    elif dia_atual in matriz_mes_atual[1]:
        semana_atual = 2
        array_matriz_semana_atual = 1
        
    elif dia_atual in matriz_mes_atual[2]:
        semana_atual = 3
        array_matriz_semana_atual = 2
        
    elif dia_atual in matriz_mes_atual[3]:
        semana_atual = 4
        array_matriz_semana_atual = 3
        
    elif dia_atual in matriz_mes_atual[4]:
        semana_atual = 1
        array_matriz_semana_atual = 4
        
    elif dia_atual in matriz_mes_atual[5]:
        semana_atual = 2
        array_matriz_semana_atual = 5
        
    else:
        print("Erro na função")
        
    return semana_atual + 1 #retorna a semana seguinte q é a utilizada na reserva



###DESCOBRIR QUAL DIA EXATO DA RESERVA
def retornaDiaReserva(dia):
    ##posicao do dia da semana 
    retorno_dia = {
        "Seg": 0,
        "Ter": 1,
        "Qua": 2,
        "Qui": 3,
        "Sex": 4
    }

    posicao_dia_reserva = retorno_dia.get(dia, 0)

    ##pegar dia exato da reserva
    quant_semanas_mes = len(matriz_mes_atual)
    indice_ultima_semana = quant_semanas_mes - 1
    dia_reserva = 0
    if indice_ultima_semana != array_matriz_semana_atual:

        dia_reserva = matriz_mes_atual[int(array_matriz_semana_atual)+1][int(posicao_dia_reserva)]
    else:
        print("Ainda nao fiz essa parte")
        #dia_reserva = matriz_mes_atual[0][posicao_dia_reserva]  VOU TER Q PEGAR A VARIAVEL DO MES, ADICIONAR 1 PRA IR PRO OUTRO MES, E RODAR NOVAMENTE O calendar.monthcalendar para ter o nova matriz do outro mes, ai depois libero essa linha
        #alem disso tem a questao de q a reserva da penultima semana para a ultima semana sendo q a ultima semana contem dias do outro mes, esta com incoscistencia pq o dia do outro mes cai como zero. ARRUMAR!
    return dia_reserva

###RETORNA DIA/MES/ANO PARA DATA RESERVA
def retornaDataReserva(dia):

    data_reserva_pronta = f"{int(retornaDiaReserva(dia))}/0{mes}/{ano}"

    return data_reserva_pronta
