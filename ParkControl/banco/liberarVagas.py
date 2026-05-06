import sqlite3 as db
from banco.modelo import Vagas
import os

# Isso descobre o caminho da pasta onde este arquivo (consultar_banco.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho exato para os bancos de dados
PATH_CARROS = os.path.join(BASE_DIR, 'BancoVagasCarros.db')
PATH_MOTOS = os.path.join(BASE_DIR, 'BancoVagasMotos.db')

def liberarVagasCarros(placa):
    try:
        conn = db.connect(PATH_CARROS)
        cursor = conn.cursor()
        vaga = Vagas(None, None, placa)
        cursor.execute("""
                    UPDATE VagasCarros SET ocupada = 0, vaga = NULL, veiculo = NULL, placa = NULL, entrada = NULL
                    WHERE placa = ?
                    """, (vaga.placa,))
    except db.Error as e:
        raise ValueError(f"Erro ao liberar a vaga: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()

def liberarVagasMotos(placa):
    try:
        conn = db.connect(PATH_MOTOS)
        cursor = conn.cursor()
        vaga = Vagas(None, None, placa)
        cursor.execute("""
                    UPDATE VagasMotos SET ocupada = 0, vaga = NULL, 
                       veiculo = NULL, placa = NULL, entrada = NULL
                    WHERE placa = ?
                    """, (vaga.placa,))
    except db.Error as e:
        raise ValueError(f"Erro ao liberar a vaga: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()


def liberarVagas():
    try:
        conn = db.connect(PATH_CARROS)
        cursor = conn.cursor()
        cursor.execute(""" UPDATE VagasCarros SET ocupada = 0, vaga = NULL, veiculo = NULL, placa = NULL, entrada = NULL """)
        conn.commit()
    except db.Error as e:
        raise ValueError(f"Erro ao liberar as vagas: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()



