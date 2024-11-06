import sqlite3

class DataBase:
    def __init__(self, path = "envio.db"):
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        table = """
        CREATE TABLE IF NOT EXISTS envio ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_envio INTEGER NOT NULL,
            competencia INTEGER NOT NULL,
            nome_arquivo TEXT NOT NULL
        );
            """
        self.cursor.execute(table)
     
    def close(self):
        self.conn.close()
        return True
    
    def get_cursor(self):
        return self.cursor
    
    def get_conn(self):
        return self.conn
    
    def commit(self):
        self.conn.commit()
        return True
    
    def insert(self, data_envio, competencia, nome_arquivo):
        insert = """
        INSERT INTO envio (data_envio, competencia, nome_arquivo) 
        VALUES (?, ?, ?)
        """
        self.cursor.execute(insert, (data_envio, competencia, nome_arquivo))
        self.commit()

    
    def get_envio(self, competencia, file_name):
        select = """
        SELECT * FROM envio
        WHERE competencia = ? AND nome_arquivo = ?
        """
        self.cursor.execute(select, (competencia, file_name))
        search = self.cursor.fetchone()
        if search:
            return search
        else:
            return None
    
if __name__ == "__main__":
    db = DataBase("envio.db")
    db.create_table()
    db.close()