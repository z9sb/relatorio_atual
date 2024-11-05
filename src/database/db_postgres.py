import psycopg2
import df_table

class DBPostgres:
    def __init__(self, host, port, user, password, dbname):
        self.host = host
        self.port = port    
        self.user = user
        self.password = password
        self.dbname = dbname
        
    def connect(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.dbname
        )

    def close(self, conn):
        conn.close()
        return True
    
    def get_cursor(self, conn):
        return conn.cursor()
    
    def get_nf_saida(self, conn):
        cursor = self.get_cursor(conn)
        cursor.execute(
            """SELECT * FROM cadnot
                WHERE dtemissao BETWEEN '2022-01-01' AND '2022-12-31'
            """
        )
        return cursor.fetchall()
        

if __name__ == "__main__":
    db = DBPostgres("localhost", 5432, "postgres", "postgres", "integrapgsql")
    
    connection = db.connect()
    
    for i in db.get_nf_saida(connection):
        print(df_table.NotaFiscal.from_raw_data(i))