from datetime import datetime, timedelta
from banco.consultar_banco import consultarEntradaCarro, consultarEntradaMoto, verificarTipoVeiculo


def calcular_valor(tipo, placa):

        
    
    entrada = consultarEntradaCarro(placa) if tipo == 'carro' else consultarEntradaMoto(placa)
    if not entrada:
        raise ValueError("Veículo não encontrado no banco de dados.")
    saida = datetime.now()
    tempo = saida - entrada
    horas = tempo.total_seconds() / 3600  # converte para horas

    # Valor base
    if tipo == 'carro':
        valor_base = 8
    elif tipo == 'moto':
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
    
