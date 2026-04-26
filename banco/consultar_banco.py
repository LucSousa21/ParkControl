import sqlite3 as db

def consultarDados(placa):
    try:
        conn = db.connect('banco/BancoVagas.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM Vagas WHERE placa = ? """, (placa,))
        dados = cursor.fetchall()
        return dados
    except db.Error as e:
        print(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()