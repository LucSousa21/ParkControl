import sqlite3 as db
from datetime import datetime

def consultarEntrada(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT entrada FROM VagasCarros WHERE placa = ? """, (placa,))
        dados = cursor.fetchall()
        hora_entrada = dados[0][0]
        entrada = datetime.fromisoformat(hora_entrada)
        return entrada
    except db.Error as e:
        print(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()

def verificarTipoVeiculo(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT vaga FROM VagasCarros WHERE placa = ? """, (placa,))
        dados = cursor.fetchall()
        tipo_veiculo = dados[0][0]
        if tipo_veiculo == 'carro':
            return 'carro'
        
        conn = db.connect('banco/BancoVagasMotos.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT vaga FROM VagasMotos WHERE placa = ? """, (placa,))
        dados = cursor.fetchall()
        tipo_veiculo = dados[0][0]
        if tipo_veiculo == 'moto':
            return 'moto'
        
    except db.Error as e:
        print(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()
