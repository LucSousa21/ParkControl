from veiculo import Veiculo
from calculo_valor import calcular_valor

# Lista de veículos atualmente no estacionamento
veiculos_estacionados = []

def registrar_entrada(tipo):
    """
    Registra a entrada de um veículo no estacionamento.

    Parâmetros:
        tipo (str): 'carro' ou 'moto'

    Retorna:
        Veiculo: objeto do veículo registrado
    """
    veiculo = Veiculo(tipo)
    veiculos_estacionados.append(veiculo)
    print(f"Entrada registrada: {veiculo}")
    return veiculo

def registrar_saida(veiculo_id):
    """
    Registra a saída de um veículo pelo ID, calcula tempo e valor.

    Parâmetros:
        veiculo_id (str): ID do veículo a ser retirado

    Retorna:
        valor (float): valor a ser cobrado
    """
    # Buscar veículo na lista
    veiculo = next((v for v in veiculos_estacionados if v.id == veiculo_id), None)
    if veiculo is None:
        raise ValueError("Veículo não encontrado no estacionamento.")

    # Registrar saída
    veiculo.registrar_saida()

    # Calcular valor
    valor = calcular_valor(veiculo)

    # Remover veículo da lista
    veiculos_estacionados.remove(veiculo)

    print(f"Saída registrada: {veiculo} | Valor a pagar: R${valor}")
    return valor
