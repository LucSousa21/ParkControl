import sqlite3 as db
from banco.modelo import Vagas

def liberarVagasCarros(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
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
        conn = db.connect('banco/BancoVagasMotos.db')
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
    conn = db.connect('banco/BancoVagasCarros.db')
    cursor = conn.cursor()
    cursor.execute(""" UPDATE VagasCarros SET ocupada = 0, vaga = NULL, veiculo = NULL, placa = NULL, entrada = NULL """)
    conn.commit()
    conn.close()



