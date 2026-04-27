import os
from modelo import Vagas
from registrar_no_banco import registrarCarro, registrarMoto
from deletar_dados import deletarDados
from consultar_banco import consultarDados
try:
    while True:

        tipo = input('Tipo do veículo (carro, moto) ou "sair" para encerrar: ').strip()
        if tipo.lower() == "sair":
            break

        modelo = input('Modelo do veículo ou "sair" para encerrar: ').strip()
        if modelo.lower() == "sair":
            break

        placa = input('Placa do veículo ou "sair" para encerrar: ').strip()
        if placa.lower() == "sair":
            break

        vaga = Vagas(tipo, modelo, placa)
        if tipo.lower() == "carro":
            registrarCarro(vaga)
        elif tipo.lower() == "moto":
            registrarMoto(vaga)
        print("Testes de registro concluídos.")

        os.system('cls' if os.name == 'nt' else 'clear')
        
except Exception as e:
    print(f"Erro durante os testes: {e}")

