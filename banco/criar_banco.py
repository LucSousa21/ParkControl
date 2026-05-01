import os
import sqlite3 as db

# Pega o caminho da pasta onde este arquivo criar_banco.py está guardado
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Define os caminhos exatos dos arquivos de banco de dados
DB_CARROS = os.path.join(DIRETORIO_ATUAL, 'BancoVagasCarros.db')
DB_MOTOS = os.path.join(DIRETORIO_ATUAL, 'BancoVagasMotos.db')#Função para criar o banco de dados e as tabelas
def criarbanco():
    try:    
        conncarros = db.connect(DB_CARROS)
        cursor = conncarros.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS VagasCarros(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ocupada INTEGER DEFAULT 0,
                            vaga TEXT,
                            veiculo TEXT,
                            placa TEXT UNIQUE,
                            entrada TEXT
                        )''')
        
        connmotos = db.connect(DB_MOTOS)
        cursor = connmotos.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS VagasMotos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ocupada INTEGER DEFAULT 0,
                            vaga TEXT,
                            veiculo TEXT,
                            placa TEXT UNIQUE,
                            entrada TEXT
                        )''')
    
    except db.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    except Exception as error:
        print(f"Erro inesperado: {error}")    
    finally:
        if conncarros:
            conncarros.commit()
            conncarros.close()

        if connmotos:
            connmotos.commit()
            connmotos.close()


#Função para inserir vagas disponíveis no banco de dados
def vagas_disponiveis():
    try:
        conncarros = db.connect(DB_CARROS)
        cursor = conncarros.cursor()
        cursor.execute("""INSERT INTO VagasCarros (id) 
                       VALUES (1), (2), (3), (4), (5),
                              (6), (7), (8), (9), (10),
                              (11), (12), (13), (14), (15), 
                              (16), (17), (18), (19), (20)
                       """)
        
        connmotos = db.connect(DB_MOTOS)
        cursor = connmotos.cursor()
        cursor.execute("""INSERT INTO VagasMotos (id) 
                        VALUES (1), (2), (3), (4), (5),
                               (6), (7), (8), (9), (10)
                       """)
    

    except db.Error as e:
        print(f"Erro ao inserir vagas: {e}")
    except Exception as error:
        print(f"Erro inesperado: {error}")    
    finally:
        if conncarros:
            conncarros.commit()
            conncarros.close()

        if connmotos:
            connmotos.commit()
            connmotos.close()

if __name__ == "__main__":
    criarbanco()
    vagas_disponiveis()