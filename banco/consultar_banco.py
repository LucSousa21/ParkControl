import sqlite3 as db
from datetime import datetime

def consultarEntradaCarro(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT entrada FROM VagasCarros WHERE placa = ? """, (placa,))
        dados = cursor.fetchone()
        if not dados:
            return None
        hora_entrada = dados[0]
        entrada = datetime.fromisoformat(hora_entrada)
        return entrada
    except db.Error as e:
        raise ValueError(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()

def consultarEntradaMoto(placa):
    try:
        conn = db.connect('banco/BancoVagasMotos.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT entrada FROM VagasMotos WHERE placa = ? """, (placa,))
        dados = cursor.fetchone()
        if not dados:
            return None
        hora_entrada = dados[0]
        entrada = datetime.fromisoformat(hora_entrada)
        return entrada
    except db.Error as e:
        raise ValueError(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()


def verificarTipoVeiculo(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT vaga FROM VagasCarros WHERE placa = ? """, (placa,))
        dados = cursor.fetchone()
        if not dados:
            return None
        tipo_veiculo = dados[0]
        if tipo_veiculo == 'carro':
            return 'carro'
        
        conn = db.connect('banco/BancoVagasMotos.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT vaga FROM VagasMotos WHERE placa = ? """, (placa,))
        dados = cursor.fetchone()
        if not dados:
            return None
        tipo_veiculo = dados[0]
        if tipo_veiculo == 'moto':
            return 'moto'
        
    except db.Error as e:
        raise ValueError(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()

def exibirVagas():
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT *, placa FROM VagasCarros """)
        vagas_carros = cursor.fetchall()
        
        conn = db.connect('banco/BancoVagasMotos.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT *, placa FROM VagasMotos """)
        vagas_motos = cursor.fetchall()
        
        return vagas_carros, vagas_motos
    except db.Error as e:
        raise ValueError(f"Erro ao consultar os dados: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()
