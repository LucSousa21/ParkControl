import os
from banco.modelo import Vagas
from banco.liberarVagas import liberarVagasMotos


try:
    placa = 'ABC1234'
    liberarVagasMotos(placa)
    print(f"Vaga liberada para a placa {placa}")
except Exception as e:
    print(f"Erro durante os testes: {e}")