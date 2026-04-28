import sqlite3 as db
from datetime import datetime
from banco.modelo import Vagas

def registrarCarro(vaga):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        vaga = Vagas(vaga.tipo, vaga.modelo, vaga.placa)
        cursor.execute(""" SELECT id FROM VagasCarros 
                       WHERE ocupada = 0 
                       """)
        vaga_id = cursor.fetchone()
        entrada = datetime.now().isoformat()
        
        if vaga_id:
            vaga_id = vaga_id[0]
            cursor.execute(""" UPDATE VagasCarros 
                           SET ocupada = 1, vaga = ?, veiculo = ?, placa = ?, entrada = ? 
                           WHERE id = ? """, (vaga.tipo, vaga.modelo, vaga.placa, entrada, vaga_id))
            
        
        else:
            raise ValueError("Não há vagas disponíveis para este tipo de veículo.")
        
    except db.Error as e:
        print(f"Erro ao registrar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()

def registrarMoto(vaga):
    try:
        conn = db.connect('banco/BancoVagasMotos.db')
        cursor = conn.cursor()
        vaga = Vagas(vaga.tipo, vaga.modelo, vaga.placa)
        cursor.execute(""" SELECT id FROM VagasMotos 
                       WHERE ocupada = 0 
                       """)
        vaga_id = cursor.fetchone()
        entrada = datetime.now().isoformat()
        
        if vaga_id:
            vaga_id = vaga_id[0]
            cursor.execute(""" UPDATE VagasMotos 
                           SET ocupada = 1, vaga = ?, veiculo = ?, placa = ?, entrada = ?
                           WHERE id = ? """, (vaga.tipo, vaga.modelo, vaga.placa, entrada, vaga_id))
            

        else:
            raise ValueError("Não há vagas disponíveis para este tipo de veículo.")
        
    except db.Error as e:
        print(f"Erro ao registrar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()