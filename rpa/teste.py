import pyperclip
import calendar


dia = pyperclip.paste().strip()

print(f"Dia q ta sendo copiado: '{dia}'")
retorno_dia = {
        "Seg": 0,
        "Ter": 1,
        "Qua": 2,
        "Qui": 3,
        "Sex": 4
    }

    
posicao_dia_reserva = retorno_dia.get(dia, "DIA NAO RECONHECIDOO")
print(f"Retorno: {posicao_dia_reserva}")


matriz_mes_atual = calendar.monthcalendar(2026, 10)
print(matriz_mes_atual)