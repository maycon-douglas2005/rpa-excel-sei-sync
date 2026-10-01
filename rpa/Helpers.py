import datetime
import calendar 
import time
##VARIAVEIS USADAS NAS FUNÇÕES
dia_atual = 2 #datetime.date.today().day


mes = 10    #datetime.date.today().month


ano = 2026 #datetime.date.today().year
matriz_mes_atual = calendar.monthcalendar(ano, mes)
semana_atual = 0
array_matriz_semana_atual = -1
quant_semanas_mes = len(matriz_mes_atual)

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
        semana_atual = 0
        array_matriz_semana_atual = 3
        
    elif dia_atual in matriz_mes_atual[4]:
        semana_atual = 1
        array_matriz_semana_atual = 4
        
        
    else:
        print("Erro na função")
        
    return semana_atual + 1 #retorna a semana seguinte q é a utilizada na reserva



###DESCOBRIR QUAL DIA EXATO DA RESERVA
def retornaDiaReserva(dia):
    print(f"Dia pego na função retornaDiaReserva: {dia}")
    ##posicao do dia da semana 
    retorno_dia = {
        "Seg": 0,
        "Ter": 1,
        "Qua": 2,
        "Qui": 3,
        "Sex": 4
    }

    
    posicao_dia_reserva = retorno_dia.get(dia, 15) # Deixe 0 como escape padrão
    time.sleep(1)
    print(f"Dia que a função PEGOU: {posicao_dia_reserva}")
    ##pegar dia exato da reserva
    dia_reserva = 0
    dia_reserva = matriz_mes_atual[int(array_matriz_semana_atual)+1][int(posicao_dia_reserva)]

    """

    indice_ultima_semana = quant_semanas_mes - 1
   
    
    if indice_ultima_semana != array_matriz_semana_atual:

        
    else:
        # Pega a variável do mês e adiciona 1 para ir para o outro mês
        proximo_mes = mes + 1
        proximo_ano = ano
        
        # Proteção para a virada de ano em dezembro
        if proximo_mes > 12:
            proximo_mes = 1
            proximo_ano += 1
            
        # Roda novamente o calendar.monthcalendar para ter a nova matriz
        matriz_proximo_mes = calendar.monthcalendar(proximo_ano, proximo_mes)
        
        # Pega a variável da primeira semana (índice 0)
        dia_reserva = matriz_proximo_mes[0][int(posicao_dia_reserva)]
        
        # Resolve a inconsistência do zero: se a posição do dia ainda for 0 na primeira semana do mês novo, 
        # significa que a primeira ocorrência desse dia específico está na segunda semana (índice 1).
        if dia_reserva == 0:
            dia_reserva = matriz_proximo_mes[1][int(posicao_dia_reserva)]
            """
    return dia_reserva

###RETORNA DIA/MES/ANO PARA DATA RESERVA
def retornaDataReserva(dia):

    data_reserva_pronta = f"{int(retornaDiaReserva(dia)):02d}/{mes:02d}/{ano}"

    return data_reserva_pronta


#verifica se na semana seguinte tem dias do proximo mes
def verificaExistenciaDiasProximoMes():
    global quant_semanas_mes

    #verificando se estamos na penultima semana
    if dia_atual in matriz_mes_atual[quant_semanas_mes-2]:

        #verificando se tem dias 00
        if 0 in array_matriz_semana_atual[quant_semanas_mes-1]:
            return True
        else:
            return False

def posicaoDiaOutraSemana():
    return True

