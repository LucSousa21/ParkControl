import sqlite3 as db
from modelo import Vagas

def registrarDados(vaga):
    try:
        conn = db.connect('BancoVagasCarros.db')
        cursor = conn.cursor()
        vaga = Vagas(vaga.tipo, vaga.modelo, vaga.placa)
        cursor.execute("""
            INSERT INTO VagasCarros (tipo, modelo, placa) VALUES (?, ?, ?)
        """, (vaga.tipo, vaga.modelo, vaga.placa))
        
    except db.Error as e:
        print(f"Erro ao registrar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()