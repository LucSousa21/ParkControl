import sqlite3 as db

#Função para criar o banco de dados e as tabelas
def criarbanco():
    try:    
        conncarros = db.connect('banco/BancoVagasCarros.db')
        cursor = conncarros.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS VagasCarros(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ocupada INTEGER DEFAULT 0,
                            vaga INTEGER,
                            veiculo TEXT,
                            placa TEXT UNIQUE
                        )''')
        
        connmotos = db.connect('banco/BancoVagasMotos.db')
        cursor = connmotos.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS VagasMotos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ocupada INTEGER DEFAULT 0,
                            vaga INTEGER,
                            veiculo TEXT,
                            placa TEXT UNIQUE
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
        conncarros = db.connect('banco/BancoVagasCarros.db')
        cursor = conncarros.cursor()
        cursor.execute("""INSERT INTO VagasCarros (vaga) 
                       VALUES (1), (2), (3), (4), (5),
                              (6), (7), (8), (9), (10),
                              (11), (12), (13), (14), (15), 
                              (16), (17), (18), (19), (20)
                       """)
        
        connmotos = db.connect('banco/BancoVagasMotos.db')
        cursor = connmotos.cursor()
        cursor.execute("""INSERT INTO VagasMotos (vaga) 
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