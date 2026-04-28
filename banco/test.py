import os
from modelo import Vagas
from registrar_no_banco import registrarCarro, registrarMoto
#from consultar_banco import consultarDados
try:
    # Teste de registro de carro
    while True:
        tipo = input("Digite o tipo de veículo (carro/moto): ").strip().lower()
        modelo = input("Digite o modelo do veículo: ").strip()
        placa = input("Digite a placa do veículo: ").strip().upper()
        veiculo = Vagas(tipo, modelo, placa)
        if tipo == 'carro':
            registrarCarro(veiculo)
        elif tipo == 'moto':
            registrarMoto(veiculo)
        else:
            print("Tipo de veículo inválido. Tente novamente.")
            continue
        sair = input("Deseja registrar outro veículo? (s/n): ").strip().lower()
        if sair != 's':
            break

    os.system('cls' if os.name == 'nt' else 'clear')
        
except Exception as e:
    print(f"Erro durante os testes: {e}")

