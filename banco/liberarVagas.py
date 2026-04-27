import sqlite3 as db
from modelo import Vagas

def liberarVagasCarros(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                    UPDATE VagasCarros SET ocupada = 0, tipo = NULL, veiculo = NULL, placa = NULL
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
        
        cursor.execute("""
                    UPDATE VagasMotos SET ocupada = 0, tipo = NULL, veiculo = NULL, placa = NULL
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

def liberarVagasCarros(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                    UPDATE VagasCarros SET ocupada = 0, tipo = NULL, veiculo = NULL, placa = NULL
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

