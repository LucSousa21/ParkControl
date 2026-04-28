from banco.modelo import Vagas
from banco.registrar_no_banco import registrarCarro, registrarMoto
from banco.liberarVagas import liberarVagasCarros, liberarVagasMotos

def registrar_veiculo(tipo, modelo, placa):
    """
    Registra um veículo no banco de dados.

    Parâmetros:
        tipo (str): 'carro' ou 'moto'
        modelo (str): modelo do veículo
        placa (str): placa do veículo
    """
    veiculo = Vagas(tipo, modelo, placa)  # vaga será atribuída no registro
    if tipo.lower() == "carro":
        registrarCarro(veiculo)
    elif tipo.lower() == "moto":
        registrarMoto(veiculo)
    else:
        raise ValueError("Tipo de veículo inválido.")
    
def liberarvaga(tipo,placa):
    """
    Libera uma vaga específica.

    Parâmetros:
        tipo (str): 'carro' ou 'moto'
        placa (str): placa do veículo
    """
    if tipo.lower() == "carro":
        liberarVagasCarros(placa)
    elif tipo.lower() == "moto":
        liberarVagasMotos(placa)
    else:
        raise ValueError("Tipo de veículo inválido.")
