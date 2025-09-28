from datetime import timedelta

def calcular_valor(veiculo):
    """
    Calcula o valor a ser cobrado de um veículo.
    
    Parâmetros:
        veiculo (Veiculo): objeto da classe Veiculo
    
    Retorna:
        valor_total (float): valor a ser cobrado
    """
    tempo = veiculo.calcular_tempo_permanencia()
    horas = tempo.total_seconds() / 3600  # converte para horas

    # Valor base
    if veiculo.tipo == 'carro':
        valor_base = 8
    elif veiculo.tipo == 'moto':
        valor_base = 4
    else:
        raise ValueError("Tipo de veículo inválido")

    # Se passou das 4 horas, calcular cobrança extra
    if horas <= 4:
        return valor_base
    else:
        excesso = tempo - timedelta(hours=4)   # tempo excedente
        minutos_excedentes = excesso.total_seconds() / 60
        cobranca_extra = (minutos_excedentes // 20) * 1  # R$1 a cada 20 minutos
        valor_total = valor_base + cobranca_extra
        return valor_total
