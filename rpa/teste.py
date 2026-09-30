import pyperclip



dia_copiado = pyperclip.paste().strip()


retorno_dia = {
        "Seg": 0,
        "Ter": 1,
        "Qua": 2,
        "Qui": 3,
        "Sex": 4
    }

posicao_dia_reserva = retorno_dia.get(dia_copiado, 3)

print(posicao_dia_reserva)