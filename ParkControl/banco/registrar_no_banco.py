import sqlite3 as db
from datetime import datetime
from banco.modelo import Vagas
import os

# Isso descobre o caminho da pasta onde este arquivo (consultar_banco.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho exato para os bancos de dados
PATH_CARROS = os.path.join(BASE_DIR, 'BancoVagasCarros.db')
PATH_MOTOS = os.path.join(BASE_DIR, 'BancoVagasMotos.db')

def registrarCarro(vaga):
    try:
        conn = db.connect(PATH_CARROS)
        cursor = conn.cursor()
        vaga = Vagas(vaga.tipo, vaga.modelo, vaga.placa)
        cursor.execute(""" SELECT id FROM VagasCarros 
                       WHERE ocupada = 0 
                       """)
        vaga_id = cursor.fetchone()
        entrada = datetime.now().isoformat(timespec='seconds')
        
        if vaga_id:
            vaga_id = vaga_id[0]
            cursor.execute(""" UPDATE VagasCarros 
                           SET ocupada = 1, vaga = ?, veiculo = ?, placa = ?, entrada = ? 
                           WHERE id = ? """, (vaga.tipo, vaga.modelo, vaga.placa, entrada, vaga_id))
            
        
        else:
            raise ValueError("Não há vagas disponíveis para este tipo de veículo.")
        
    except db.Error as e:
        raise ValueError(f"Erro ao registrar os dados: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()

def registrarMoto(vaga):
    try:
        conn = db.connect(PATH_MOTOS)
        cursor = conn.cursor()
        vaga = Vagas(vaga.tipo, vaga.modelo, vaga.placa)
        cursor.execute(""" SELECT id FROM VagasMotos 
                       WHERE ocupada = 0 
                       """)
        vaga_id = cursor.fetchone()
        entrada = datetime.now().isoformat(timespec='seconds')
        
        if vaga_id:
            vaga_id = vaga_id[0]
            cursor.execute(""" UPDATE VagasMotos 
                           SET ocupada = 1, vaga = ?, veiculo = ?, placa = ?, entrada = ?
                           WHERE id = ? """, (vaga.tipo, vaga.modelo, vaga.placa, entrada, vaga_id))
            

        else:
            raise ValueError("Não há vagas disponíveis para este tipo de veículo.")
        
    except db.Error as e:
        raise ValueError(f"Erro ao registrar os dados: {e}")
    except Exception as e:
        raise ValueError(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()