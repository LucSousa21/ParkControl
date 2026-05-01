import re
from banco.modelo import Vagas
from banco.registrar_no_banco import registrarCarro, registrarMoto
from banco.liberarVagas import liberarVagasCarros, liberarVagasMotos

def obter_placa_tratada(placa):
        # 1. Remove qualquer caractere que não seja letra ou número
        placa_limpa = re.sub(r"[^a-zA-Z0-9]", "", placa).upper()

        # 2. Verifica se a placa tem o tamanho correto de 7 dígitos
        if len(placa_limpa) != 7:
            raise ValueError("Erro: A placa deve conter exatamente 7 caracteres.")

        # 3. Identifica e formata o padrão Antigo (ex: AAA1234)
        if re.match(r"^[A-Z]{3}[0-9]{4}$", placa_limpa):
            placa_formatada = placa_limpa.upper().strip()
            return placa_formatada

        # 4. Identifica o padrão Mercosul (ex: AAA1B23)
        elif re.match(r"^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$", placa_limpa):
            placa_formatada = placa_limpa.upper().strip()
            return placa_formatada

        else:
            raise ValueError("Erro: Formato de placa inválido.")

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
    
