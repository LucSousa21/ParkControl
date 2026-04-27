import sqlite3 as db
import datetime


def deletarDados(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        
        # Create RecycleBin table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS RecycleBin (
                id INTEGER,
                ocupada INTEGER,
                tipo TEXT,
                veiculo TEXT,
                placa TEXT,
                deleted_at TEXT
            )
        """)
        
        # Select the data to move to recycle bin
        cursor.execute("SELECT id, ocupada, tipo, veiculo, placa FROM VagasCarros WHERE placa = ?", (placa,))
        row = cursor.fetchone()
        
        if row:
            # Insert into RecycleBin
            cursor.execute("""
                INSERT INTO RecycleBin (id, ocupada, tipo, veiculo, placa, deleted_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (row[0], row[1], row[2], row[3], row[4], datetime.datetime.now().isoformat()))
            
            # Delete from main table
            cursor.execute("DELETE FROM VagasCarros WHERE placa = ?", (placa,))
        else:
            print(f"Nenhum registro encontrado para a placa: {placa}")
            
    except db.Error as e:
        print(f"Erro ao deletar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()


def restaurarDados(placa):
    try:
        conn = db.connect('banco/BancoVagasCarros.db')
        cursor = conn.cursor()
        
        # Select from RecycleBin
        cursor.execute("SELECT id, ocupada, tipo, veiculo, placa FROM RecycleBin WHERE placa = ? ORDER BY deleted_at DESC LIMIT 1", (placa,))
        row = cursor.fetchone()
        
        if row:
            # Insert back into VagasCarros
            cursor.execute("""
                INSERT INTO VagasCarros (id, ocupada, tipo, veiculo, placa)
                VALUES (?, ?, ?, ?, ?)
            """, (row[0], row[1], row[2], row[3], row[4]))
            
            # Delete from RecycleBin
            cursor.execute("DELETE FROM RecycleBin WHERE placa = ? AND deleted_at = (SELECT MAX(deleted_at) FROM RecycleBin WHERE placa = ?)", (placa, placa))
            print(f"Dados restaurados para a placa: {placa}")
        else:
            print(f"Nenhum dado encontrado na lixeira para a placa: {placa}")
            
    except db.Error as e:
        print(f"Erro ao restaurar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.commit()
            conn.close()


if __name__ == "__main__":
    deletarDados("aaa")  # Exemplo de uso, substitua pela placa desejada