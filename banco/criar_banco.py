import sqlite3 as db

def criarbanco():
    try:    
        conn = db.connect('banco/BancoVagasMotos.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS VagasMotos(
                            id INTEGER PRIMARY KEY,
                            ocupada INTEGER DEFAULT 0,
                            tipo TEXT,
                            veiculo TEXT,
                            placa TEXT UNIQUE
                        )''')
    
    except db.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    except Exception as error:
        print(f"Erro inesperado: {error}")    
    finally:
        if conn:
            conn.commit()
            conn.close()


if __name__ == "__main__":

    criarbanco()