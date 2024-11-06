from src.database.db_postgres import DBPostgres
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


db = DBPostgres(db_host, db_port, db_user, db_password, db_name)

print(db.get_nf_entrada())
