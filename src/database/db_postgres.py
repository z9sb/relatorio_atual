import psycopg2

class DBPostgres:
    def __init__(self, host, port, user, password, dbname):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connect = self._connect()

    def _connect(self):
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

    def get_nf_saida(self, dt_start, dt_end):
        """Get all NF Saida from database."""
        cursor = self.get_cursor(self.connect)
        query = """
            SELECT * FROM cadnot
            WHERE dtemissao BETWEEN %s AND %s
        """
        cursor.execute(query, (dt_start, dt_end))
        return cursor.fetchall()

    def get_nf_entrada(self, dt_start, dt_end):
        """Get all NF Entrada from database.
        Data dt_emissao as data de emissao"""
        cursor = self.get_cursor(self.connect)
        query = """
            SELECT *
            FROM pedntf nf
            JOIN pedinf inf ON nf.nota_fiscal = inf.nota_fiscal
            JOIN cadpro cad ON inf.matricula = cad.matricula
            WHERE nf.dt_emissao BETWEEN %s AND %s
        """
        cursor.execute(query, (dt_start, dt_end))
        return cursor.fetchall()

    def get_inf_company(self):
        cursor = self.get_cursor(self.connect)
        query = """
            SELECT * FROM public.cadfil cad
            WHERE cad.regime_trib = '1';
            """
        cursor.execute(query)
        return cursor.fetchone()


if __name__ == "__main__":
    db = DBPostgres("localhost", 5432, "postgres",
                    "postgres", "integrapgsql")
    #print(db.get_nf_entrada())
    company = list(db.get_inf_company())
    print(company[14])
