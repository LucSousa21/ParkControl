import sqlite3 as db
from banco.modelo import Vagas

def liberarVagasCarros(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        vaga = Vagas(None, None, placa)
        cursor.execute("""
                    UPDATE VagasCarros SET ocupada = 0, vaga = id, veiculo = NULL, placa = NULL, entrada = NULL
                    WHERE placa = ?
                    """, (placa,))
    except db.Error as e:
        print(f"Erro ao liberar a vaga: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
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
                    """, (placa,))
    except db.Error as e:
        print(f"Erro ao liberar a vaga: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()



