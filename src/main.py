from src.database.db_postgres import DBPostgres
from src.database.nf_model_entrada import NFModelEntrada as NFEntrada
from src.database.nf_model_saida import NFModelSaida as NFSaida
from src.utils.date_util import get_month_start, get_month_end, get_month
import os
from dotenv import load_dotenv
import pandas as pd
from src.utils.send_email import create_message_with_attachment, send_message
from src.database.data_base import DataBase
from datetime import datetime

def check_to_send(competencia, file_name):
    send = DataBase().get_envio(competencia, file_name)
    if send:
        return False
    else:
        DataBase().insert(str(datetime.now()), competencia, file_name)
        return True

def send_email_attachment(company, start_date, end_date):
    message = create_message_with_attachment(
        'me', 'contabilidadebento.xml@gmail.com', company[2], f'{company[14]} {start_date} - {end_date}',['nf_saida.csv', 'nf_entrada.csv']
        )
    send_message(message)
      
def dataframe_to_csv(dataframe, filename):
    dataframe = pd.DataFrame(dataframe)
    dataframe.to_csv(filename, index=False)

def load_data(database, tipo: int):
    if tipo == 1:
        return NFEntrada.from_raw_data(database)
    elif tipo == 2:
        return NFSaida.from_raw_data(database)

def main() -> None:
    """
    Main entry point of the application.
    """
    load_dotenv()

    data_entrada = []
    data_saida = []

    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_username = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    db = DBPostgres(db_host, db_port, db_username, db_password, db_name)

    start_date = get_month_start()
    end_date = get_month_end()
    competencia = get_month()
    
    company = db.get_inf_company()

    notas_entrada = db.get_nf_entrada(start_date, end_date)
    notas_saida = db.get_nf_saida(start_date, end_date)

    for nota in notas_entrada:
        entrada = load_data(nota, 1)
        data_entrada.append(entrada)
        
    for nota in notas_saida:
        saida = load_data(nota, 2)
        data_saida.append(saida)

    dataframe_to_csv(data_saida, 'nf_saida.csv')
    dataframe_to_csv(data_entrada, 'nf_entrada.csv')

    entrada_check = check_to_send(competencia, 'nf_saida.csv')
    saida_check = check_to_send(competencia, 'nf_entrada.csv')
    if entrada_check or saida_check:
        send_email_attachment(company, start_date, end_date)

if __name__ == "__main__":
    main()