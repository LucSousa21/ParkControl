import sqlite3 as db


def deletarDados(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM VagasCarros WHERE placa = ?", (placa,))
    except db.Error as e:
        print(f"Erro ao deletar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()