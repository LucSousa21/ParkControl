from logica.veiculo import Veiculo
from logica.calculo_valor import calcular_valor
from banco.modelo import Vagas
from banco.registrar_no_banco import registrarCarro, registrarMoto
from banco.liberarVagas import liberarVagasCarros, liberarVagasMotos


# Controle de vagas disponíveis
vagas_moto = [f"M{i}" for i in range(1, 21)]
vagas_carro = [f"C{i}" for i in range(1, 51)]

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
    if tipo == "moto":
        if not vagas_moto:
            raise ValueError("Não há vagas disponíveis para motos.")
        vaga = vagas_moto.pop(0)
    elif tipo == "carro":
        if not vagas_carro:
            raise ValueError("Não há vagas disponíveis para carros.")
        vaga = vagas_carro.pop(0)
    else:
        raise ValueError("Tipo de veículo inválido.")

    veiculo = Veiculo(tipo, vaga)
    veiculos_estacionados.append(veiculo)
    print(f"Entrada registrada: {veiculo}")
    return veiculo


def registrar_saida(vaga_id):
    """
    Registra a saída de um veículo pela vaga, calcula tempo e valor.

    Parâmetros:
        vaga_id (str): ID da vaga (ex: 'C1', 'M3')

    Retorna:
        valor (float): valor a ser cobrado
    """
    # Buscar veículo na lista
    veiculo = next((v for v in veiculos_estacionados if v.vaga_id == vaga_id), None)
    if veiculo is None:
        raise ValueError("Veículo não encontrado no estacionamento.")

    # Registrar saída
    veiculo.registrar_saida()

    # Calcular valor
    valor = calcular_valor(veiculo)

    # Remover veículo da lista
    veiculos_estacionados.remove(veiculo)

    # Liberar vaga novamente
    if veiculo.tipo == "moto":
        vagas_moto.append(veiculo.vaga_id)
        vagas_moto.sort(key=lambda x: int(x[1:]))  # garante ordem M1, M2, ...
    else:
        vagas_carro.append(veiculo.vaga_id)
        vagas_carro.sort(key=lambda x: int(x[1:]))

    print(f"Saída registrada: {veiculo} | Valor a pagar: R${valor}")
    return valor


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
    
def liberarvaga(placa):
    """
    Libera uma vaga específica.

    Parâmetros:
        placa (str): placa do veículo
    """
    if placa.lower() == "carro":
        liberarVagasCarros(placa)
    elif placa.lower() == "moto":
        liberarVagasMotos(placa)
    else:
        raise ValueError("Tipo de veículo inválido.")

